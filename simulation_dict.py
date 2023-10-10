import variables as vb
import bubbles
# Fichier contenant la classe SIMULATION 

class Simulation:
    
    def __init__(self):
        self.bubbles=[]
        self.sites=[] # Nucleation sites
        self.variables=dict()
        
    
    def read_data(self,filename): 
        
        # Pour le moment on va tout prendre dans le module variables
        self.variables["t_0"]=vb.t_0
        self.variables["dt"]=vb.dt
        self.variables[]
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
                    
        
    def initialise(self,filename,model): # Initialise the simulation
        
        # Attribution du model à utiliser : pour le moment ne change rien
        self.model=model
        
        # Lecture du module contenant tous les parametres necessaires a la simu
        self.read_data(filename)
        
        # Calculs preliminaires
        self.C_i=self.C_0-self.C_atm
        self.C_b=self.P_atm/(self.R_gp*self.Temp)

        
        
    def advance(self,bubble,r,t,y,c) : # Il faudra d'autres paramètres ici
        print("_____________ TIME STEP ____________")
        print("Avant : RADIUS =",bubble.radius," SPEED = ",bubble.speed," ALTITUDE = ",bubble.altitude)
        bubble.update_altitude(self)
        bubble.update_speed(self)
        bubble.grow(t, c, self)
        bubble.accelerate(t)

        print("Après : RADIUS =",bubble.radius," SPEED = ",bubble.speed," ALTITUDE = ",bubble.altitude)

        
        
        