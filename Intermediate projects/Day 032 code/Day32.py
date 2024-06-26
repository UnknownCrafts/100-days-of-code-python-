#Flash card app using tkinter

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CSV IMPORT ------------------------------- #
data = pandas.read_csv("./data/french_words.csv")
dictionary_data = data.to_dict(orient="records")

# ---------------------------- HELPER FUNCTIONS ------------------------------- #

def next_card():
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random.choice(dictionary_data)["French"])
def wrong():
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random.choice(dictionary_data)["French"])
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.minsize(width=800, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.eval('tk::PlaceWindow . center')


card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

incorrect_button = Button(image=incorrect_image, highlightthickness=0, borderwidth=0, command=wrong)
incorrect_button.grid(column=0, row=1)

correct_button = Button(image=correct_image, highlightthickness=0, borderwidth=0, command=next_card)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()