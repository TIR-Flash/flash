from flask import render_template, request, redirect, url_for, session, Blueprint, flash, jsonify
from db import mongo
from datetime import datetime

core = Blueprint('core', __name__)

@core.route('/test_select')
def test_select():
    l = mongo.db.lessons.find_one({"name":"React.js"})
    return render_template('lesson.html', lesson=l)

@core.route('/test_insert')
def test_insert():
    l = {"test_key":"test_value", "timestamp": datetime.now()}
    lid = mongo.db.lessons.insert_one(l).inserted_id
    return str(lid)

@core.route('/test_create')
def test_create():
    l = {
	"name": "React.js",
	"components": [
		{
		    "title": "What is React?",
		    "type": "image",
		    "description": "React is a javascript framework for creating user interfaces.",
		    "src": "https://facebook.github.io/react/img/logo.svg"
		},
		{
		    "title": "Introduction",
		    "type": "video",
		    "description": "Watch this video:",
		    "link": "https://www.youtube.com/watch?v=A71aqufiNtQ"
		},
		{
		    "title": "Getting Started",
		    "type": "code",
		    "description": "First, you'll need to install the dependencies.",
		    "content": '''apt install npm
npm init
npm install --save react react-dom'''
		},
		{
		    "title": "Exercise 1: Hello World!",
		    "type": "code",
		    "description": "Try this out",
		    "content": '''import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  &lt;h1&gt;Hello, world!&lt;/h1&gt;,
  document.getElementById('root')
);'''
		}
	    ]
	}
    lid = mongo.db.lessons.insert_one(l).inserted_id
    return jsonify(str(l))

@core.route('/')
def home():
    return render_template('home.html')

@core.route('/lesson/<id>')
def lesson(id):
    return render_template('sample_tutorial.html')

@core.route('/create', methods=['GET','POST'])
def create():
    return render_template('create.html')
