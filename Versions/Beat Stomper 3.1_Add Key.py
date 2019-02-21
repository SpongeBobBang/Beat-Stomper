#Beat Stomper
#S3 CS3 Stefan Yuzhao Heng, Kevin Jianxiang Gao

from tkinter import *
from random import* 

class Main(Frame):
    def Load_Canvas(self,*args):
        self.__PlankCount = 0
        self.__On_Air = False
        
        self.Scaling = 100
        self.Canvas_Width = 5.4
        self.Canvas_Height = 9.6
        
        self.draw = Canvas(self,width=(self.Canvas_Width * self.Scaling),height=(self.Canvas_Height * self.Scaling),bg="#030303")

        self.Frame_Rate = 23
        self.Frame_Time = int(round(1000/self.Frame_Rate))
        
        self.draw.pack(side=LEFT)

    def Load_Planks(self,*args):
        self.Plank_No = []
        self.Plank_Loc_X = []
        self.Plank_Loc_Y = []
        self.Plank_Speed_X = []
        self.Plank_Speed_Y = []

        self.Plank_Width = 1.8
        self.Plank_Height = 0.5

        self.Fst_X = round(uniform(self.Plank_Width,self.Canvas_Width-self.Plank_Width),3)
        self.Fst_Y = 8.0
        self.Fst_Speed_X = 0.15
        self.Fst_Speed_Y = 0.03
        
        self.Snd_X = round(uniform(self.Plank_Width,self.Canvas_Width-self.Plank_Width),3)
        self.Snd_Y = 4.8
        self.Snd_Speed_X = 0.15
        self.Snd_Speed_Y = 0.03

        self.Trd_X = round(uniform(self.Plank_Width,self.Canvas_Width-self.Plank_Width),3)
        self.Trd_Y = 1.6
        self.Trd_Speed_X = 0.15
        self.Trd_Speed_Y = 0.03
        
        self.Fst_Plank = self.Load_Plank(self.Fst_X,self.Fst_Y,self.Plank_Width,self.Plank_Height,"blue")
        self.Snd_Plank = self.Load_Plank(self.Snd_X,self.Snd_Y,self.Plank_Width,self.Plank_Height,"red")
        self.Trd_Plank = self.Load_Plank(self.Trd_X,self.Trd_Y,self.Plank_Width,self.Plank_Height,"yellow")       
        
        self.Plank_No.append(self.Fst_Plank)
        self.Plank_No.append(self.Snd_Plank)
        self.Plank_No.append(self.Trd_Plank)
        
        self.draw.pack(side=LEFT)

    def Load_Block(self,*args):
        self.Block_X = (self.Plank_Loc_X[1])/self.Scaling
        self.Block_Y = (self.Plank_Loc_Y[1])/self.Scaling

        self.Block = self.Load_Plank(self.Block_X,self.Block_Y,0.6,0.6,"White")

        self.draw.pack(side=LEFT)
        
    def Load_Plank(self,X,Y,Width,Height,Color):
        return self.draw.create_rectangle((X-Width/2)*self.Scaling,(Y-Height/2)*self.Scaling,(X+Width/2)*self.Scaling,(Y+Height/2)*self.Scaling,fill=Color)
        
    def Update_Plank_Status(self,*args):
        self.Plank_Loc_X.append(self.Fst_X*self.Scaling)
        self.Plank_Loc_Y.append(self.Fst_Y*self.Scaling)
        self.Plank_Speed_X.append(self.Fst_Speed_X*self.Scaling)
        self.Plank_Speed_Y.append(self.Fst_Speed_Y*self.Scaling)

        self.Plank_Loc_X.append(self.Snd_X*self.Scaling)
        self.Plank_Loc_Y.append(self.Snd_Y*self.Scaling)
        self.Plank_Speed_X.append(self.Snd_Speed_X*self.Scaling)
        self.Plank_Speed_Y.append(self.Snd_Speed_Y*self.Scaling)

        self.Plank_Loc_X.append(self.Trd_X*self.Scaling)
        self.Plank_Loc_Y.append(self.Trd_Y*self.Scaling)
        self.Plank_Speed_X.append(self.Trd_Speed_X*self.Scaling)
        self.Plank_Speed_Y.append(self.Trd_Speed_Y*self.Scaling)

    def Update_Plank_Velocity(self,index,*args):
        if (self.Plank_Loc_X[index] > (self.Canvas_Width-self.Plank_Width/2)*self.Scaling) or (self.Plank_Loc_X[index] < self.Scaling*self.Plank_Width/2):
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

    def Move_Block(self,*args):
        self.draw.move(self.Block,self.Plank_Loc_X[0]-self.Block_X*self.Scaling,self.Plank_Loc_Y[0]-(self.Block_Y+0.55)*self.Scaling)
        self.Block_X = (self.Plank_Loc_X[0])/self.Scaling
        self.Block_Y = (self.Plank_Loc_Y[0])/self.Scaling-0.55
        self.after(self.Frame_Time,self.Move_Block)

    def Check(self):
        self.master.bind("<Key>",self.KeyboardChcek)

    def KeyboardChcek(self,event):
        if event.char != 'p' and event.char != 'r':
            self.__On_Air = True
        else:
            self.__On_Air = False
        print(event.char,self.__On_Air)

    def Move_Plank1(self,*args):
        self.Update_Plank_Velocity(0)
        self.draw.move(self.Fst_Plank,self.Get_Plank_DeltaPerFrame_X(0),self.Get_Plank_DeltaPerFrame_Y(0))
        self.after(self.Frame_Time,self.Move_Plank1)

    def Move_Plank2(self,*args):
        self.Update_Plank_Velocity(1)
        self.draw.move(self.Snd_Plank,self.Get_Plank_DeltaPerFrame_X(1),self.Get_Plank_DeltaPerFrame_Y(1))
        self.after(self.Frame_Time,self.Move_Plank2)

    def Move_Plank3(self,*args):
        self.Update_Plank_Velocity(2)
        self.draw.move(self.Trd_Plank,self.Get_Plank_DeltaPerFrame_X(2),self.Get_Plank_DeltaPerFrame_Y(2))
        self.after(self.Frame_Time,self.Move_Plank3)
            
    def __init__(self,*args,master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        
        self.Load_Canvas()
        self.Load_Planks()
        self.Update_Plank_Status()
        self.Load_Block()
        
        self.Get_Plank_DeltaPerFrame_X(0)
        self.Get_Plank_DeltaPerFrame_Y(0)
        self.Update_Plank_Velocity(0)
        self.Update_Plank_Velocity(1)
        self.Update_Plank_Velocity(2)
        
        self.after(self.Frame_Time,self.Move_Plank1)
        self.after(self.Frame_Time,self.Move_Plank2)
        self.after(self.Frame_Time,self.Move_Plank3)

        self.after(self.Frame_Time,self.Move_Block)
        self.Check()

BeatStomper = Main()
BeatStomper.mainloop()
