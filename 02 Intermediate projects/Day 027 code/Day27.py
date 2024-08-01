# Miles to Kilometer converter using tkinter

from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height= 100)
window.config(padx=20, pady=10)
window.eval('tk::PlaceWindow . center')

def mi_to_km():
    answer.config(text=float(input.get().strip())*1.609)

equal_to_label = Label(text="is equal to",)
equal_to_label.grid(column=0,row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

answer = Label(text="0")
answer.grid(column=1, row=1)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0, padx= 10)

button = Button(text="Calculate",command=mi_to_km)
button.grid(column=1, row=2)



window.mainloop()