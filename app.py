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
search = False
per_page = 5
bs_version = 4


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


@APP.route('/')
def index():
    """This will render the homepage"""
    return render_template('home.html')


@APP.route('/upload')
@is_logged_in
def upload():
    return render_template('upload-photo.html')


@APP.route('/create', methods=['POST'])
def create():
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        MONGO.save_file(image_file.filename, image_file)
        MONGO.db.photos.insert({'username': session['username'], 'image_file': image_file.filename, 'image_name': request.form.get(
            'image_name'), 'image_description': request.form.get('image_description'), 'image_category': request.form.get('image_category'), 'image_rotation': request.form.get('image_rotation')})
        page = request.args.get(get_page_parameter(), type=int, default=1)
        photos = MONGO.db.photos
        allphotos = photos.find().skip((page - 1) * per_page).sort([('_id', -1), ]).limit(per_page)
        pagination = Pagination(page=page, per_page=5, total=allphotos.count(), search=search, record_name='photos', bs_version=bs_version, css_framework='bootstrap', show_single_page=False)
        flash("The photo was uploaded to the site.", 'success')
    return render_template('showphotos.html', photos= allphotos, pagination= pagination)


@APP.route('/file/<filename>')
def file(filename):
    return MONGO.send_file(filename)


@APP.route('/photo/<image_name>')
def getImage(image_name):
    print(image_name)
    photo = MONGO.db.photos.find_one_or_404({'image_name': image_name})
    print(photo)
    return f'''
        
        <img src="{url_for('file', filename=photo['image_file'])}">
        
    '''


@APP.route('/showphoto/<photoid>')
def showphoto(photoid):
     # Show individual photo
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    onephoto = photos.find({"_id": ObjectId(photoid)}).skip((page - 1) * per_page).sort([('_id', -1), ]).limit(per_page)
    pagination = Pagination(page=page, per_page=5, total=onephoto.count(), search=search, record_name='photos', bs_version=bs_version, css_framework='bootstrap', show_single_page=False)
    return render_template('showphotos.html', photos= onephoto, pagination= pagination)

@APP.route('/showphotos')
def showphotos():
    # Show all photo sorted by creation date - from the _id
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    allphotos = photos.find().skip((page - 1) * per_page).sort([('_id', -1), ]).limit(per_page)
    pagination = Pagination(page=page, per_page=5, total=allphotos.count(), search=search, record_name='photos', bs_version=bs_version, css_framework='bootstrap', show_single_page=False)
    return render_template('showphotos.html', photos= allphotos, pagination= pagination)


@APP.route('/showphotosbycategory/<category>')
def showphotosbycategory(category):
    # Show photos filtered by category and sorted by creation date 
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    catphotos = photos.find({"image_category": category}).skip((page - 1) * per_page).sort([('_id', -1), ]).limit(per_page)
    pagination = Pagination(page=page, per_page=5, total=catphotos.count(), search=search, record_name='photos', bs_version=bs_version, css_framework='bootstrap', show_single_page=False)
    flash("Showing photographs for the category: {}".format(category))
    return render_template('showphotos.html', photos= catphotos, pagination= pagination)


@APP.route('/deletephoto/<photoid>')
def deletephoto(photoid):
    photo2delete = MONGO.db.photos.find_one_or_404({"_id": ObjectId(photoid)})
    MONGO.db.photos.delete_one({"_id": ObjectId(photoid)})
    page = request.args.get(get_page_parameter(), type=int, default=1)
    photos = MONGO.db.photos
    allphotos = photos.find().skip((page - 1) * per_page).sort([('_id', -1), ]).limit(per_page)
    pagination = Pagination(page=page, per_page=5, total=allphotos.count(), search=search, record_name='photos', bs_version=bs_version, css_framework='bootstrap', show_single_page=False)
    flash("The photograph {} has been deleted.".format(
        photo2delete['image_name']), 'success')
    return render_template('showphotos.html', photos= allphotos, pagination= pagination)


class PhotoForm(Form):
    username = StringField('User Name', [validators.Length(min=1, max=50)])
    image_name = StringField('Image Name', [validators.Length(min=1, max=200)])
    image_description = StringField(
        'Image Description', [validators.Length(min=1, max=200)])
    image_file = StringField('Image File', [validators.Length(min=1, max=500)])
    #image_category = SelectField('Image Category',choices=['People','Animals','Natural', 'Urban'])


@APP.route('/editphotodetails/<photoid>', methods=['GET', 'POST'])
def editphotodetails(photoid):
    # Get photo to edit
    photo2edit = MONGO.db.photos.find_one_or_404({"_id": ObjectId(photoid)})
    # Get form to edit
    form = PhotoForm(request.form)
    # Pre-populate form with values
    print(photo2edit['username'])
    form.username.data = photo2edit['username']
    form.image_name.data = photo2edit['image_name']
    form.image_description.data = photo2edit['image_description']
    form.image_file.data = photo2edit['image_file']
    #form.image_category.data = photo2edit['image_category']
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        image_name = request.form['image_name']
        image_description = request.form['image_description']
        # image_file = request.form['image_file'] ..... cannot capture this due to HTML security
        image_category = request.form['image_category']
        # Update the record
        MONGO.db.photos.update_one({"_id": ObjectId(photoid)}, {
            '$set': {'username': username, 'image_name': image_name, 'image_description': image_description, "image_category": image_category }})

        flash('Photo {} has been updated.'.format(image_name), 'success')
        page = request.args.get(get_page_parameter(), type=int, default=1)
        photos = MONGO.db.photos
        allphotos = photos.find().skip((page - 1) * per_page).sort([('_id', -1), ]).limit(per_page)
        pagination = Pagination(page=page, per_page=5, total=allphotos.count(), search=search, record_name='photos', bs_version=bs_version, css_framework='bootstrap', show_single_page=False)
        return render_template('showphotos.html', photos= allphotos, pagination= pagination)

    return render_template('edit-photo.html', form=form)

@APP.route('/postcomment/<photoid>', methods=['POST'])
def postcomment(photoid):
    #print(photoid)
    #print(request.form.get('comment'))
    MONGO.db.photos.update_one({'_id': ObjectId(photoid)}, {'$push': {'comments': request.form.get('comment')}}, upsert=True)
    flash("Your comment has been added to the photo.", 'success')
    return redirect(url_for('showphoto', photoid=photoid))

@APP.route('/addlike/<photoid>', methods=['POST'])
def addlike(photoid):
    MONGO.db.photos.update_one({'_id': ObjectId(photoid)}, {'$inc': {'likes': 1}}, upsert=True)
    flash("Your 'like' has been added to the photo.", 'success')
    return redirect(url_for('showphoto', photoid=photoid))

class RegisterForm(Form):
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
    if request.method == 'POST':
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

    return render_template('login.html')


@APP.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# if __name__ == '__main__':
#     app.run(debug=True)

# The above is required for local development but
# needs to be commented out to run in Heroku and replaced with the below code

if __name__ == '__main__':
    APP.run(debug=os.environ.get('DEBUG'), host=os.environ.get(
        'IP'), port=os.environ.get('PORT'))
