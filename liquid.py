#   PACKAGES :

import variables as vb
import numpy as np
import random
import uuid

# Stand alone function so no need to create an object

def get_concentration(y,t,n) :
    conc=0.
    for i in range(n+1) :
        conc+=(4*vb.C_i/((2*i+1)*vb.pi)*np.exp(-((2*i+1)*vb.pi/(2*vb.y_0))**2*vb.D*t)*np.sin((2*i+1)*vb.pi*y/(2*vb.y_0)))
    return conc

#   Creating Bubble class

class Liquid :

    chosen_n = 2 # Number of modes to be used

    def __init__(self) :
        self.upcoming_concentration=[]

    def get_concentration(self,y,t,n) :
        conc=0.
        for i in range(n+1) :
            conc+=(4*vb.C_i/((2*i+1)*vb.pi)*np.exp(-((2*i+1)*vb.pi/(2*vb.y_0))**2*vb.D*t)*np.sin((2*i+1)*vb.pi*(vb.h-y)/(2*vb.y_0)))
        return conc

    def get_upcoming_concentration(self,y,t,n) : # NEEDS TO RETURN AN ARRAY : concentration ahead is only computed once
        for i in range(int(vb.ny)):                                                                 # for every bubble
            self.upcoming_concentration.append(self.get_concentration(y-i*vb.dy,t,n))
        return self.upcoming_concentration

class Nucleation_site() :

    def __init__(self,position=(0,vb.h),f=0.1) :
        self.position=position
        self.frequency=round(random.uniform(0.05,0.15), 3)
        self.timer=self.frequency
        self.id=uuid.uuid1()

    def create_or_not(self) :
        if self.timer >= self.frequency :
            self.timer=0.
            return True
        else :
            self.timer+=vb.dt
            return False
