
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


class SSVEP_demo(object):
    def __init__(self, root, filename):
        frame = tk.Canvas(root, width=1920, height=1080)
        frame.place(anchor='center', relx=0.5, rely=0.5)
        frame.pack()

        # Place images
        margins = 200
        width = 1500
        height = 1080

        img = ImageTk.PhotoImage(Image.open(filename))

        frame.create_image(margins, 170,anchor=NW,image=img)
        frame.create_image(margins, 320,anchor=NW,image=img)

        frame.create_image(margins, 550,anchor=NW,image=img)
        frame.create_image(margins, 720,anchor=NW,image=img)

        frame.create_image(width-margins, 170,anchor=NW,image=img)
        frame.create_image(width-margins, 320,anchor=NW,image=img)

        frame.create_image(width-margins, 550,anchor=NW,image=img)
        frame.create_image(width-margins, 720,anchor=NW,image=img)

        root.mainloop()

        #self.update = self.draw().__next__
        #root.after(100, self.update)


def main():
    # Root setup
    root = Tk()
    root.title("SSVEP_demo")
    filename = "media/pencil-icon.png"
    root.geometry('1920x1080')
    app = SSVEP_demo(root, filename)

if __name__ == "__main__":
    main()