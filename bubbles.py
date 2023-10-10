#   PACKAGES :

import variables as vb
import numpy as np
import liquid as liq
import sys
import uuid

#____________ Creating Bubble class ___________

class Bubble :

    def __init__(self,R_0,y_0,x_0,site_id=None) :
        self.abscissa=x_0
        self.radius = R_0
        self.altitude = y_0
        self.speed = 0.000005
        self.acceleration = 0.
        self.next_concentration=[]
        self.printing_counter=0
        self.Reynolds=vb.rho_liq*2*self.speed*self.radius/vb.mu_liq
        self.id = uuid.uuid1()
        self.site_id=site_id


        # self.speed_variables_output=open('../OUTPUTS/speed_variables.txt','w')


# __________ GET FUNCTIONS ____________

    def get_radius(self) :
        return self.radius

    def get_altitude(self) :
        return self.altitude

    def get_speed(self) :
        return self.speed

    def get_acceleration(self) :
        return self.acceleration

    def get_Reynolds(self) :
        return self.Reynolds

    def get_abscissa(self) :
        return self.abscissa

    def get_id(self) :
        return self.id


#____________ UPDATE FUNCTIONS _________

#   RADIUS

    def grow(self,t,c) :
        alpha = -vb.R_gp*vb.T*vb.D/vb.P_atm
        delta_c = vb.C_b-c
        print(c,vb.C_b,delta_c)

        #Condition to stop execution if the radius starts to decrease :

        if alpha*delta_c/self.radius<0 :
            print("Decreasing radius, code failure at time ",t," s")
            sys.exit()

        self.radius = self.radius + vb.dt*alpha*delta_c/self.radius

    def grow_analytical(self,t,c) :
        self.radius = np.sqrt(2*vb.R_gp*vb.T*vb.D/vb.P_atm * (vb.C_0-c) * t + vb.R_0**2)

    def no_grow(self) :
        self.radius = self.radius

#   SPEED

    def constant_speed(self,t) :
        self.speed=self.speed

    def update_speed(self,t) :
        # Computes the drag coefficient as a function of Reynolds :

        Reynolds=vb.rho_liq*2*self.speed*self.radius/vb.mu_liq

        if Reynolds<1 :
            if self.printing_counter != 1 :
                print("Using Re < 1 at t=",t)
                self.printing_counter=1
            C_d=24/Reynolds
        elif Reynolds>1 and Reynolds<10**3 :
            if self.printing_counter != 2 :
                print("Using 1 < Re < 10**3 at t=",t)
                self.printing_counter=2
            C_d=18.5/Reynolds**(0.6)
        elif Reynolds>10**3 and Reynolds<3*10**5 :
            if self.printing_counter != 3 :
                print("Using Re > 10**3 at t=",t)
                self.printing_counter=3
            C_d=0.5
        elif Reynolds> 3*10**5 :
            if self.printing_counter != 4:
                print ("Using Re > 3*10**5 at t=",t)
                self.printing_counter=4
            C_d=0.07

        self.Reynolds=Reynolds
        print("Adding to speed : ", vb.dt*(-3*vb.rho_liq*self.speed**2*C_d/8/vb.rho_gaz/self.radius + vb.g*(vb.rho_liq-vb.rho_gaz)/vb.rho_gaz))
        self.speed += vb.dt*(-3*vb.rho_liq*self.speed**2*C_d/8/vb.rho_gaz/self.radius + vb.g*(vb.rho_liq-vb.rho_gaz)/vb.rho_gaz)

        Alpha = -3*vb.rho_liq*C_d/8/vb.rho_gaz/self.radius
        Beta = vb.g*(vb.rho_liq-vb.rho_gaz)/vb.rho_gaz
        Gamma = -3*vb.rho_liq*self.speed**2*C_d/8/vb.rho_gaz/self.radius

        print("Bêta = ",Beta)
        print("Alpha =",Alpha)
        print("Gamma =",Gamma)

        self.speed_variables_output.write(str(t)+' '+str(Beta)+' '+str(Gamma)+' '+str(Gamma+Beta)+'\n')


    # def terminal_speed(self) :
    #     eotvos = (vb.rho_liq-vb.rho_gaz)*vb.g*4*self.radius**2/vb.sigma
    #     f_sc = 1+0.5/(1+np.exp((np.log(eotvos)+1)/0.38))
    #
    #     self.speed=1/(np.sqrt(f_sc**2*(144*vb.mu_liq**2/vb.g**2/vb.rho_liq**2/(self.radius)**4
    #                                 + vb.mu_liq**(4/3)/0.14425**2*vb.g**(5/3)*vb.rho_liq**(4/3)*(self.radius)**3)
    #                                 + 1/(2.14*vb.sigma / vb.rho_liq * 2*self.radius)/0.505*vb.g*2*self.radius))
    def terminal_speed(self) :
        speed_viscous = (vb.g*vb.rho_liq*(2*self.radius)**2/12/vb.mu_liq)

        speed_inertial = (0.14425*vb.g**(5/6)*vb.rho_liq**(2/3)*(2*self.radius)**(3/2)/vb.mu_liq**(2/3))

        speed_spheroid = np.sqrt(2.14*vb.sigma/vb.rho_liq/2/self.radius + 0.505*vb.g*2*self.radius)

        self.speed = (1/np.sqrt(1/speed_viscous**2 + 1/speed_spheroid**2 + 1/speed_inertial**2))

    def accelerate(self,t) :
        u=9*vb.mu_liq*t/2/vb.rho_gaz/self.radius**2
        u_prime=9*vb.mu_liq*(self.radius-2*t)/2/vb.rho_gaz/self.radius**3
        # L'accélérration est calculée analytiquement en fonction du rayon qu'il faut mettre à jour avant (lui aussi analytique)
        #self.acceleration=2*vb.rho_liq*vb.g/9/vb.mu_liq*(-self.radius**2*u_prime*np.exp(u)+2*self.radius*(1-np.exp(u)))
        self.acceleration=vb.dt*(-9*vb.mu_liq*self.speed/2/vb.rho_gaz/(self.radius**2) + vb.g*(vb.rho_liq-vb.rho_gaz)/vb.rho_gaz)



