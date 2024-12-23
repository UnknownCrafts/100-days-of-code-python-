# Typing speed test

import random
from tkinter import END, Canvas, Entry, Label, Tk

# ------------------------------ Initialize Variables ----------------------- #

word_list = []
sentence_list = []
textbox_list = []

timer = 60
max_typing_speed = 0
current_word = ""
word_count = 0

# ------------------------------ Initial Setup ----------------------- #

#Load the words from the text file
with open("words.txt") as file:
    for word in file:
        word_list.append(word.strip("\n"))

#Choose random words from the word_list
for i in range(20):
    sentence_list.append(random.choice(word_list))

# ------------------------------ Helper Functions ----------------------- #

def update_timer():
    global timer, word_count
    if timer > 0 and word_count <= 19:
        timer -= 1
        
        if timer == 1:
            timer_label.configure(text= f'Time: {timer} second')
        else:
            timer_label.configure(text= f'Time: {timer} seconds')
            
        window.after(1000, update_timer)
    else:
        update_max_speed()
    
def update_max_speed():
    global max_typing_speed, timer, textbox_list
    correct_word_count = 0
    time_remaining = 60 - timer
    
    textbox_list = textbox_list[:19]
    for i in range(len(textbox_list)):
        if sentence_list[i] == textbox_list[i]:
            correct_word_count += 1
            
    max_typing_speed = (correct_word_count/time_remaining)*100
    max_typing_speed_label.configure(text= f'Max Typing Speed: {max_typing_speed} WPM')

def update_current_word():
    global current_word, word_count
    if word_count <= 19:
        current_word = sentence_list[word_count]
        current_word_label.configure(text= f'Current Word: {current_word}')
        word_count += 1

def process(event=None):
    global timer
    if timer == 60:
        update_timer()
    textbox_list.append(textbox.get())
    textbox.delete(0, END)
    update_current_word()
    
# ------------------------------ UI ----------------------- #

window = Tk()
window.title("Typing Speed Test App")
window.config(padx=50, pady=50, height=500, width=700)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(width=500, height=700, highlightthickness=0)

timer_label = Label(window, text="Time: 60 seconds")
timer_label.grid(column=0, row=0)

max_typing_speed_label = Label(window, text="Max Typing Speed: 0 WPM")
max_typing_speed_label.grid(column=0, row=1)

current_word_label = Label(window, text="Current Word: N/A")
current_word_label.grid(column=0, row=2)
update_current_word()

textbox = Entry(window, width = 30)
textbox.grid(column=0, row=3, columnspan=1)
textbox.bind("<Return>", process)

window.mainloop()