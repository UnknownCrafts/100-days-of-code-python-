from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, URL
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' # Change this for production
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    map_url: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    has_sockets: Mapped[int] = mapped_column(Integer, nullable=False)
    has_toilet: Mapped[int] = mapped_column(Integer, nullable=False)
    has_wifi: Mapped[int] = mapped_column(Integer, nullable=False)
    can_take_calls: Mapped[int] = mapped_column(Integer, nullable=False)
    seats: Mapped[str] = mapped_column(String, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String, nullable=False)

class AddCafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('An Image of the Cafe (URL)', validators=[DataRequired(), URL()])
    location = StringField('The General Area (e.g London Bridge)', validators=[DataRequired()])
    has_sockets = SelectField('Power Socket Availability', choices=[("✘"),("✅")])
    has_toilet = SelectField('Restroom Availability', choices=[("✘"),("✅")])
    has_wifi = SelectField('Wifi Availability', choices=[("✘"),("✅")])
    can_take_calls = SelectField('Order Over Phone Service', choices=[("✘"),("✅")])
    seats = SelectField('Seats Available', choices=[("0-10"),("10-20"),("20-30"),("30-40"),("40-50"),("50+")])
    coffee_price = StringField('Price of The Coffee', validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = form.name.data,
            map_url = form.map_url.data,
            img_url = form.img_url.data,
            location = form.location.data,
            seats = form.seats.data,
            has_sockets = int(form.has_sockets.data == "✅"),
            has_toilet = int(form.has_toilet.data == "✅"),
            has_wifi = int(form.has_wifi.data == "✅"),
            can_take_calls = int(form.can_take_calls.data == "✅"),
            coffee_price = form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafes"))
        
    return render_template('add.html', form=form)

@app.route('/delete')
def delete_cafe():
    cafe_id = request.args.get("id")
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("cafes"))


@app.route('/cafes')
def cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    db.session.commit()
    return render_template('cafes.html', cafes=all_cafes)


if __name__ == '__main__':
    app.run(debug=True)
