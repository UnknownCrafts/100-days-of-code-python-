# A watermarking app

from tkinter import Checkbutton, IntVar, Tk, Canvas, Button
from tkinter import filedialog as fd
from PIL import Image, ImageDraw

# ------------------------------ Global Variables ----------------- #

save_file_checkbutton_out = 0
show_output_image_checkbutton_out = 0

# ------------------------------ Helper Functions ----------------- #

def getImages():
    image_paths = fd.askopenfiles(
        title="Choose an image(s)",
        filetypes=[
            ('image files', ('.png', '.jpg')),
        ])
    
    if len(image_paths) != 0:
        count = 0
        increment = 60
        starting_posx = 10
        starting_posy = 10
        for path in image_paths:
            
            file_name = f'copyrighted{count}.png'
            file_path = path.name.split("/")
            file_path.pop()
            file_path.pop(0)
            file_path = "/" + "/".join(file_path) + "/" + file_name
            
            im = Image.open(path.name)
            
            txt = Image.new("RGBA", im.size, (255, 255, 255, 128))
            
            d = ImageDraw.Draw(txt)

            # draw text, half opacity
            for i in range(im.size[1]//10):
                for j in range(im.size[0]//10):
                    d.text((starting_posx, starting_posy), text = "Copyright", fill=(0, 0, 0, 255), align="center")
                    starting_posx += increment
                starting_posx = 10
                starting_posy += increment

            out = Image.alpha_composite(im, txt)

            if (show_output_image_checkbutton_out.get()):
                out.show()
                
            if (save_file_checkbutton_out.get()):
                out.save(file_path)
                
            count += 1


# ------------------------------ UI ----------------------- #

window = Tk()
window.title("Watermarking app")
window.config(padx=50, pady=50)
window.eval('tk::PlaceWindow . center')

save_file_checkbutton_out = IntVar()
show_output_image_checkbutton_out = IntVar()

canvas = Canvas(width=200, height=200, highlightthickness=0)

choose_images_button = Button(text="Choose image(s)", width=11, command=getImages)
choose_images_button.grid(column=0, row=0, padx=12)

save_file_checkbutton = Checkbutton(window, text = "Save Output", 
                    variable = save_file_checkbutton_out, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10)
save_file_checkbutton.grid(column=0, row=1, padx=12)

show_output_image_checkbutton = Checkbutton(window, text = "Show Output", 
                    variable = show_output_image_checkbutton_out, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10)
show_output_image_checkbutton.grid(column=1, row=1, padx=12)

window.mainloop()