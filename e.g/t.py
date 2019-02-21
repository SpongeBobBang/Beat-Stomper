from tkinter import*

class Main(Frame):
    def t(self):
        root=Tk()
        root.title("Black Jack")
        cv=Canvas(root,width=500,height=720)
        cv.pack()

    def __init__(self,master=None):
        Frame.__init__(self,master)
        Pack.config(self)
        self.t()

a=Main()
a.mainloop()
