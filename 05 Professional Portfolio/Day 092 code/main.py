# Image Colour Palette Generator

import base64
import numpy as np
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' # Change this for production
Bootstrap5(app)

class UploadImageForm(FlaskForm):
    file = FileField("You've found the right place! Upload an image to check it out.", validators=[FileRequired(), FileAllowed(['jpg', "jpeg", "png"], 'Images only!')])
    submit = SubmitField('Submit')

# All Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    form = UploadImageForm()
    image_data = None
    if form.validate_on_submit():
        file = form.file.data
        
        # type(form.file.data) is werkzeug.FileStorage class which has read() function that outputs file data in bytes
        image_bytes = file.read()
        encoded_string = base64.b64encode(image_bytes).decode()
        
        N = 10 # top N colors in the image
        img = np.array(Image.open(file))
        unqc,C = np.unique(img.reshape(-1,img.shape[-1]), axis=0, return_counts=True)
        topNidx = np.argpartition(C,-N)[-N:]
        
        hexcodes = []
        # Convert RGB values to hex and append to the hexcodes array
        for color in unqc[topNidx]:
            hexcode = "#" + "".join([hex(color[0]).replace("0x",""), hex(color[1]).replace("0x",""), hex(color[2]).replace("0x","")])
            if len(hexcode) < 7:
                hexcode += "0"
            hexcodes.append(hexcode)
        
        image_data = {
            "image_bytes": encoded_string,
            "colors": hexcodes
        }
        
        return render_template("index.html", image_data=image_data, form=form)
    return render_template("index.html", image_data=image_data, form=form)


if __name__ == '__main__':
    app.run()
