import variables as vb
import numpy as np

file = open('speed_function.txt','w')
t=vb.t_0

while t<vb.t_f :
    speed=2*vb.R_0**2*vb.rho_liq*vb.g/9/vb.mu_liq*(1-np.exp(-9*vb.mu_liq*t/2/vb.rho_gaz/vb.R_0**2))
    print('speed : ',speed)
    file.write(str(t)+"  "+str(speed)+"\n")
    t+=vb.dt
