#Flash card app using tkinter

from tkinter import *
import pandas
import random

# ---------------------------- CSV IMPORT ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    dictionary_data = data.to_dict(orient="records")


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = random.choice(dictionary_data)
flip_timer = ""

# ---------------------------- HELPER FUNCTIONS ------------------------------- #

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary_data)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(background_image, image=card_front_image)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(background_image, image=card_back_image)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    
def is_known():
    global data, dictionary_data
    
    try:
        dictionary_data.remove(current_card)
    except:
        data = pandas.read_csv("./data/french_words.csv")
        dictionary_data = data.to_dict(orient="records")
        
    data = pandas.DataFrame(dictionary_data)
    data.to_csv("./data/words_to_learn.csv", index=False)
    
    next_card()
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.minsize(width=800, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.eval('tk::PlaceWindow . center')

flip_timer = window.after(3000, flip_card)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_image = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

incorrect_button = Button(image=incorrect_image, highlightthickness=0, borderwidth=0, command=next_card)
incorrect_button.grid(column=0, row=1)

correct_button = Button(image=correct_image, highlightthickness=0, borderwidth=0, command=is_known)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()