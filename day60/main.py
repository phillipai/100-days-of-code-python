from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(".env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

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


@app.route('/post/<int:p_id>')
def get_post(p_id):
    return render_template('post.html', post=all_posts[int(p_id) - 1])


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = (data["name"])
        email = (data["email"])
        phone = (data["phone"])
        message = (data["message"])
        with smtplib.SMTP("smtp.outlook.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: New Message!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
