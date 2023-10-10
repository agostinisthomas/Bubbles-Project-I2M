import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import variables as vb


def plot_params(file,bubble_id) :

    path = '../OUTPUTS/Multiple_Bubbles/'+file+'.txt'
    with open(path) as f :
        time=[]
        rad=[]
        speed=[]
        alt=[]
        n_bubbles=[]
        lines = f.readlines()
        for l in lines :
            #if l.startswith(bubble_id):
            if l.startswith(lines[2].split()[0]) :
                time.append(float(l.split()[1]))
                rad.append(float(l.split()[2]))
                speed.append(float(l.split()[3]))
                alt.append(float(l.split()[4]))

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Évolution des paramètres en fonction du temps")
    ax1.set_xlabel('Temps (s)')

    ax1.plot(time,rad, c='r', label='Radius (m)')
    ax1.plot(time,speed, c='b', label='Speed (m/s)')
    ax1.plot(time,alt, c='g', label='Altitude (m)')
    ax1.grid()
    leg = ax1.legend()
    plt.show()





def plot_bubble_count(file) :
    path = '../OUTPUTS/Multiple_Bubbles/'+file+'.txt'
    with open(path) as f :
        n_bubbles=[]
        lines = f.readlines()
        for l in lines :
            if l.startswith('New') :
                n_bubbles.append(int(l.split()[-1]))

    time=np.linspace(vb.t_0,vb.t_f,(vb.t_f-vb.t_0)/vb.dt)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Évolution du nombre de bulles en fonction du temps")
    ax1.set_xlabel('Temps (s)')
    ax1.plot(time,n_bubbles, c='g', label='Nombre de bulles')

    leg = ax1.legend()

    plt.show()
