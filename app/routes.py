from flask import Blueprint, render_template, request, redirect, session, url_for
from .models import User, Blog
from . import db, bcrypt

main = Blueprint("main", __name__)

@main.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("main.login"))

    blogs = Blog.query.all()  # Fetch all blogs from DB
    return render_template("home.html", blogs=blogs)


@main.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if password != confirm:
            error = "Passwords do not match!"
            return render_template("register.html", error=error)

        if User.query.filter_by(email=email).first():
            error = "Email already registered!"
            return render_template("register.html", error=error)

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(name=name, email=email, password=hashed)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("main.login"))

    return render_template("register.html", error=error)


@main.route("/", methods=["GET", "POST"])
@main.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("main.home"))
        else:
            error = "Invalid email or password!"

    return render_template("login.html", error=error)


@main.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("main.login"))


@main.route("/add-blogs", methods=["GET"])
def blogs():
    return render_template("add-blogs.html")


@main.route("/add_blog", methods=["POST"])
def add_blog():
    title = request.form.get("title")
    content = request.form.get("content")

    if title and content:
        new_blog = Blog(title=title, content=content)
        db.session.add(new_blog)
        db.session.commit()

    return redirect(url_for("main.home"))
