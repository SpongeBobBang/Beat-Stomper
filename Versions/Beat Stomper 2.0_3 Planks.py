#Beat Stomper
#S3 CS3 Stefan Yuzhao Heng, Kevin Jianxiang Gao

from tkinter import *
from random import* 

class Main(Frame):
    def Initialize(self):
        self.__PlankCount = 0
        
        self.scaling = 100
        self.canvas_width = 5.4
        self.canvas_height = 9.6
        self.draw = Canvas(self,width=(self.canvas_width * self.scaling),height=(self.canvas_height * self.scaling),bg="#030303")

        self.Plank1 = self.draw.create_rectangle(1.8*self.scaling,7.75*self.scaling,3.6*self.scaling,8.25*self.scaling,fill='#e755f0')

        self.Plank_No=[]
        self.Plank_Loc_X=[0,0,0]
        self.Plank_Loc_Y=[0,0,0]
        self.Plank_Speed_X=self.Get_Difficulty(self.__PlankCount)
        self.Plank_Speed_Y=[0,0,0]

        self.first_rec = self.draw.create_rectangle(1.8*self.scaling,7.75*self.scaling,3.6*self.scaling,8.25*self.scaling,fill='blue')
        self.second_rec = self.draw.create_rectangle(1.8*self.scaling,4.55*self.scaling,3.6*self.scaling,5.05*self.scaling,fill='red')
        self.third_rec = self.draw.create_rectangle(1.8*self.scaling,1.35*self.scaling,3.6*self.scaling,1.85*self.scaling,fill='yellow')        
        
        self.Plank_No.append(self.first_rec)
        self.Plank_No.append(self.second_rec)
        self.Plank_No.append(self.third_rec)

        self.first_x=2.7
        self.first_y=1.6
        self.first_vx=0.1
        self.first_vy=0.05
        
        self.second_x=2.7
        self.second_y=4.8
        self.second_vx=0.1
        self.second_vy=0.05

        self.third_x=2.7
        self.third_y=8.0
        self.third_vx=0.1
        self.third_vy=0.05
        
        self.draw.pack(side=LEFT)

    def Move_Plank1(self,*args):
        
        self.draw.move(self.Plank1,self.Plank_Speed_X,0)
        self.after(10,self.Move_Plank1)

    def Get_Plank_Dire_X(self,*args):
        temp = randint(0,1)
        if temp % 2 == 0:
            return 1
        else:
            return -1

    def Get_Difficulty(self,*args):
        return round(1+self.__PlankCount/100,1)

    def Update_Plank_Status():
        eee
        
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.Initialize()
        self.after(10,self.Move_Plank1)
        
        
BeatStomper = Main()

BeatStomper.mainloop()
