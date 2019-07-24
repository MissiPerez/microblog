# MicroBlog 

This project is to demonstrate the setup of Flask.

## Getting Started

Introduction to Flask - using the Flask Mega Tutorial series, a course designed by Miguel Grinberg.  Each chapter of this series will help to achieve "Hello, World".

### To complete this first assignment, do the following:

Read the material for part 1 (Links to an external site.)Links to an external site..

Create your own `microblog` repository in your github

Ensure you have a working version of `pipenv (Links to an external site.)Links to an external site.` installed.  If you are not comfortable using pipenv, you can use virtualenv (as in the tutorial) instead.

Clone your `microblog` repo to your own local machine, and create a python 3 virtual environment at the top level of your microblog folder, by using pipenv rather than using `python3 -m venv` or virtualenv.

Install the Flask library into your virtual environment.

Also, install the flake8 linter with `pipenv install flake8`.

Write the "Hello World" code as described in the tutorial.  Make sure you follow the directory structure as laid out in the tutorial.

Add a debug launch configuration for Flask to your project.  It should look like this within your launch.json file:

`"configurations": [
 {
 "name": "Python: Flask",
 "type": "python",
 "request": "launch",
 "module": "flask",
 "env": {
 "FLASK_APP": "microblog.py",
 "FLASK_ENV": "development",
 "FLASK_DEBUG": "0"
 },
 "args": [
 "run",
 "--no-debugger",
 "--no-reload"
 ],
 "jinja": true
 }
]`

#### Before running:
* FLASK_APP environment variable:

`(venv) $ export FLASK_APP=microblog.py`

##### Are you ready to be blown away? You can run your first web application, with the following command:

`(venv) $ flask run`


