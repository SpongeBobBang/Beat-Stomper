#Beat Stomper
#S3 CS3 Stefan Yuzhao Heng, Kevin Jianxiang Gao

from tkinter import *
from random import* 

class Main(Frame):
    def Load_Canvas(self):
        self.__PlankCount = 0
        
        self.Scailing = 100
        self.Canvas_Width = 5.4
        self.Canvas_Height = 9.6
        
        self.draw = Canvas(self,width=(self.Canvas_Width * self.Scailing),height=(self.Canvas_Height * self.Scailing),bg="#030303")
        
        self.draw.pack(side=LEFT)

    def Load_Planks(self,*args):
        self.Plank_No=[]
        self.Plank_Loc_X=[]
        self.Plank_Loc_Y=[]
        self.Plank_Speed_X=[]
        self.Plank_Speed_Y=[]

        self.Plank_Width = 1.8
        self.Plank_Height = 0.5

        self.Fst_X= round(uniform(0.9,4.5)*self.Scailing,1)
        self.Fst_Y=8.0*self.Scailing
        self.Fst_Speed_X=0.15*self.Scailing
        self.Fst_Speed_Y=2
        
        self.Snd_X=round(uniform(0.9,4.5)*self.Scailing,1)
        self.Snd_Y=4.8*self.Scailing
        self.Snd_Speed_X=0.15*self.Scailing
        self.Snd_Speed_Y=2

        self.Trd_X=round(uniform(0.9,4.5)*self.Scailing,1)
        self.Trd_Y=1.6*self.Scailing
        self.Trd_Speed_X=0.15*self.Scailing
        self.Trd_Speed_Y=2
        
        self.Fst_Plank = self.Load_Plank(self.Fst_X/self.Scailing,8.0,1.8,0.5,"blue")
        self.Snd_Plank = self.Load_Plank(self.Snd_X/self.Scailing,4.8,1.8,0.5,"red")
        self.Trd_Plank = self.Load_Plank(self.Trd_X/self.Scailing,1.6,1.8,0.5,"yellow")       
        
        self.Plank_No.append(self.Fst_Plank)
        self.Plank_No.append(self.Snd_Plank)
        self.Plank_No.append(self.Trd_Plank)
        
        self.draw.pack(side=LEFT)

    def Load_Plank(self,X,Y,Width,Height,Color):
        return self.draw.create_rectangle((X-Width/2)*self.Scailing,(Y-Height/2)*self.Scailing,(X+Width/2)*self.Scailing,(Y+Height/2)*self.Scailing,fill=Color)
        
    def Update_Plank_Status(self,*args):
        self.Plank_Loc_X.append(self.Fst_X)
        self.Plank_Loc_Y.append(self.Fst_Y)
        self.Plank_Speed_X.append(self.Fst_Speed_X)
        self.Plank_Speed_Y.append(self.Fst_Speed_Y)

        self.Plank_Loc_X.append(self.Snd_X)
        self.Plank_Loc_Y.append(self.Snd_Y)
        self.Plank_Speed_X.append(self.Snd_Speed_X)
        self.Plank_Speed_Y.append(self.Snd_Speed_Y)

        self.Plank_Loc_X.append(self.Trd_X)
        self.Plank_Loc_Y.append(self.Trd_Y)
        self.Plank_Speed_X.append(self.Trd_Speed_X)
        self.Plank_Speed_Y.append(self.Trd_Speed_Y)

    def Update_Plank_Velocity(self,index,*args):
        if (self.Plank_Loc_X[index] > 450) or (self.Plank_Loc_X[index] < 90):
            self.Plank_Speed_X[index] = -1.0 * self.Plank_Speed_X[index]

    def Get_Plank_DeltaPerFrame_X(self,index,*args):
        if self.Plank_Loc_Y[index] < 960+25:
            DeltaPerFrame_X = self.Plank_Speed_X[index]
        else:
            DeltaPerFrame_X = randint(90,450)-self.Plank_Loc_X[index]
        self.Plank_Loc_X[index] = self.Plank_Loc_X[index] + DeltaPerFrame_X
        return DeltaPerFrame_X

    def Get_Plank_DeltaPerFrame_Y(self,index,*args):
        if self.Plank_Loc_Y[index] < 960+25:
            DeltaPerFrame_Y = (self.Plank_Speed_Y[index] )
        else:
            DeltaPerFrame_Y = -960-25
        self.Plank_Loc_Y[index] = self.Plank_Loc_Y[index] + DeltaPerFrame_Y
        return DeltaPerFrame_Y

    def Move_Plank1(self,*args):
        self.Update_Plank_Velocity(0)
        DeltaPerFrame_X=self.Get_Plank_DeltaPerFrame_X(0)
        DeltaPerFrame_Y=self.Get_Plank_DeltaPerFrame_Y(0)
        self.draw.move(self.Fst_Plank, DeltaPerFrame_X, DeltaPerFrame_Y)
        self.after(20,self.Move_Plank1)

    def Move_Plank2(self,*args):
        self.Update_Plank_Velocity(1)
        DeltaPerFrame_X=self.Get_Plank_DeltaPerFrame_X(1)
        DeltaPerFrame_Y=self.Get_Plank_DeltaPerFrame_Y(1)
        self.draw.move(self.Snd_Plank, DeltaPerFrame_X, DeltaPerFrame_Y)
        self.after(20,self.Move_Plank2)

    def Move_Plank3(self,*args):
        self.Update_Plank_Velocity(2)
        DeltaPerFrame_X=self.Get_Plank_DeltaPerFrame_X(2)
        DeltaPerFrame_Y=self.Get_Plank_DeltaPerFrame_Y(2)
        self.draw.move(self.Trd_Plank, DeltaPerFrame_X, DeltaPerFrame_Y)
        self.after(20,self.Move_Plank3)
            
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        
        self.Load_Canvas()
        self.Load_Planks()
        self.Update_Plank_Status()
        self.Get_Plank_DeltaPerFrame_X(0)
        self.Get_Plank_DeltaPerFrame_Y(0)
        self.Update_Plank_Velocity(0)
        self.Update_Plank_Velocity(1)
        self.Update_Plank_Velocity(2)
        self.after(20,self.Move_Plank1)
        self.after(20,self.Move_Plank2)
        self.after(20,self.Move_Plank3)

BeatStomper = Main()
BeatStomper.mainloop()
