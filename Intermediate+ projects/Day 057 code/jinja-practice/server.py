# First time using jinja

import random
import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(1,10)
    copyright = f"Copyright {datetime.now().year}. Built by Surya Vasudev"
    return render_template("index.html", num=random_number, footer=copyright)

@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("guess.html", name=name.title(), age=age, gender=gender)

@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run()