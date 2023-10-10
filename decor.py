# PACKAGES :
import variables as vb
import liquid as liq
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches

# Super class to handle the arrival of data

class SimulationDecor :

    def __init__(self) :
        pass

    def decorate(self,t,simulation) :
        pass

# SUBCLASS FOR .TXT FILES

class TxtDecor(SimulationDecor) :

    def __init__(self,filename):
        super().__init__()
        if not filename.endswith('.txt'): # Just to be sure
            filename+='.txt'
        self.file = open('../OUTPUTS/Multiple_Bubbles/'+filename,'w')

    def write_txt_file(self,t,bubble,index):
        self.file.write(str(bubble.get_id())+' '+str(t)+' '+str(bubble.get_radius())+' '+str(bubble.get_speed())+' '+str(bubble.get_altitude())+' '+str(bubble.get_abscissa())+' '+str(bubble.site_id)+'\n')


    def finalize(self,simu):
        self.file.close()

    def decorate(self,t,simulation) :
        self.file.write("################################################################################################## \n")
        self.file.write("New iteration, t="+str(t)+"s"+"   "+ "Number of bubbles : "+str(len(simulation.bubbles))+"\n")
        for b in simulation.bubbles :
            index = simulation.bubbles.index(b)
            self.write_txt_file(t,b,index)

# SUBCLASS FOR MATPLOTLIB ANIMATIONS

class MatplotlibDecor(SimulationDecor) :

    def finalize(self):
        self.plot_with_matplot()


    # Initialise bubble position vectors (to be passed as parameter later on)
    def __init__(self) :

        super().__init__()

    # --------- ANIMATION ---------
    # Initialisation function to setup the BG

    def init(self):
            self.ax.add_patch(self.patch)
            return self.patch,


    # Function called iteratively :
    def animate(self,i):
        print("Animate check 1")
        self.patch=patches.Circle((self.x_coordinates_vector[i],vb.y_0-self.y_coordinates_vector[i]),self.radius_vector[i])

        # Pour que le script s'arrete lorsque la bulle atteint la surface :
        # if self.patch.center[1]>=0.95*plt.gca().get_ylim()[1]:
        #     sys.exit()
        #This needs to be changed : can't terminate process every time a bubbles reaches surface
        print('Animate check 2')
        return self.patch,

    def plot_with_matplot(self) :

        # Creating figure object, axis, and setting their respective sizes :
        self.fig = plt.figure()
        # plt.ylim(0,0.2)
        # plt.xlim(-0.3,0.3)
        # plt.axis('equal')
        # self.fig.grid()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(0, 0.5)
        print("Radius vector \n",self.radius_vector)
        self.patch = patches.Circle((0,0), self.radius_vector[0])
        print("Patch : ",self.patch)
        self.anim=animation.FuncAnimation(self.fig, self.animate,
                                    init_func=self.init,
                                    frames=len(self.y_coordinates_vector),
                                    interval=200,
                                    blit=False)
        plt.show()
