
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time

class SSVEP_demo(object):


    def __init__(self, root):
        self.root = root
        canvas = tk.Canvas(root, width=1920, height=1080)
        self.canvas = canvas

        self.canvas.place(anchor='center', relx=0.5, rely=0.5)
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.paint)
        #image = Image.open(filename)
        #img = ImageTk.PhotoImage(image)
        self.update = self.render().__next__
        root.after(1, self.update)
        self.init_time = time.time()


    def paint(self,event):
        color = "black"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def render(self):

        #load images
        pencil = Image.open("media/pencil-icon.png")
        eraser = Image.open("media/eraser-icon.png")

        top_left_arrow = Image.open("media/TopLeft.png")
        bottom_right_arrow = Image.open("media/BotRight.png")

        pencil_image = ImageTk.PhotoImage(pencil)
        inv_pencil_image = ImageTk.PhotoImage(pencil.transpose(Image.Transpose.FLIP_LEFT_RIGHT))

        eraser_image = ImageTk.PhotoImage(eraser)
        inv_eraser_image = ImageTk.PhotoImage(eraser.transpose(Image.Transpose.FLIP_LEFT_RIGHT))

        top_left_arrow_image = ImageTk.PhotoImage(top_left_arrow)
        inv_top_left_arrow_image = ImageTk.PhotoImage(top_left_arrow.transpose(Image.Transpose.FLIP_LEFT_RIGHT))

        bottom_right_arrow_image = ImageTk.PhotoImage(bottom_right_arrow)
        inv_bottom_right_arrow_image = ImageTk.PhotoImage(bottom_right_arrow.transpose(Image.Transpose.FLIP_LEFT_RIGHT))


        dyn_pencil = pencil_image
        dyn_eraser = eraser_image
        dyn_width_increaser = top_left_arrow_image
        dyn_width_decreaser = bottom_right_arrow_image
        dyn_color_increaser = top_left_arrow_image
        dyn_color_decreaser = bottom_right_arrow_image
        #currentImage7 = img
        #currentImage8 = img

        FREQ_1 = 15
        FREQ_2 = 20
        FREQ_3 = 5
        FREQ_4 = 25
        FREQ_5 = 10
        FREQ_6 = 30

        coeff_1 = (1000 / FREQ_1) / 2
        coeff_2 = (1000 / FREQ_2) / 2
        coeff_3 = (1000 / FREQ_3) / 2  
        coeff_4 = (1000 / FREQ_4) / 2
        coeff_5 = (1000 / FREQ_5) / 2
        coeff_6 = (1000 / FREQ_6) / 2  
        
    
        while True:
            self.time = (time.time() - self.init_time) * 1000
            
            #print(self.time, " ms")
            #print((self.time // 50 ) % 2)
            if ((self.time // coeff_1) % 2 == 0):
                dyn_pencil = inv_pencil_image
            else:
                dyn_pencil = pencil_image
            
            if ((self.time // coeff_2) % 2 == 0):              
                dyn_eraser = inv_eraser_image
            else:
                dyn_eraser = eraser_image

          
            if ((self.time // coeff_3) % 2 == 0):              
                dyn_width_increaser = inv_top_left_arrow_image
            else:
                dyn_width_increaser = top_left_arrow_image

            
            if ((self.time // coeff_4) % 2 == 0):               
                dyn_width_decreaser = inv_bottom_right_arrow_image
            else:
                dyn_width_decreaser = bottom_right_arrow_image

          
            if ((self.time // coeff_5) % 2 == 0):              
                dyn_color_increaser = inv_top_left_arrow_image
            else:
                dyn_color_increaser = top_left_arrow_image

            
            if ((self.time // coeff_6) % 2 == 0):               
                dyn_color_decreaser = inv_bottom_right_arrow_image
            else:
                dyn_color_decreaser = bottom_right_arrow_image


            margins = 150
            width = 1500
            #height = 1080

            drawn_pencil = self.canvas.create_image(margins, 170,anchor=NW,image=dyn_pencil)
            drawn_eraser = self.canvas.create_image(width-margins, 170,anchor=NW,image=dyn_eraser)

            drawn_width_increaser= self.canvas.create_image(margins, 620,anchor=NW,image=dyn_width_increaser)
            drawn_width_decreaser= self.canvas.create_image(margins, 750,anchor=NW,image=dyn_width_decreaser)

            drawn_color_increaser = self.canvas.create_image(width-margins, 620,anchor=NW,image=dyn_color_increaser)
            drawn_color_decreaser =self.canvas.create_image(width-margins, 750,anchor=NW,image=dyn_color_decreaser)

            #icon7 = self.canvas.create_image(width-margins, 550,anchor=NW,image=dyn_width_increaser)
            #icon8 = self.canvas.create_image(width-margins, 720,anchor=NW,image=currentImage8)

            #icons= [icon1, icon2, icon3, icon4, icon5, icon6, icon7, icon8]
            icons= [drawn_pencil, drawn_eraser, drawn_width_increaser, drawn_width_decreaser, drawn_color_increaser, drawn_color_decreaser]
            #icons = [drawn_pencil]

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
    root.geometry('1920x1080')
    app = SSVEP_demo(root)
    root.mainloop()


if __name__ == "__main__":
    main()