# PARAMETRES A PRENDRE EN ENTREE :

t_0=500   # Temps ecoule depuis l'ouverture de la bouteille
t_f=503
C_0=227.3   # Concentration initiale du champagne en C02
C_lost = 50  # Pourcentage de la concentration initiale dispersée au premier degazage
y_0=0.2     # Profondeur initiale en m
R_0=0.1*10**-3   # Rayon initiale en m
h=0.2  # Hauteur du liquide dans le verre
n_modes=3 # Ordre de resolution fourrier

# PARAMETRES NUMERIQUES :

dt=1*10**(-2)
dy=0.0001
ny=h/dy

# PARAMETRES GLOBAUX/CONSTANTES :

C_atm=0.0180    # mol/m**3
D=2*10**(-5)    # m**2/s
pi=3.1417
rho_liq=998   # kg/m**3
rho_gaz=1.98  # kg/m**3
g=9.8   # m/s**2
mu_liq=1.3*10**-3  # 50% de plus que l'eau
T=298  # Temperature en Kelvin pour le moment constante
P_atm=10**5  #Pa  -  Pourrait etre interessant de changer
R_gp=8.314  # Constante des Gazs Parfaits
sigma = 75*10**(-3)  # Coeff de tension superficielle eau/air

# CALCULS PRELIMINAIRES :

C_0 = C_0*C_lost/100  # Prise en compte du dégazage initial
C_i=C_0-C_atm
C_b=P_atm/(R_gp*T)
