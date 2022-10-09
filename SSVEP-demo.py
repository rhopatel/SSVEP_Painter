
from tkinter import *
import tkinter
from PIL import ImageTk, Image

def main():
    # Root setup
    root = Tk()
    root.title("SSVEP_demo")
    root.geometry('1920x1080')

    # Create canvas
    frame = Canvas(root, width=1920, height=1080)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Place images
    margins = 400
    width = 1920
    height = 1080

    img = ImageTk.PhotoImage(Image.open("media/pencil-icon.png"))
    frame.create_image(margins, 170,anchor=NW,image=img)
    frame.create_image(margins, 320,anchor=NW,image=img)

    frame.create_image(margins, 550,anchor=NW,image=img)
    frame.create_image(margins, 720,anchor=NW,image=img)


    frame.create_image(width-margins, 170,anchor=NW,image=img)
    frame.create_image(width-margins, 320,anchor=NW,image=img)

    frame.create_image(width-margins, 550,anchor=NW,image=img)
    frame.create_image(width-margins, 720,anchor=NW,image=img)

    root.mainloop()

if __name__ == "__main__":
    main()