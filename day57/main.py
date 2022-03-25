from flask import Flask, render_template
import requests


BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/blog")
def get_blog():
    response = requests.get(BLOG_URL)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def find_post(post_id):
    response = requests.get(BLOG_URL)
    all_posts = response.json()
    if post_id == 1:
        return render_template("post.html", posts=all_posts)
    if post_id == 2:
        return render_template("post2.html", posts=all_posts)
    if post_id == 3:
        return render_template("post3.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
