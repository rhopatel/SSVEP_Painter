
from tkinter import *
import tkinter

def main():
    print("hello")
    # create root window
    root = Tk()

    # root window title and dimension
    root.title("SSVEP_demo")
    # Set geometry (widthxheight)
    root.geometry('350x200')
    
    # all widgets will be here
    # Execute Tkinter
    root.mainloop()

def appStarted(app):
    app.width = 350
    app.height = 200

    #circle with line through it
def drawCirlceWithLinePair(x0,y0,x1,y1):
    pass
    #root.create_oval(x0,y0,x1,y1, fill = "black", outline = "white")

    #root.create_oval(x0,y0,x1,y1, fill = "black", outline = "white")
    #root.create_oval(x0,y1, 2 * x1 ,y1, fill = "black", outline = "white")
    

if __name__ == "__main__":
    main()