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

        self.Plank_No=[]
        self.Plank_Loc_X=[]
        self.Plank_Loc_Y=[]
        self.Plank_Speed_X=[]
        self.Plank_Speed_Y=[]

        self.first_rec = self.draw.create_rectangle(1.8*self.scaling,7.75*self.scaling,3.6*self.scaling,8.25*self.scaling,fill='blue')
        self.second_rec = self.draw.create_rectangle(1.8*self.scaling,4.55*self.scaling,3.6*self.scaling,5.05*self.scaling,fill='red')
        self.third_rec = self.draw.create_rectangle(1.8*self.scaling,1.35*self.scaling,3.6*self.scaling,1.85*self.scaling,fill='yellow')        
        
        self.Plank_No.append(self.first_rec)
        self.Plank_No.append(self.second_rec)
        self.Plank_No.append(self.third_rec)

        self.first_x=2.7*self.scaling
        self.first_y=8.0*self.scaling
        self.first_vx=0.15*self.scaling
        self.first_vy=5
        
        self.second_x=2.7*self.scaling
        self.second_y=4.8*self.scaling
        self.second_vx=0.15*self.scaling
        self.second_vy=2

        self.third_x=2.7*self.scaling
        self.third_y=1.6*self.scaling
        self.third_vx=0.15*self.scaling
        self.third_vy=2
        
        self.draw.pack(side=LEFT)


    def Update_Plank_Status(self,*args):
        self.Plank_Loc_X.append(self.first_x)
        self.Plank_Loc_Y.append(self.first_y)
        self.Plank_Speed_X.append(self.first_vx)
        self.Plank_Speed_Y.append(self.first_vy)

        self.Plank_Loc_X.append(self.second_x)
        self.Plank_Loc_Y.append(self.second_y)
        self.Plank_Speed_X.append(self.second_vx)
        self.Plank_Speed_Y.append(self.second_vy)

        self.Plank_Loc_X.append(self.third_x)
        self.Plank_Loc_Y.append(self.third_y)
        self.Plank_Speed_X.append(self.third_vx)
        self.Plank_Speed_Y.append(self.third_vy)

    def Update_Plank_Velocity(self,index,*args):
        if (self.Plank_Loc_X[index] > 450) or (self.Plank_Loc_X[index] < 90):
            self.Plank_Speed_X[index] = -1.0 * self.Plank_Speed_X[index]

    def Get_Plank_Deltax(self,index,*args):
        if self.Plank_Loc_Y[index] < 960+25:
            deltax = self.Plank_Speed_X[index]
        else:
            deltax = randint(90,450)-self.Plank_Loc_X[index]
        self.Plank_Loc_X[index] = self.Plank_Loc_X[index] + deltax
        return deltax

    def Get_Plank_Deltay(self,index,*args):
        if self.Plank_Loc_Y[index] < 960+25:
            deltay = (self.Plank_Speed_Y[index] )
        else:
            deltay = -960-25
        self.Plank_Loc_Y[index] = self.Plank_Loc_Y[index] + deltay
        return deltay

    def movePlank1(self,*args):
        self.Update_Plank_Velocity(0)
        deltax=self.Get_Plank_Deltax(0)
        deltay=self.Get_Plank_Deltay(0)
        '''
        if deltay == -960-25:
        
            self.temp = randint(90,450)
            
            self.draw.move(self.first_rec,self.temp-self.Plank_Loc_X[0], deltay)
            self.Plank_Loc_X[0] = self.temp
            
            labelTest=Label(self,fg="white",text=self.Plank_Loc_X[0],anchor="c",bg="black",font=("Marker Felt",10,"bold"))
            labelTest.place(height=40,width=100,x=50,y=500)
            

            
            self.Plank_Loc_X = 150
            self.Update_Plank_Velocity(0)
            deltax=self.Get_Plank_Deltax(0)
            self.draw.move(self.first_rec, deltax, deltay)
            
        else:
        '''
        self.draw.move(self.first_rec, deltax, deltay)
        
        labelTest=Label(self,fg="white",text=self.Plank_Loc_X[0],anchor="c",bg="black",font=("Marker Felt",10,"bold"))
        labelTest.place(height=40,width=100,x=50,y=100)
        
        self.after(20,self.movePlank1)

    def movePlank2(self,*args):
        self.Update_Plank_Velocity(1)
        deltax=self.Get_Plank_Deltax(1)
        deltay=self.Get_Plank_Deltay(1)
        self.draw.move(self.second_rec, deltax, deltay)
        '''
        labelTest=Label(self,fg="white",text=self.Plank_Loc_X[1],anchor="c",bg="black",font=("Marker Felt",10,"bold"))
        labelTest.place(height=40,width=100,x=250,y=100)
        '''
        self.after(20,self.movePlank2)

    def movePlank3(self,*args):
        self.Update_Plank_Velocity(2)
        deltax=self.Get_Plank_Deltax(2)
        deltay=self.Get_Plank_Deltay(2)
        self.draw.move(self.third_rec, deltax, deltay)
        '''
        labelTest=Label(self,fg="white",activebackground="#bbbbbb",text=deltay,anchor="c",bg="#b0b0b0",font=("Marker Felt",10,"bold"))
        labelTest.place(height=40,width=100,x=450,y=100)
        '''
        self.after(20,self.movePlank3)
            
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        
        self.Initialize()
        self.Update_Plank_Status()
        self.Update_Plank_Velocity(0)
        self.Update_Plank_Velocity(1)
        self.Update_Plank_Velocity(2)
        self.Get_Plank_Deltax(0)
        self.Get_Plank_Deltay(0)
        self.after(20,self.movePlank1)
        '''
        self.after(20,self.movePlank2)
        self.after(20,self.movePlank3)
        '''

BeatStomper = Main()
BeatStomper.mainloop()
