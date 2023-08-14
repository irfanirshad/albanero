from flask import Blueprint, render_template, redirect

bp_app1 = Blueprint("helloworld", __name__, "templates")

@bp_app1.route("/")
def index():
    return "Hello World!"

@bp_app1.route("/hello")
def hello():
    return "Hello World Again!"

@bp_app1.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}!"

@bp_app1.route("/hellohtml")
def hello_html():
    return render_template("hello.html")