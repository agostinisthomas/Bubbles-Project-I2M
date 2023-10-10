import variables as vb
import numpy as np


def speed_viscous(r) :
    return (vb.g*vb.rho_liq*(2*r)**2/12/vb.mu_liq)

def speed_inertial(r) :
    return ( 0.14425*vb.g**(5/6)*vb.rho_liq**(2/3)*(2*r)**(3/2)/vb.mu_liq**(2/3))

def speed_spheroid(r) :
    return ( np.sqrt(2.14*vb.sigma/vb.rho_liq/2/r + 0.505*vb.g*2*r) )

def speed_general(r) :
    return (1/np.sqrt(1/speed_viscous(r)**2 + 1/speed_spheroid(r)**2 + 1/speed_inertial(r)**2))

file = open('../OUTPUTS/speed_separate_terms.txt','w')

dr = 1*10**(-5)
r=dr
r_max = 1*10**(-2)

while r<r_max :
    list=[speed_viscous(r) , speed_inertial(r) , speed_spheroid(r)]
    file.write(str(r)+' '+str(speed_viscous(r))+' '+str(speed_inertial(r))+' '+str(speed_spheroid(r))+' '+str(min(list))+' '+str(speed_general(r))+'\n')
    r+=dr
