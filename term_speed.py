import liquid as liq
import variables as vb
import numpy as np

n=15
t=vb.t_0

file=open('../OUTPUTS/term_speed.txt','w')


def terminal_speed(r) :
    eotvos = (vb.rho_liq-vb.rho_gaz)*vb.g*4*r**2/vb.sigma
    f_sc = 1+0.5/(1+np.exp((np.log(eotvos)+1)/0.38))

    return(1/(np.sqrt(f_sc**2*(144*vb.mu_liq**2/vb.g**2/vb.rho_liq**2/(r)**4
                                + vb.mu_liq**(4/3)/0.14425**2*vb.g**(5/3)*vb.rho_liq**(4/3)*(r)**3)
                                + 1/(2.14*vb.sigma / vb.rho_liq * 2*r)/0.505*vb.g*2*r)))


def speed_viscous(r) :
    return (vb.g*vb.rho_liq*(2*r)**2/12/vb.mu_liq)

def speed_inertial(r) :
    return ( 0.14425*vb.g**(5/6)*vb.rho_liq**(2/3)*(2*r)**(3/2)/vb.mu_liq**(2/3))

def speed_spheroid(r) :
    return ( np.sqrt(2.14*vb.sigma/vb.rho_liq/2/r + 0.505*vb.g*2*r) )

def speed_general(r) :
    return (1/np.sqrt(1/speed_viscous(r)**2 + 1/speed_spheroid(r)**2 + 1/speed_inertial(r)**2))

# INIT

c=liq.get_concentration(vb.h/2,t,5)
radius=np.sqrt(2*vb.R_gp*vb.T*vb.D/vb.P_atm * (vb.C_0-c) * (t-vb.t_0) + vb.R_0**2)
speed = terminal_speed(radius)
speed_g = speed_general(radius)
print("Smallest radius = ",radius)

# TIME LOOP

while t<vb.t_f :
    c=liq.get_concentration(vb.h/2,t,5)
    radius=np.sqrt(2*vb.R_gp*vb.T*vb.D/vb.P_atm * (vb.C_0-c) * (t-vb.t_0) + vb.R_0**2)
    speed = terminal_speed(radius)
    speed_g = speed_general(radius)
    file.write(str(t)+' '+str(speed)+' '+str(radius)+' '+str(speed_g)+'\n')

    t+=vb.dt

print("Biggest radius : ", radius)
