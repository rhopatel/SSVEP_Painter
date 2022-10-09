
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
    img = ImageTk.PhotoImage(Image.open("media/arrow.jpg"))
    frame.create_image(0,0,anchor=NW,image=img)

    root.mainloop()

if __name__ == "__main__":
    main()