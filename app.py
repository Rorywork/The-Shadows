import os
from flask import Flask, flash, render_template, redirect, request, url_for, session, logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)
app.secret_key =  os.environ.get('SECRET_KEY')

app.config["MONGO_DBNAME"] = 'myTestDB'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session: 
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/upload')
@is_logged_in
def upload():
    return render_template('upload-photo.html')


@app.route('/create', methods=['POST'])
def create():
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        mongo.save_file(image_file.filename, image_file)
        mongo.db.photos.insert({'username' : request.form.get('username'), 'image_file' : image_file.filename, 'image_name' : request.form.get('image_name'), 'image_description' : request.form.get('image_description'), 'image_category' : request.form.get('image_category'), 'image_rotation' : request.form.get('image_rotation')})
        #photo2show = mongo.db.photos.find_one_or_404({"_id" : ObjectId(photoid)})
        flash("The photo was uploaded to the site.")
    return render_template('showphotos.html', photos=mongo.db.photos.find().sort([('_id', -1),]))

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


@app.route('/photo/<image_name>')
def getImage(image_name):
    print(image_name)
    photo = mongo.db.photos.find_one_or_404({'image_name' : image_name})
    print(photo)
    return f'''
        
        <img src="{url_for('file', filename=photo['image_file'])}">
        
    '''

@app.route('/showphotos')
def showphotos():
    # Show all photo sorted by creation date - from the _id    
    return render_template('showphotos.html', photos=mongo.db.photos.find().sort([('_id', -1),]))    


@app.route('/showphotosbycategory/<category>')
def showphotosbycategory(category):
    flash("Showing photographs for the category: {}".format(category))
    return render_template('showphotos.html', photos=mongo.db.photos.find({"image_category" : category }).sort([('_id', -1),]))


@app.route('/deletephoto/<photoid>')
def deletephoto(photoid):
    photo2delete = mongo.db.photos.find_one_or_404({"_id" : ObjectId(photoid)})
    mongo.db.photos.delete_one({"_id" : ObjectId(photoid)})
    flash("The photograph {} has been deleted.".format(photo2delete['image_name']))
    # return f'''
    #     <h1>{photo2delete['image_description']} DELETED.</h1>
    # '''
    return render_template('showphotos.html', photos=mongo.db.photos.find().sort([('_id', -1),]))    

class PhotoForm(Form):
    username = StringField('User Name', [validators.Length(min=1, max=50)])
    image_name = StringField('Image Name', [validators.Length(min=1, max=200)])
    image_description = StringField('Image Description', [validators.Length(min=1, max=200)])
    image_file = StringField('Image File', [validators.Length(min=1, max=500)])
    #image_category = SelectField('Image Category',choices=['People','Animals','Natural', 'Urban'])



@app.route('/editphotodetails/<photoid>', methods=['GET', 'POST'])
def editphotodetails(photoid):
    #Get photo to edit
    photo2edit = mongo.db.photos.find_one_or_404({"_id" : ObjectId(photoid)})
    #Get form to edit
    form = PhotoForm(request.form)
    #Pre-populate form with values
    print(photo2edit['username'])
    form.username.data = photo2edit['username']
    form.image_name.data = photo2edit['image_name']
    form.image_description.data = photo2edit['image_description']
    form.image_file.data = photo2edit['image_file']
    #form.image_category.data = photo2edit['image_category']
    if request.method =='POST' and form.validate():
        username = request.form['username']
        image_name = request.form['image_name']
        image_description = request.form['image_description']
        #image_file = request.form['image_file'] ..... cannot capture this due to HTML security
        #image_category = request.form['image_category']
        # Update the record
        mongo.db.photos.update_one({"_id" : ObjectId(photoid)} , { '$set' : {'username': username}})
        # ..... more to come.....
        flash('Photo {} has been updated.'.format(image_name), 'success')
        return render_template('showphotos.html', photos=mongo.db.photos.find().sort([('_id', -1),]))    

    return render_template('edit-photo.html', form=form)    

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        #insert into the MongoDB
        mongo.db.users.insert({'name' : name, 'email' : email, 'username' : username, 'password' : password})
        
        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        doc_count = mongo.db.users.count_documents({'username' : username})
        
        if doc_count > 0:

            result = mongo.db.users.find_one_or_404({'username' : username})
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

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect (url_for('login'))



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# if __name__ == '__main__':
#     app.run(debug=True)

# The above is required for local development but
# needs to be commented out to run in Heroku and replaced with the below code

if __name__ == '__main__':
   from os import environ
   app.run(debug=False, host='0.0.0.0',port=environ.get("PORT", 5000))    