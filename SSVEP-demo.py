
from tkinter import *
import tkinter
from PIL import ImageTk, Image

def main():
    root = Tk()

    root.title("SSVEP_demo")
    root.geometry('1920x1080')
    frame = Canvas(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    img = ImageTk.PhotoImage(Image.open("media/arrow.jpg"))
    frame.create_image(10,10,anchor=NW,image=img)

    root.mainloop()

if __name__ == "__main__":
    main()