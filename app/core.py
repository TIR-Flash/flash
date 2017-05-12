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

@core.route('/paid')
def paid():
    return render_template('home.html')

@core.route('/')
def home():
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
		    "description": "First, you'll need to install the dependencies. React is built on node.js so you will need the node package manager (npm) in order to install modules. ",
		    "content": '''apt install npm
npm init'''
		},
                {
                    "title": "Configure webpack",
                    "type": "code",
                    "description": "You will need a file called webpack.config.js that tells webpack which files to bundle and how.",
                    "content": '''var path = require('path');

module.exports = {
  entry: path.join(__dirname, 'app/static/js/hello.jsx'),
  output: {
    filename: 'bundle.js',
    path: path.join(__dirname, 'app/static/js')
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  }
};
'''
                },
                {
                    "title": "Configuring your app",
                    "type": "code",
                    "description": "You will also need a file called package.json that does a lot of things such as installing dependencies and buiding your app. You will also need a bundler that lets you package all your code together. We will use webpack but you can also use browserify. Finally, you will need a compiler such as Babel to make your ES6 (the latest standard of javascript) code compatible with older browsers.",
                    "content": '''{
  "name": "myappp",
  "version": "1.0.0",
  "description": "My first react app",
  "dependencies": {
    "webpack": "latest", 
    "webpack-dev-server": "latest", 
    "babel-cli": "latest", 
    "babel-core": "latest", 
    "babel-loader": "latest", 
    "babel-preset-env": "latest", 
    "babel-preset-es2015": "latest", 
    "babel-preset-react": "latest",
    "react": "latest", 
    "react-dom": "latest", 
  },
  "scripts": {
    "build": "node_modules/.bin/webpack --config webpack.config.js"
  },
  "babel": {
    "presets": ["env", "es2015", "react"]
  }
}
'''
                },
		{
		    "title": "Exercise 1: Hello World!",
		    "type": "code",
		    "description": "Create a file called hello.jsx where you will add the following code.",
		    "content": '''import React from 'react';
import ReactDOM from 'react-dom';

class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}

ReactDOM.render(<Welcome name="your-name-here"/>, document.getElementById('root'));'''
		},
                {
                    "title": "Run your app",
                    "type": "code",
                    "description": "Now all you need is an html file where you will use your react component. Create a file called index.html and add the following code and then you can just run 'npm install', 'npm run build'. Open your index.html file in a browser and your app should be running.",
                    "content": '''<!DOCTYPE html>
<html>
<head>
    <title>My first React.js app</title>
</head>
<body>
    <div id="root"></div>
    <script src="bundle.js"></script>
</body>
</html>'''
                }
	    ]
	}
    lid = mongo.db.lessons.insert_one(l).inserted_id
    return render_template('free.html')

@core.route('/lesson/<topic>')
def lesson(topic):
    l = mongo.db.lessons.find_one_or_404({"name":topic})
    return render_template('lesson.html', lesson=l)

@core.route('/create', methods=['GET','POST'])
def create():
    return render_template('create.html')
