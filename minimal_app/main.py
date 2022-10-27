from fileinput import filename
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/sign_in")
def sign_in():
    return "Sign In"


@app.route("/admin")
def admin():
    return "Hello Admin"


# varialble rules
@app.route("/users/<username>")
def show_user_profile(username):
    # show user profile
    return f"User Id: {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post: {post_id}"


# Unique URLs / Redirection Behavior


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about")
def about():
    return "The about page"


# using url_for
from flask import url_for

with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("about"))
    print(url_for("sign_in", next="/"))
    print(url_for("projects"))


# https methods

from flask import request


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "do_the_login()"
    else:
        return "show_the_login_form()"


# or


@app.get("/login")
def login_get():
    return "show_the_login_form()"


@app.post("/login")
def login_post():
    return "do_the_login()"


# Static files
# url_for("static", filename="style.css") use in templates


# Rendering templates
from flask import render_template


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)
