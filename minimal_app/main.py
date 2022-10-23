from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


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


# if __name__ == "__main__":
#     app.run(debug=True)
