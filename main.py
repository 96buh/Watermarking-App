from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw

FONT_NAME = "Courier"

global panel
global filename
global img
global edit_img
panel = None

PREVIEW_WIDTH = 640
PREVIEW_HEIGHT = 480


def select_file():
    global filename
    filename = fd.askopenfilename()
    return filename


def open_img():
    global panel
    global filename
    global img
    filename = select_file()
    if panel is not None:
        panel.destroy()
    img = Image.open(filename)

    if img.width > PREVIEW_WIDTH or img.height > PREVIEW_HEIGHT:
        ratio = min(PREVIEW_WIDTH / img.width, PREVIEW_HEIGHT / img.height)
        new_width = int(img.width * ratio)
        new_height = int(img.height * ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)

    img = ImageTk.PhotoImage(img)

    panel = Label(window, image=img)
    panel.grid(row=1, column=5, rowspan=5, padx=10)


def preview():
    global filename
    global img
    text = watermark_text.get("1.0", "end-1c")
    text_size = int(watermark_text_size.get("1.0", "end-1c"))
    color = watermark_text_color.get("1.0", "end-1c")

    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    # custom font
    font = ImageFont.truetype("sans-serif.ttf", text_size)

    draw.text((0, 0), text, color, font=font)
    if img.width > PREVIEW_WIDTH or img.height > PREVIEW_HEIGHT:
        ratio = min(PREVIEW_WIDTH / img.width, PREVIEW_HEIGHT / img.height)
        new_width = int(img.width * ratio)
        new_height = int(img.height * ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.grid(row=1, column=5, rowspan=5, padx=10)


def save():
    global filename
    text = watermark_text.get("1.0", "end-1c")
    text_size = int(watermark_text_size.get("1.0", "end-1c"))
    color = watermark_text_color.get("1.0", "end-1c")

    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    # custom font
    font = ImageFont.truetype("sans-serif.ttf", text_size)
    draw.text((0, 0), text, color, font=font)
    file_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    img.save(file_path)


window = Tk()

window.title("Watermarking App")
window.config(padx=50, pady=50)

# watermark text area
Label(text="Text", font=("Arial", 15)).grid(row=1, column=0, padx=10)
watermark_text = Text(height=1, width=18, font=("Arial", 15))
watermark_text.grid(row=1, column=1, pady=5)

# edit text size
Label(text="Size", font=("Arial", 15)).grid(row=2, column=0, padx=10)
watermark_text_size = Text(height=1, width=18, font=("Arial", 15))
watermark_text_size.grid(row=2, column=1, pady=5)

# edit text color
Label(text="Color", font=("Arial", 15)).grid(row=3, column=0, padx=10)
watermark_text_color = Text(height=1, width=18, font=("Arial", 15))
watermark_text_color.grid(row=3, column=1, pady=5)

# select image button
select_image = Button(text="Select Image", font=("Arial", 10), command=open_img)
select_image.grid(row=4, column=0, pady=10)

# preview button
pewview_button = Button(text="Preview", font=("Arial", 10), width=25, command=preview)
pewview_button.grid(row=4, column=1, pady=10)

# save button
save_button = Button(text="Save", width=10, font=("Arial", 10), command=save)
save_button.grid(row=5, column=0, pady=10)

# canvas
canvas = Canvas(window, width=PREVIEW_WIDTH, height=PREVIEW_HEIGHT, bg='gray')
canvas.grid(row=1, column=5, padx=10, rowspan=5)

window.mainloop()
