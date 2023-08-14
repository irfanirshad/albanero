from flask import Blueprint, render_template, redirect, url_for

bp_app2 = Blueprint("calculator", __name__)

@bp_app2.route('/')
def index():
    return 'This is the calculator blueprint'

@bp_app2.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)


@bp_app2.route('/go_to_hello')
def add(num1, num2):
    return redirect(url_for("helloworld.hello_html"))


'''
You could add a divide function or a subtraction function
And so on.....

Now lets see how to resolve conflicting url routes ...

head over to main.py
'''