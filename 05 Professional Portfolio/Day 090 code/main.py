# Disappearing Text Writing App

from tkinter import END, Canvas, Label, Tk
from tkinter.scrolledtext import ScrolledText

# ------------------------------ Initialize Variables ----------------------- #
timer = 5
timer_update_process_list = []

# ------------------------------ Helper Functions ----------------------- #

def update_timer():
    global timer, textbox, timer_update_process_list
    if timer > 0:
        timer -= 1
        
        if timer == 1:
            timer_label.configure(text= f'Time Remaining: {timer} second')
        else:
            timer_label.configure(text= f'Time Remaining: {timer} seconds')
            
        timer_update_process_list.append(window.after(1000, update_timer))
    else:
        textbox.delete(1.0, END)

def process(event=None):
    global timer, timer_update_process_list
    timer = 5
    for id in timer_update_process_list:
        window.after_cancel(id)
    update_timer()
    
# ------------------------------ UI ----------------------- #

window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=50, pady=50, height=500, width=700)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(width=500, height=700, highlightthickness=0)

text_label = Label(window, text="The written text will be deleted after the timer has reached 0.")
text_label.grid(column=0, row=0)

text_label2 = Label(window, text="Keep writing to prevent deletion.")
text_label2.grid(column=0, row=1)

timer_label = Label(window, text=f"Time Remaining: {timer} seconds")
timer_label.grid(column=0, row=2)

textbox = ScrolledText(window, width = 100)
textbox.grid(column=0, row=3, columnspan=1)
textbox.bind_all("<Key>", process)

window.mainloop()