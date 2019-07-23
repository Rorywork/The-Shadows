import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import flask_pymongo
from bson.onject.id import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myTestDB'
app.config{"MONGO_URI"} = 'mongodb+srv://root:B4dmintonC0d3@myfirstcluster-tdray.mongodb.net/myTestDB?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template('tasks.html', tasks=mongo.db.tasks.find())

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, host='0.0.0.0',port=environ.get("PORT", 5000))    
  

# test code c