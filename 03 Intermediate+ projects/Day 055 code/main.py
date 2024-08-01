# Just playing around with flask plus learned about decorators

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}<b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}<em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        text = function()
        return f"<u>{text}<u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()