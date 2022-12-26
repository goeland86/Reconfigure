import tkinter as tk
from tkinter import ttk, Scrollbar, RIGHT, Y
from PIL import Image, ImageTk
from recore_pin_maps import RecoreA5PinMaps, RecoreA6PinMaps, RecoreA7PinMaps

# Create the main window
root = tk.Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the label that will display the selected image
image_label = tk.Label()

# Create a label for the combobox
label = ttk.Label(root, text="Please choose your board revision:")

# Create a frame to hold the comboboxes
combobox_frame = ttk.Frame(root)

# Create a combobox for selecting the image to display
combobox = ttk.Combobox(root, values=["A7", "A6", "A5"])

# Load the images and rotate them 90 degrees to the right
a7_image = Image.open("images/Recore-pinout_A7.png")
a7_image = ImageTk.PhotoImage(a7_image)

a6_image = Image.open("images/Recore-pinout_A6.png")
a6_image = ImageTk.PhotoImage(a6_image)

a5_image = Image.open("images/Recore-pinout_A5.png")
a5_image = ImageTk.PhotoImage(a5_image)

recore_pin_maps = None
pin_maps = []

# Define a function that will be called when a value is selected in the combobox
def on_combobox_select(event=None):
    # Get the selected value from the combobox
    value = combobox.get()

    if value == "A7":
        # Update the image displayed by the label to the A7 image
        image_label.configure(image=a7_image)
        # Show the A7 comboboxes
        # combobox_frame.pack(side="right", fill="both", expand=True)
        recore_pin_maps = RecoreA7PinMaps()

    elif value == "A6":
        # Update the image displayed by the label to the A6 image
        image_label.configure(image=a6_image)
        recore_pin_maps = RecoreA6PinMaps()

    if value == "A5":
        # Update the image displayed by the label to the A5 image
        image_label.configure(image=a5_image)
        recore_pin_maps = RecoreA5PinMaps()


# Bind the combobox to the on_combobox_select function
combobox.bind("<<ComboboxSelected>>", on_combobox_select)

# Place the combobox and the image label in the window
combobox.pack()
image_label.pack()

# Start the main event loop
root.mainloop()
