# A dynamic content blog style website

import requests
from post import Post
from flask import Flask, render_template


app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = [Post(x) for x in response.json()]

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<content_id>')
def posted(content_id):
    selected_post = None
    for post in all_posts:
        if str(post.get_id()) == str(content_id):
            selected_post = post
            break
    return render_template("post.html", post_=selected_post)

if __name__ == "__main__":
    app.run()
