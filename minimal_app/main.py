from flask import Flask
from markupsafe import escape

app = Flask(__name__)


from flask import abort, redirect, url_for


@app.route("/")
def index():
    # return "<p>Hello World</p>"
    return redirect(url_for("sign_in"))


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
    print(url_for("index"))
    print(url_for("about"))
    print(url_for("sign_in", next="/"))
    print(url_for("projects"))


# https methods

from flask import request


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         return "do_the_login()"
#     else:
#         return "show_the_login_form()"


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
    # http://127.0.0.1:5000/hello?key=123&name=xxx
    searchword = request.args.get("name", "")
    print(f"url data---: {searchword}")
    return render_template("hello.html", name=name)


# Request object
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)


# file upload
from werkzeug.utils import secure_filename


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        print("Uploading file...")
        file = request.files["photo"]
        # file.save("/var/www/uploads/uploaded_file.jpg")  # change file name
        file.save(
            f"/var/www/uploads/{secure_filename(file.filename)}"
        )  # use user file name

        print("Uploaded file!")

    return render_template("upload.html")


# Redirect and errors
@app.route("/no_page_found")
def no_page_found():
    return page_not_found()


@app.errorhandler(404)
def page_not_found():
    # abort(404) #or
    return render_template("page_not_found.html"), 404
