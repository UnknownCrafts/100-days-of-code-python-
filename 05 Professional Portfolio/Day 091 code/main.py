# PDF to AudioBook
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from pypdf import PdfReader
from pathlib import Path
import openai

'''
Initiate filepath and savepath variables, filepath is for the pdf file/folder that needs decoding,
meanwhile savepath is for the path where the decoded files are saved.
'''
filepath = ""
savepath = str(Path.home()) + "/Downloads/"

# Helper Functions
def getFile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[('Allowed Types', '*.pdf')])
    filepath_label.set(filepath)

def getDir():
    global savepath
    savepath = filedialog.askdirectory()
    savepath += "/"
    save_path_label.set(savepath)

def getText(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def saveAsAudio(text, file_name):
    global savepath
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(savepath + file_name)

def retrieveInput():
    global filepath
    if filepath != "":
        for file in filepath:
            file_text = getText(file)
            file_name = file.split("/")[-1]
            saveAsAudio(file_text, file_name)
    root.destroy()

# --GUI Code Starts Here--
root = Tk()
root.geometry('500x300')
root.title("PDF to Audiobook")
root.eval('tk::PlaceWindow . center')

save_path_label = StringVar()
save_path_label.set(savepath)

filepath_label = StringVar()
filepath_label.set(filepath)

  
label = Label(root,text="PDF to Audiobook")
label.pack()

btn = Button(root, text = 'Done', 
                command = retrieveInput)

btn.pack(side = 'bottom')   

open_file_button = Button(root, text="Open File(s) to convert", command=getFile)
open_file_button.pack()

current_chosen_file_or_folder_label = Label(root, textvariable= filepath_label)
current_chosen_file_or_folder_label.pack()

choose_button = Button(root, text="Choose the location to save the audiobook", command=getDir)
choose_button.pack()

current_save_location_label = Label(root, textvariable= save_path_label)
current_save_location_label.pack()

root.mainloop()
# --GUI Code Ends Here--