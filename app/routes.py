from flask import render_template, request, redirect, Blueprint 
main = Blueprint("main", __name__)


@main.route('/')
def login():
    return render_template("login.html")

@main.route('/login', methods=["POST"])
def home():
    return render_template("home.html")