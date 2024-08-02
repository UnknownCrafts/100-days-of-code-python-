import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)
response = requests.get("https://gist.githubusercontent.com/UnknownCrafts/a51be8fc423ad795f36bafe93c1897eb/raw/fc15463f44eeacd5f623617ac2c8a7d0e77ae58f/blogdata.json").json()

@app.route("/")
def home():
    return render_template("index.html", posts=response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<index>")
def show_post(index):
    selected_post = None
    for posts in response:
        if int(posts["id"]) == int(index):
            selected_post = posts
            break
    return render_template("post.html", post=selected_post)

if __name__ == "__main__":
    app.run()