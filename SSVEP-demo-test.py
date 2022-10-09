
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time
import math

class SSVEP_demo(object):
    def __init__(self, root, filename):
        self.root = root
        canvas = tk.Canvas(root, width=1920, height=1080)
        self.canvas = canvas
        self.filename = filename

        self.canvas.place(anchor='center', relx=0.5, rely=0.5)
        self.canvas.pack()

        #image = Image.open(filename)
        #img = ImageTk.PhotoImage(image)
        self.update = self.draw().__next__
        root.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        

        while True:
            self.time = time.time()

            #print(self.time)
            if math.ceil(self.time) % 2 == 0:
                img = ImageTk.PhotoImage(image.transpose(Image.FLIP_LEFT_RIGHT))
            else:
                img = ImageTk.PhotoImage(image)


            #icon1 = self.canvas.create_image(
            #    250, 250, image=tkimage)
            # Place images
            margins = 200
            width = 1500
            height = 1080

            icon1 = self.canvas.create_image(margins, 170,anchor=NW,image=img)
            icon2 = self.canvas.create_image(margins, 320,anchor=NW,image=img)

            icon3= self.canvas.create_image(margins, 550,anchor=NW,image=img)
            icon4= self.canvas.create_image(margins, 720,anchor=NW,image=img)

            icon5= self.canvas.create_image(width-margins, 170,anchor=NW,image=img)
            icon6 =self.canvas.create_image(width-margins, 320,anchor=NW,image=img)

            icon7 = self.canvas.create_image(width-margins, 550,anchor=NW,image=img)
            icon8 = self.canvas.create_image(width-margins, 720,anchor=NW,image=img)

            icons= [icon1, icon2, icon3, icon4, icon5, icon6, icon7, icon8]
            self.root.after_idle(self.update)

            yield

            for icon in icons:
                self.canvas.delete(icon)
        #time += 1
        #angle %= 360


def main():
    # Root setup
    root = Tk()
    root.title("SSVEP_demo")
    filename = "media/pencil-icon.png"
    root.geometry('1920x1080')
    app = SSVEP_demo(root, filename)
    root.mainloop()


if __name__ == "__main__":
    main()