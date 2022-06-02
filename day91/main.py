from tkinter import *
from tkinter import filedialog
import numpy as np
from PIL import Image
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

NUMBER_OF_COLORS = 15
TITLE_FONT = "Arial"
TITLE_COLOR = "#EFEFEF"
WORD_FONT = "Times New Roman"
WORD_COLOR = "#EEEEEE"
BACKGROUND_COLOR = "#222832"
BTN_BACKGROUND_COLOR = "#2F3847"


def get_img_colors():
    img_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select IMG",
        filetypes=(('Image Files', "*.jpg;*.jpeg;*.png"), ("All Files", "*.*"))
    )
    img = Image.open(img_file, 'r').convert('RGB')
    color_codes = palette(img)
    color_names = []
    for code in color_codes:
        if convert_rgb_to_names(code) not in color_names and len(color_names) < NUMBER_OF_COLORS:
            color_names.append(convert_rgb_to_names(code))
            colors_text.insert(END, convert_rgb_to_names(code) + '\n')


def palette(img):
    """
    Return palette in descending order of frequency
    """
    arr = np.asarray(img)
    palette, index = np.unique(asvoid(arr).ravel(), return_inverse=True)
    palette = palette.view(arr.dtype).reshape(-1, arr.shape[-1])
    count = np.bincount(index)
    order = np.argsort(count)
    return palette[order[::-1]]


def asvoid(arr):
    """View the array as dtype np.void (bytes)
    This collapses ND-arrays to 1D-arrays, so you can perform 1D operations on them.
    http://stackoverflow.com/a/16216866/190597 (Jaime)
    http://stackoverflow.com/a/16840350/190597 (Jaime)
    Warning:
    >>> asvoid([-0.]) == asvoid([0.])
    array([False], dtype=bool)
    """
    arr = np.ascontiguousarray(arr)
    return arr.view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[-1])))


def convert_rgb_to_names(rgb_tuple):
    # A dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index].title()


def copy_to_clipboard():
    root.clipboard_append(colors_text.get("1.0", END))


def clear_text():
    colors_text.delete("1.0", END)


root = Tk()
root.title('Image to Color List')
root.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
title_label = Label(text="Image to Color List", font=(TITLE_FONT, 32, "bold"), fg=TITLE_COLOR, bg=BACKGROUND_COLOR)
open_btn = Button(text="Select Image", font=(WORD_FONT, 20), width=25, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=get_img_colors)
copy_btn = Button(text="Copy Text", font=(WORD_FONT, 20), width=25, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=copy_to_clipboard)
clear_btn = Button(text="Clear Text", font=(WORD_FONT, 20), width=25, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                   command=clear_text)
colors_text = Text(root, width=35, height=16, font=(TITLE_FONT, 14))
title_label.grid(column=0, row=0, pady=20)
colors_text.grid(column=0, row=1)
open_btn.grid(column=0, row=2, pady=10)
copy_btn.grid(column=0, row=3)
clear_btn.grid(column=0, row=4, pady=10)
root.mainloop()
