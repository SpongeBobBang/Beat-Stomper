from BeatStomperLibrary import*
from tkinter import*

class Main(Frame):

    def Load_Canvas(self,*args):
        self.draw = Canvas(self,width=400,height=400,bg="#202020")
        self.draw.pack(side=LEFT)

    def ee(self):
        self.__x = 3
        
    def __init__(self,master=None):
        Frame.__init__(self, master)
        Pack.config(self)

        self.ee()
        self.later()

    def later(self):
        aa(self,self.__x)
        self.Load_Canvas()

        
e = Main()
e.mainloop()
