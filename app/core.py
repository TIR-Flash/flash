from flask import render_template, request, redirect, url_for, session, Blueprint, flash, jsonify

core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template('base.html')