from flask import render_template, request, redirect, url_for, session, Blueprint, flash, jsonify

core = Blueprint('core', __name__)

@core.route('/')
def home():
	return render_template('home.html')

@core.route('/lesson/<id>')
def lesson(id):
	return render_template('sample_tutorial.html')