#   ALTITUDE

    def update_altitude(self) :
        self.altitude-=vb.dt*self.speed


# ___________ ADVANCE USING THE CORRECT MODEL __________

    def rise_and_grow(self,model_to_use,t) :

        # __________ MODELS __________ :

        # Model 1 : no growth just acceleration ++
        # Model 2 : analytical growth and acceleration ~~
        # Model 3 : numerical growth with constant concentration but constant speed (no acceleration)
        # Model 4 : numerical growth with analytical concentration and constant speed
        # Model 5 : All numerical (except concentration)
        # Model 6 : Speed is taken as equal to terminal at each given radius

        # _________ MODEL 1_________

        if model_to_use==1 :
            self.update_altitude()
            self.update_speed(t)
            self.accelerate(t)
            self.no_grow()

        #__________ MODEL 2 ___________

        if model_to_use==2 : # Modèle avec C=Cte
            self.update_altitude()
            self.update_speed(t)
            self.accelerate(t)
            self.grow_analytical(t,vb.C_i)

        #__________ MODEL 3 ___________

        elif model_to_use==3 :
            #self.update_altitude()
            self.constant_speed(t)
            self.accelerate(t)
            #self.grow(t-vb.t_0,liq.get_concentration(self.get_altitude(),t,vb.n_modes))
            self.grow(t-vb.t_0,57)
            #print("altitude : ",self.altitude)
            #print("concentration : ",liq.get_concentration(self.get_altitude(),t,vb.n_modes))

        # __________ MODEL 4 __________

        elif model_to_use==4 :
            #self.update_altitude()
            self.constant_speed(t)
            self.accelerate(t)
            self.grow_analytical(t-vb.t_0,liq.get_concentration(vb.h/2,t,vb.n_modes))
                                                              # temps propre ^^^^^^^^  ????
        # __________ MODEL 5 __________

        elif model_to_use==5 :
            self.update_altitude()
            self.update_speed(t)
            self.accelerate(t)
            self.grow(t-vb.t_0,liq.get_concentration(self.get_altitude(),t,vb.n_modes))

        #___________ MODEL 6 ____________

        elif model_to_use==6 :
            self.update_altitude()
            self.grow_analytical(t-vb.t_0,liq.get_concentration(vb.h/2,t,vb.n_modes))
            self.terminal_speed()
