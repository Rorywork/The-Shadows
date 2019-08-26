'''This is the overall controlling program for The Shadows website'''
import os
from functools import wraps
from flask import Flask, flash, render_template, redirect, request, url_for, session, logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_paginate import Pagination, get_page_parameter


APP = Flask(__name__)
APP.secret_key = os.environ.get('SECRET_KEY')

APP.config["MONGO_DBNAME"] = 'myTestDB'
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

MONGO = PyMongo(APP)

# Pagination defaults
SEARCH = False
PER_PAGE = 5
BS_VERSION = 4


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@APP.route('/')
def index():
    """This will render the homepage"""
    return render_template('home.html')


@APP.route('/upload')
@is_logged_in
def upload():
    """This will render the upload photo page when user is logged in"""
    return render_template('upload-photo.html')


@APP.route('/create', methods=['POST'])
def create():
    """This will save the uploaded photo and associated attributes to the MongoDB"""
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        MONGO.save_file(image_file.filename, image_file)
        MONGO.db.photos.insert({'username': session['username'],
                                'image_file': image_file.filename,
                                'image_name': request.form.get('image_name'),
                                'image_description': request.form.get('image_description'),
                                'image_category': request.form.get('image_category'),
                                'image_rotation': request.form.get('image_rotation')})
        page = request.args.get(get_page_parameter(), type=int, default=1)
        photos = MONGO.db.photos
        allphotos = photos.find().skip(
            (page - 1) * PER_PAGE).sort([('_id', -1), ]).limit(PER_PAGE)
        pagination = Pagination(page=page, per_page=5, total=allphotos.count(),
                                search=SEARCH, record_name='photos', bs_version=BS_VERSION,
                                css_framework='bootstrap', show_single_page=False)
        flash("The photo was uploaded to the site.", 'success')
    return redirect("/showphotos")


@APP.route('/file/<filename>')
def file(filename):
    """This is used to save the image onto the MongoDB"""
    return MONGO.send_file(filename)


@APP.route('/showphoto/<photoid>')
def showphoto(photoid):
    """This is used to show an individual photo based upon it's unique ID number"""
     # Show individual photo
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    onephoto = photos.find({"_id": ObjectId(photoid)}).skip(
        (page - 1) * PER_PAGE).sort([('_id', -1), ]).limit(PER_PAGE)
    pagination = Pagination(page=page, per_page=5, total=onephoto.count(),
                            search=SEARCH, record_name='photos', bs_version=BS_VERSION,
                            css_framework='bootstrap', show_single_page=False)
    return render_template('showphotos.html', photos=onephoto, pagination=pagination)


@APP.route('/showphotos')
def showphotos():
    """Used to show all photos and also group and count the photos categories for use in buttons."""
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    allphotos = photos.find().skip(
        (page - 1) * PER_PAGE).sort([('_id', -1), ]).limit(PER_PAGE)
    agr = [{'$match': {'image_category': {'$ne': None}}},
           {'$group': {'_id': '$image_category', 'myCount': {'$sum': 1}}},
           {'$sort': {'myCount': -1, '_id': 1}}
           ]
    grp = list(MONGO.db.photos.aggregate(agr))
    tot = MONGO.db.photos.find().count()
    pagination = Pagination(page=page, per_page=5, total=allphotos.count(),
                            search=SEARCH, record_name='photos', bs_version=BS_VERSION,
                            css_framework='bootstrap', show_single_page=False)                        
    return render_template('showphotos.html', photos=allphotos, grp=grp,
                           total=tot, pagination=pagination)


@APP.route('/showphotosbycategory/<category>')
def showphotosbycategory(category):
    """Shows photos by category"""
    # Show photos filtered by category and sorted by creation date
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    catphotos = photos.find({"image_category": category}).skip(
        (page - 1) * PER_PAGE).sort([('_id', -1), ]).limit(PER_PAGE)
    agr = [{'$match': {'image_category': {'$ne': None}}},
           {'$group': {'_id': '$image_category', 'myCount': {'$sum': 1}}},
           {'$sort': {'myCount': -1, '_id': 1}}
           ]
    grp = list(MONGO.db.photos.aggregate(agr))
    tot = MONGO.db.photos.find().count()
    pagination = Pagination(page=page, per_page=5, total=catphotos.count(
    ), search=SEARCH, record_name='photos', bs_version=BS_VERSION, css_framework='bootstrap', show_single_page=False)
    return render_template('showphotos.html', photos=catphotos, grp=grp, total=tot, pagination=pagination)


