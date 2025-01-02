# Image Colour Palette Generator

import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SubmitField

BASE_MAPS_URL = "https://www.google.com/maps/search/?api=1&query="
BREWERY_FILTER = ["planning", "closed", "large", "bar"]


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' # Change this for production
Bootstrap5(app)

class Submit(FlaskForm):
    submit = SubmitField('Show Me!')

# All Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    form = Submit()
    chosen_brewery = None
    
    if form.validate_on_submit():
        response = requests.get("https://api.openbrewerydb.org/v1/breweries/random").json()
        
        while response[0]["brewery_type"] in BREWERY_FILTER:
            response = requests.get("https://api.openbrewerydb.org/v1/breweries/random").json()
        
        chosen_brewery = response[0]
        query = f"{chosen_brewery["street"]} {chosen_brewery["city"]} {chosen_brewery["country"]}".replace(" ", "%20")
        chosen_brewery["maps_link"] = BASE_MAPS_URL + query
        
        return render_template("index.html", brewery=chosen_brewery, form=form)
    return render_template("index.html",brewery=chosen_brewery, form=form)


if __name__ == '__main__':
    app.run(debug=True)
