import liquid as liq
import variables as vb
import numpy as np

n=15
t=500

file=open('../OUTPUTS/concentration_analytical.txt','w')

def get_concentration(y,t,n) :
    conc=0.
    for i in range(n+1) :
        conc+=(4*vb.C_i/((2*i+1)*vb.pi)*np.exp(-((2*i+1)*vb.pi/(2*vb.y_0))**2*vb.D*t)*np.sin((2*i+1)*vb.pi*(vb.h-y)/(2*vb.y_0)))
    return conc

for i in range(int(vb.ny)) :
    file.write(str(i*vb.dy)+' '+str(get_concentration(i*vb.dy,t,n))+'\n')
