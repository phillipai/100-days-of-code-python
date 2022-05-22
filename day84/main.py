from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

FONT_NAME = "Courier"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

root = Tk()
root.title('IMG_WATERMARK')
root.config(padx=25, pady=25)
img_file = ''


def watermark(img_input, img_output, text_watermark, xy_pos):
    image = Image.open(img_input)

    edit_image = ImageDraw.Draw(image)

    sky_blue = (135, 206, 235)
    font_watermark = ImageFont.truetype("arial.ttf", 200)
    edit_image.text(xy_pos, text_watermark, font=font_watermark, fill=sky_blue)
    image.show()
    image.save(img_output)


def select_file():
    global img_file
    img_file = askopenfilename()


def watermark_img():
    if img_file == '':
        messagebox.showerror("No image found", "Please select an image first.")
    else:
        img_output = f'watermarked.jpg'
        text_watermark = text_entry.get()
        watermark(img_file, img_output, text_watermark=text_watermark, xy_pos=(100, 100))
        messagebox.showinfo("Complete", "Successfully watermarked!")


title_label = Label(text="IMG Watermark", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=0, row=1, rowspan=4)

b1 = Button(root, text="1. Select IMG", font=20, width=15,
            command=select_file)
b2 = Button(root, text="3. Watermark IMG", font=20, width=15,
            command=watermark_img)
b1.grid(column=1, row=1, columnspan=2, padx=25, pady=25)
b2.grid(column=1, row=4, columnspan=2, padx=25, pady=25)

text_label = Label(text="2. Watermark Text", font=20)
text_label.grid(column=1, row=2, padx=25, pady=25)
text_entry = Entry(width=26)
text_entry.grid(column=1, row=3)

root.mainloop()
