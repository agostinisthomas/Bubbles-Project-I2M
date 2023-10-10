# PACKAGES

import simulation as sim
import liquid as liq
import decor
import bubbles
import plotting
from time import process_time

#               Démarrage du chrono :

time_start=process_time()

#               Fixed variables for testing :

n_modes = 15
modele = 6
n_bubbles = 2
n_sites = 5
filename = 'Trial'

#                Create objects needed :

liquid=liq.Liquid() # Object Liquid from class Liquid
simu=sim.Simulation(modele,n_sites) #  "" simu from class Simulation
deco=decor.TxtDecor(filename)
simu.initialise(filename)

#                Create bubbles  :

#b1,b2=bubbles.Bubble(simu.R_0, simu.y_0)
#simu.bubbles=[bubbles.Bubble(simu.R_0,simu.y_0,simu.x_0) for i in range(n_bubbles)]

# _____________________________ MAIN LOOP ____________________________

t = simu.t_0 # Initialize time

while t<=simu.t_f  : # Time loop

    # Write files :
    deco.decorate(t,simu)

    # Calculate at every time step :
    simu.advance(t)


    # Advance time :
    t+=simu.dt

#deco.finalize(simu)
time_stop=process_time()

print("Temps d'execution : ",time_stop-time_start," s")
print(simu.bubbles[0].get_id())
plotting.plot_params(filename,str(simu.bubbles[15].get_id()))