@APP.route('/deletephoto/<photoid>')
def deletephoto(photoid):
    """Used to delete photos when you are logged in as the superuser"""
    photo2delete = MONGO.db.photos.find_one_or_404({"_id": ObjectId(photoid)})
    MONGO.db.photos.delete_one({"_id": ObjectId(photoid)})
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    allphotos = photos.find().skip(
        (page - 1) * PER_PAGE).sort([('_id', -1), ]).limit(PER_PAGE)
    pagination = Pagination(page=page, per_page=5, total=allphotos.count(
    ), search=SEARCH, record_name='photos', bs_version=BS_VERSION, css_framework='bootstrap', show_single_page=False)
    flash("The photograph {} has been deleted.".format(
        photo2delete['image_name']), 'success')
    return render_template('showphotos.html', photos=allphotos, pagination=pagination)


class PhotoForm(Form):
    """Defines the form for editing photo details"""
    username = StringField('User Name', [validators.Length(min=1, max=50)])
    image_name = StringField('Image Name', [validators.Length(min=1, max=200)])
    image_description = StringField(
        'Image Description', [validators.Length(min=1, max=200)])
    image_file = StringField('Image File', [validators.Length(min=1, max=500)])



@APP.route('/editphotodetails/<photoid>', methods=['GET', 'POST'])
def editphotodetails(photoid):
    """Used for editing photographs when logged in as superuser"""
    photo2edit = MONGO.db.photos.find_one_or_404({"_id": ObjectId(photoid)})
    form = PhotoForm(request.form)
    print(photo2edit['username'])
    form.username.data = photo2edit['username']
    form.image_name.data = photo2edit['image_name']
    form.image_description.data = photo2edit['image_description']
    form.image_file.data = photo2edit['image_file']
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        image_name = request.form['image_name']
        image_description = request.form['image_description']
        image_category = request.form['image_category']
        MONGO.db.photos.update_one({"_id": ObjectId(photoid)}, {
            '$set': {'username': username, 'image_name': image_name,
                     'image_description': image_description, "image_category": image_category}})

        flash('Photo {} has been updated.'.format(image_name), 'success')
        page = request.args.get(get_page_parameter(), type=int, default=1)
        photos = MONGO.db.photos
        allphotos = photos.find().skip(
            (page - 1) * PER_PAGE).sort([('_id', -1), ]).limit(PER_PAGE)
        pagination = Pagination(page=page, per_page=5, total=allphotos.count(),
                                search=SEARCH, record_name='photos', bs_version=BS_VERSION,
                                css_framework='bootstrap', show_single_page=False)
        return render_template('showphotos.html', photos=allphotos, pagination=pagination)

    return render_template('edit-photo.html', form=form)


@APP.route('/postcomment/<photoid>', methods=['POST'])
def postcomment(photoid):
    """Used to post comments"""
    MONGO.db.photos.update_one({'_id': ObjectId(photoid)},
                               {'$push': {'comments': request.form.get('comment')}}, upsert=True)
    flash("Your comment has been added to the photo.", 'success')
    return redirect(url_for('showphoto', photoid=photoid))


@APP.route('/addlike/<photoid>', methods=['POST'])
def addlike(photoid):
    """Used to add likes to photos"""
    MONGO.db.photos.update_one({'_id': ObjectId(photoid)},
                               {'$inc': {'likes': 1}}, upsert=True)
    flash("Your 'like' has been added to the photo.", 'success')
    return redirect(url_for('showphoto', photoid=photoid))


class RegisterForm(Form):
    """Form definition for registration"""
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@APP.route('/register', methods=['GET', 'POST'])
def register():
    """Used to register a new user and to sign into the site"""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        # insert into the MongoDB
        MONGO.db.users.insert(
            {'name': name, 'email': email, 'username': username, 'password': password})
        session['logged_in'] = True
        session['username'] = username
        flash('You are now registered and have full access to the site', 'success')

        return redirect(url_for('showphotos'))
    return render_template('register.html', form=form)


@APP.route('/login', methods=['GET', 'POST'])
def login():
    """Used to login to the site"""
    if request.method == 'POST' and "loginForm" in request.form:
        username = request.form['username']
        password_candidate = request.form['password']

        doc_count = MONGO.db.users.count_documents({'username': username})

        if doc_count > 0:

            result = MONGO.db.users.find_one_or_404({'username': username})
            password = result['password']

            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('showphotos'))
            else:
                error = 'Invalid Login'
                return render_template('login.html', error=error)

        else:

            error = 'Username not found'
            return render_template('login.html', error=error)

    if request.method == 'POST' and "commentForm" in request.form:
        flash('You must login to add a comment', 'error')
    if request.method == 'POST' and "likeForm" in request.form:
        flash("You must login to 'like' a photo", 'error')

    return render_template('login.html')


@APP.route('/logout')
def logout():
    """Used to logout of the site"""
    flash('You are now logged out', 'success')
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    APP.run(debug=os.environ.get('DEBUG'), host=os.environ.get(
        'IP'), port=os.environ.get('PORT'))
