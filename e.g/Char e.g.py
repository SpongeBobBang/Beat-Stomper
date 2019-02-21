from tkinter import*
import tkinter


class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=100, height=100)
        self.master.config()

        self.master.bind('<Key>', self.left_key)
        self.master.bind('<Right>', self.right_key)

        self.main_frame = tkinter.Frame()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()


        
        self.Scaling = 100
        self.Canvas_Width = 5.4
        self.Canvas_Height = 9.6
        
        self.draw = Canvas(self,width=(self.Canvas_Width * self.Scaling),height=(self.Canvas_Height * self.Scaling),bg="#030303")
        
        self.draw.pack(side=LEFT)

    #staticmethod
    def left_key(self,event):
        print (event, " key pressed")

    #staticmethod
    def right_key(self,event):
        print (event, " key pressed")

root = tkinter.Tk()
app = Application(root)
app.mainloop()
