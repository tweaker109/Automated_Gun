from tkinter import *
import os

# Create the main window
root = Tk()
root.title("Gun Controls")
root.iconbitmap(default="gun.ico")
root.config(bg="#2D2D2D")
root.minsize(width=687, height=500)
root.resizable(0, 0)

# Define iOS-like colors
ios_green = "#4CD964"
ios_yellow = "#FFCC00"
ios_blue = "#007AFF"

# Define a function to create round buttons
def create_round_button(parent, text, bg_color, x, y):
    button = Button(parent, text=text, bg=bg_color, fg="white", height=3, width=15, font=("Helvetica", 15, "bold"), borderwidth=0, command=lambda: os.system("python " + text + ".py"))
    button.place(x=x, y=y)

# Create and place rounded buttons
create_round_button(root, "Auto", ios_green, 30, 45)
create_round_button(root, "Home", ios_yellow, 250, 45)
create_round_button(root, "Fire", ios_blue, 465, 45)

# Create and place round arrow buttons
arrow_radius = 20

# Up arrow
up_arrow = Button(root, text="👆", bg="#CC6666", fg="white", height=2, width=5, font=("Helvetica", 20, "bold"), borderwidth=0)
up_arrow.place(x=318 - arrow_radius, y=215 - arrow_radius)

# Left arrow
left_arrow = Button(root, text="👈", bg="#CC6666", fg="white", height=2, width=5, font=("Helvetica", 20, "bold"), borderwidth=0)
left_arrow.place(x=218 - arrow_radius, y=308 - arrow_radius)

# Down arrow
down_arrow = Button(root, text="👇", bg="#CC6666", fg="white", height=2, width=5, font=("Helvetica", 20, "bold"), borderwidth=0)
down_arrow.place(x=318 - arrow_radius, y=403 - arrow_radius)

# Right arrow
right_arrow = Button(root, text="👉", bg="#CC6666", fg="white", height=2, width=5, font=("Helvetica", 20, "bold"), borderwidth=0)
right_arrow.place(x=418 - arrow_radius, y=308 - arrow_radius)

# Start the main event loop
root.mainloop()
