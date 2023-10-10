import variables as vb
import liquid as liq
import numpy as np

file=open('../OUTPUTS/analytical_radius.txt','w')

t=vb.t_0
radius=vb.R_0

c=liq.get_concentration(vb.h/2,t,5)
print("c = ",c)
print(vb.D)

while t<vb.t_f :
    c=liq.get_concentration(vb.h/2,t,5)
    radius=np.sqrt(2*vb.R_gp*vb.T*vb.D/vb.P_atm * (vb.C_0-c) * (t-vb.t_0) + vb.R_0**2)
    file.write(str(t)+' '+str(radius)+' ' + str(c)+'\n')
    t+=vb.dt
