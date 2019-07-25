import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myTestDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:B4dmintonC0d3@myfirstcluster-tdray.mongodb.net/myTestDB?retryWrites=true&w=majority'

mongo = PyMongo(app)




#@app.route('/get_tasks')
#def get_tasks():
#    return render_template('tasks.html', tasks=mongo.db.tasks.find())

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('tasks.html', tasks=mongo.db.myFirstMDB.find())



@app.route('/upload')
def upload():
    return render_template('upload-photo.html')


@app.route('/create', methods=['POST'])
def create():
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        mongo.save_file(image_file.filename, image_file)
        mongo.db.users.insert({'username' : request.form.get('username'), 'image_file' : image_file.filename, 'image_name' : request.form.get('image_name'), 'image_description' : request.form.get('image_description')})
    
    return 'Done!'

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.users.find_one_or_404({'username' : username})
    return f'''
        <h1>{username}</h1>
        <img src="{url_for('file', filename=user['profile_image_name'])}">
    '''



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == '__main__':
    app.run(debug=True)

# The above is required for local development but
# needs to be commented out to run in Heroku and replaced with the below code

#if __name__ == '__main__':
#    from os import environ
#    app.run(debug=False, host='0.0.0.0',port=environ.get("PORT", 5000))    