import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myTestDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:B4dmintonC0d3@myfirstcluster-tdray.mongodb.net/myTestDB?retryWrites=true&w=majority'

mongo = PyMongo(app)
# print(mongo.db)



#@app.route('/get_tasks')
#def get_tasks():
#    return render_template('tasks.html', tasks=mongo.db.tasks.find())

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('tasks.html', photos=mongo.db.photos.find())



@app.route('/upload')
def upload():
    return render_template('upload-photo.html')


@app.route('/create', methods=['POST'])
def create():
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        mongo.save_file(image_file.filename, image_file)
        mongo.db.photos.insert({'username' : request.form.get('username'), 'image_file' : image_file.filename, 'image_name' : request.form.get('image_name'), 'image_description' : request.form.get('image_description'), 'image_category' : request.form.get('image_category'), 'image_rotation' : request.form.get('image_rotation')})
    
    return 'Done!'

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
    return render_template('_showphotos.html', photos=mongo.db.photos.find())    


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == '__main__':
    app.run(debug=True)

# The above is required for local development but
# needs to be commented out to run in Heroku and replaced with the below code

#if __name__ == '__main__':
#    from os import environ
#    app.run(debug=False, host='0.0.0.0',port=environ.get("PORT", 5000))    