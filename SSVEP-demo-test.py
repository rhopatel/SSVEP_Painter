
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
        self.init_time = time.time()

    def draw(self):
        image = Image.open(self.filename)

        img = ImageTk.PhotoImage(image)
        invImg = ImageTk.PhotoImage(image.transpose(Image.FLIP_LEFT_RIGHT))

        currentImage1 = img
        currentImage2 = img
        currentImage3 = img
        currentImage4 = img
        currentImage5 = img
        currentImage6 = img
        currentImage7 = img
        currentImage8 = img

        flipped1 = False
        flipped2 = False
        flipped3 = False
        flipped4 = False
        flipped5 = False
        flipped6 = False
        flipped7 = False
        flipped8 = False
    
        while True:
            self.time = (time.time() - self.init_time) * 1000
            eps = 2

            if (self.time % 20 < eps):                
                currentImage1 = invImg if not flipped1 else img
                flipped1 = not flipped1

            if (self.time % 50 < eps):                
                currentImage2 = invImg if not flipped1 else img
                flipped2 = not flipped2
            
            if (self.time % 77 < eps):                
                currentImage3 = invImg if not flipped1 else img
                flipped3 = not flipped3

            if (self.time % 100 < eps):                
                currentImage4 = invImg if not flipped1 else img
                flipped4 = not flipped4

            if (self.time % 133 < eps):                
                currentImage5 = invImg if not flipped1 else img
                flipped5 = not flipped5
            
            if (self.time % 150 < eps):                
                currentImage6 = invImg if not flipped1 else img
                flipped6 = not flipped6
            
            if (self.time % 250 < eps):                
                currentImage7 = invImg if not flipped1 else img
                flipped7 = not flipped7
            
            if (self.time % 500 < eps):                
                currentImage8 = invImg if not flipped1 else img
                flipped8 = not flipped8

            #icon1 = self.canvas.create_image(
            #    250, 250, image=tkimage)
            # Place images
            margins = 200
            width = 1500
            height = 1080

            icon1 = self.canvas.create_image(margins, 170,anchor=NW,image=currentImage1)
            icon2 = self.canvas.create_image(margins, 320,anchor=NW,image=currentImage2)

            icon3= self.canvas.create_image(margins, 550,anchor=NW,image=currentImage3)
            icon4= self.canvas.create_image(margins, 720,anchor=NW,image=currentImage4)

            icon5= self.canvas.create_image(width-margins, 170,anchor=NW,image=currentImage5)
            icon6 =self.canvas.create_image(width-margins, 320,anchor=NW,image=currentImage6)

            icon7 = self.canvas.create_image(width-margins, 550,anchor=NW,image=currentImage7)
            icon8 = self.canvas.create_image(width-margins, 720,anchor=NW,image=currentImage8)

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
    filename = "media/resized.png"
    root.geometry('1920x1080')
    app = SSVEP_demo(root, filename)
    root.mainloop()


if __name__ == "__main__":
    main()