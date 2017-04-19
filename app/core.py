from flask import render_template, request, redirect, url_for, session, Blueprint, flash, jsonify
from db import mongo
from datetime import datetime

core = Blueprint('core', __name__)

@core.route('/test_select')
def test_select():
    l = mongo.db.lessons.find_one({"test_key":"test_value"})
    return str(l)

@core.route('/test_insert')
def test_insert():
    l = {"test_key":"test_value", "timestamp": datetime.now()}
    lid = mongo.db.lessons.insert_one(l).inserted_id
    return str(lid)

@core.route('/')
def home():
    return render_template('home.html')

@core.route('/lesson/<id>')
def lesson(id):
    return render_template('sample_tutorial.html')
