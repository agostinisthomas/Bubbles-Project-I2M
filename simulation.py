import variables as vb
import liquid as liq
import numpy as np
import bubbles
# import bubbles

# Fichier contenant la classe SIMULATION

class Simulation:

    def __init__(self,model,n_sites):
        # Création d'une liste de sites de nucléation avec une distribution normale :
        self.sites=[]
        mu , sig = 0, 0.5
        for x in np.random.normal(mu,sig,n_sites) :
            self.sites.append(liq.Nucleation_site((x,vb.h)))
        self.bubbles=[]
        self.model=model


    def read_data(self,filename):

        # Pour le moment on va tout prendre dans le module variables
        self.x_0=0.
        self.t_0=vb.t_0
        self.dt=vb.dt
        self.C_0=vb.C_0
        self.y_0=vb.y_0
        self.R_0=vb.R_0
        self.h=vb.h
        self.C_atm=vb.C_atm
        self.D=vb.D
        self.rho_liq=vb.rho_liq
        self.mu_liq=vb.mu_liq
        self.Temp=vb.T
        self.P_atm=vb.P_atm
        self.R_gp=vb.R_gp
        self.g=vb.g
        self.t_f=vb.t_f
        self.ny=vb.ny
        self.rho_gaz=vb.rho_gaz


    def initialise(self,filename): # Initialise the simulation
        # Lecture de variables.py :
        self.read_data(filename)
        # Calculs preliminaires :
        self.C_i=self.C_0-self.C_atm
        self.C_b=self.P_atm/(self.R_gp*self.Temp)

        for s in self.sites :
            if s.create_or_not() :
                self.bubbles.append(bubbles.Bubble(self.R_0,s.position[1],s.position[0],s.id))

    def advance(self,t) :

        for s in self.sites :
            if s.create_or_not() :
                self.bubbles.append(bubbles.Bubble(self.R_0,s.position[1],s.position[0],s.id))

        for b in self.bubbles :
            b.rise_and_grow(self.model, t)
            if b.altitude<=0. :
                self.bubbles.remove(b)
