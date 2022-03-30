from flask import Flask, render_template
import requests


blog_url = "https://api.npoint.io/2b1e1701b179fe512483"
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/index.html')
def index():
    return render_template("index.html", posts=all_posts)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:p_id>')
def get_post(p_id):
    return render_template('post.html', post=all_posts[int(p_id) - 1])


if __name__ == "__main__":
    app.run(debug=True)