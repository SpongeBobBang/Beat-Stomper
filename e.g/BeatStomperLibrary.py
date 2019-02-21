from random import*


def Get_Difficulty_Factor(Plank_Count):
    return round(1+(Plank_Count/50),2)
        
def Random_Sign_Factor():
    if randint(1,2) == 1:
        return 1.0
    else:
        return -1.0
       
def aa(self,x):
    x +=1
    print(x,"ee")

