#Beat Stomper
#S3 CS3 Stefan Yuzhao Heng, Kevin Jianxiang Gao

from tkinter import *
from random import* 

class Main(Frame):
    def Load_Canvas(self,*args):
        self.__PlankCount = 0

        self.__Fst_Press = False
        self.__Snd_Able = False
        self.__Snd_Press = False
        self.__Control = True
        self.On_Air = True
        
        self.Jump_Speed = -40
        
        self.Scaling = 100
        self.Canvas_Width = 5.4
        self.Canvas_Height = 9.6
        
        self.draw = Canvas(self,width=(self.Canvas_Width * self.Scaling),height=(self.Canvas_Height * self.Scaling),bg="#030303")

        self.Frame_Rate = 20
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

        self.Fst_X = round(uniform(self.Plank_Width,self.Canvas_Width-self.Plank_Width),2)
        self.Fst_Y = 8.0
        self.Fst_Speed_X = 0.1
        self.Fst_Speed_Y = 0.02
        
        self.Snd_X = round(uniform(self.Plank_Width,self.Canvas_Width-self.Plank_Width),2)
        self.Snd_Y = 4.8
        self.Snd_Speed_X = 0.1
        self.Snd_Speed_Y = 0.02

        self.Trd_X = round(uniform(self.Plank_Width,self.Canvas_Width-self.Plank_Width),2)
        self.Trd_Y = 1.6
        self.Trd_Speed_X = 0.1
        self.Trd_Speed_Y = 0.02
        
        self.Fst_Plank = self.Load_Plank(self.Fst_X,self.Fst_Y,self.Plank_Width,self.Plank_Height,"blue")
        self.Snd_Plank = self.Load_Plank(self.Snd_X,self.Snd_Y,self.Plank_Width,self.Plank_Height,"red")
        self.Trd_Plank = self.Load_Plank(self.Trd_X,self.Trd_Y,self.Plank_Width,self.Plank_Height,"yellow")       
        
        self.Plank_No.append(self.Fst_Plank)
        self.Plank_No.append(self.Snd_Plank)
        self.Plank_No.append(self.Trd_Plank)
        
        self.draw.pack(side=LEFT)

    def Load_Block(self,*args):
        self.Block_X = (self.Plank_Loc_X[0])/self.Scaling-0.1
        self.Block_Y = (self.Plank_Loc_Y[0])/self.Scaling-0.55

        self.Block = self.Load_Plank(self.Block_X,self.Block_Y,0.6,0.6,"White")

        self.draw.pack(side=LEFT)
        self.Block_X = (self.Plank_Loc_X[0])/self.Scaling
        self.Block_Y = (self.Plank_Loc_Y[0])/self.Scaling
        
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
        
        self.Plank_Y_Array = self.Plank_Loc_Y

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
            DeltaPerFrame_Y = (self.Plank_Speed_Y[index])
        else:
            DeltaPerFrame_Y = -960-25
        self.Plank_Loc_Y[index] = self.Plank_Loc_Y[index] + DeltaPerFrame_Y
        return DeltaPerFrame_Y

    def Move_Block(self,*args):
        '''
        self.Lowest_Plank_No = self.Get_Lowest_Plank()
        '''
        if self.__Fst_Press == False:
            self.draw.move(self.Block,0,self.Plank_Loc_Y[0]-(self.Block_Y)*self.Scaling)

            self.Delta = self.Plank_Loc_X[0]-(self.Block_X)*self.Scaling
            self.Block_X += self.Delta/self.Scaling
            
            self.Block_Y = round((self.Plank_Loc_Y[0])/self.Scaling,2)
        else: 
                
            if self.Start_Direction_Generated == False:
                if self.Plank_Loc_X[0]-(self.Block_X)*self.Scaling > 0:
                    self.Delta = 20
                else:
                    self.Delta = -20
                self.Start_Direction_Generated = True
                    
            self.Block_X += self.Delta/self.Scaling
            
            if self.Block_X > 5.1 or self.Block_X < 0.3:
                self.Delta = -1.2 * self.Delta

                
            if self.__Snd_Able == False and self.__Control == True:
                if self.__Snd_Press == True and self.Jump_Speed < 0 :
                    self.Jump_Speed = 0
                    self.__Control = False 
                    self.Jump_Speed += 30
                self.Delta = 0
                    
            self.Jump_Speed += 2
            self.draw.move(self.Block,0,self.Jump_Speed)

            self.Block_Y += round(self.Jump_Speed/self.Scaling,2)
            
        self.draw.move(self.Block,self.Delta,0)
        
        self.after(self.Frame_Time,self.Move_Block)

    def Check_Landed(self,*args):
        if self.On_Air == True:
            if self.Jump_Speed > 0:
                for Index in range(len(self.Plank_Loc_Y)):
                    if self.Block_Y*self.Scaling < self.Plank_Loc_Y[Index]-25+20 and self.Block_Y*self.Scaling > self.Plank_Loc_Y[Index]-25-20:
                        if self.Block_X*self.Scaling > self.Plank_Loc_X[Index] - 90 and self.Block_X*self.Scaling < self.Plank_Loc_X[Index] + 90:
                            print("e")
                            self.On_Air = False
                            self.__First_Press = False
            

        self.after(self.Frame_Time,self.Check_Landed)

    def Get_Lowest_Plank(self,*arges):
        for i in range(len(self.Plank_No)):
            if self.Plank_Loc_Y[i] == max(self.Plank_Loc_Y[0],self.Plank_Loc_Y[1],self.Plank_Loc_Y[2]):
                return i
                break

    def Update_Plank_Array(self,*args):
        self.temp = self.Plank_Y_Array[0]
        self.Plank_Y_Array[0] = self.Plank_Y_Array[1]
        self.Plank_Y_Array[1] = self.Plank_Y_Array[2]
        self.Plank_Y_Array[2] = self.temp

    def Check(self):
        self.master.bind("<Key>",self.Move_Chcek)
        self.master.bind("<Button-1>",self.Move_Chcek)

    def Move_Chcek(self,event):
        if event.char != 'p' and event.char != 'r':
            if self.__Fst_Press == False:
                On_Air = True
                self.__Fst_Press = True
                self.__Snd_Able = True
                self.__Snd_Press = False
                self.Start_Direction_Generated = False
            elif self.__Fst_Press == True:
                On_air = True
                self.__Snd_Able = False
                self.__Snd_Press = True
            else: 
                self.__Snd_Able = False
        else:
            ee


    def Adjust(self,*args):
        for i in range(len(self.Plank_Loc_Y)):
            for j in range(len(self.Plank_Loc_X)):
                if self.Block_Y== round(self.Plank_Loc_Y[i]/self.Scaling,2)-0.55:
                    if self.Block_X> round(self.Plank_Loc_X[j]/self.Scaling,2)-0.9 and self.Block_X<round(self.Plank_Loc_X[j]/self.Scaling,2)+0.9:
                        self.Jump_Speed=0
                        self.Block_X = round(self.Plank_Loc_X[j]/self.Scaling,2)
                        self.Block_Y = 5.4
        print(self.Block_Y, round(self.Plank_Loc_Y[i]/self.Scaling,2)-0.55)

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

        
        self.after(self.Frame_Time,self.Check_Landed)

        self.after(self.Frame_Time,self.Move_Block)
        
        
        self.Check()
        
        

BeatStomper = Main()
BeatStomper.mainloop()
