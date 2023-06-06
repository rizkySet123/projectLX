import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("mongodb+srv://rizky:rizky123setiawan@cluster0.ed4ndng.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("dbsparta")

client = MongoClient('mongodb+srv://rizky:rizky123setiawan@cluster0.ed4ndng.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc ={
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fansmassages.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    messages_list = list(db.fansmassages.find({}, {'_id' : False}))
    return jsonify({'messages': messages_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)