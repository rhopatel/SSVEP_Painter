from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time

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
        invImg = ImageTk.PhotoImage(image.transpose(Image.Transpose.FLIP_LEFT_RIGHT))

        currentImage1 = img
        currentImage2 = img
        currentImage3 = img
        currentImage4 = img
        currentImage5 = img
        currentImage6 = img
        currentImage7 = img
        currentImage8 = img


        while True:
            self.time = (time.time() - self.init_time) * 1000

            #print(self.time, " ms")
            #print((self.time // 50 ) % 2)
            if ((self.time // 20) % 2 == 0):
                currentImage1 = invImg
            else:
                currentImage1 = img

            #if (self.time % 50 < eps):                
                #currentImage2 = invImg if not flipped1 else img
                #flipped2 = not flipped2

            if ((self.time // 25) % 2 == 0):              
                currentImage3 = invImg
            else:
                currentImage3 = img

            #if (self.time % 77 < eps):                
                #currentImage4 = invImg if not flipped1 else img
                #flipped4 = not flipped4

            if ((self.time // 33) % 2 == 0):              
                currentImage5 = invImg
            else:
                currentImage5 = img


            #if (self.time % 100 < eps):                
                #currentImage6 = invImg if not flipped1 else img
                #flipped6 = not flipped6

            if ((self.time // 100) % 2 == 0):               
                currentImage7 = invImg
            else:
                currentImage7 = img


            #if (self.time % 133 < eps):                
                #currentImage8 = invImg if not flipped1 else img
                #flipped8 = not flipped8


            margins = 200
            width = 1500
            #height = 1080

            icon1 = self.canvas.create_image(margins, 170,anchor=NW,image=currentImage1)
            #icon2 = self.canvas.create_image(margins, 320,anchor=NW,image=currentImage2)

            icon3= self.canvas.create_image(margins, 550,anchor=NW,image=currentImage3)
            #icon4= self.canvas.create_image(margins, 720,anchor=NW,image=currentImage4)

            icon5= self.canvas.create_image(width-margins, 170,anchor=NW,image=currentImage5)
            #icon6 =self.canvas.create_image(width-margins, 320,anchor=NW,image=currentImage6)

            icon7 = self.canvas.create_image(width-margins, 550,anchor=NW,image=currentImage7)
            #icon8 = self.canvas.create_image(width-margins, 720,anchor=NW,image=currentImage8)

            #icons= [icon1, icon2, icon3, icon4, icon5, icon6, icon7, icon8]
            icons= [icon1, icon3, icon5, icon7]


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