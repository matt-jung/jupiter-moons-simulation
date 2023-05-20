# ANALYSIS ONE
# STABLE ORBITS

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


plt.rcParams['text.usetex'] = True


Bodies=["$Jupiter$","$Io$","$Europa$","$Ganymede$","$Callisto$"]
Colours = ['black','tab:blue','tab:orange','tab:green','tab:red']

# Set matplotlib formatting preferences
mpl.rc('font',size=18)
mpl.rc('lines',linewidth=2,marker='',markersize=6,markeredgewidth=3)
mpl.rc('errorbar',capsize=6)
mpl.rc('axes',linewidth=1,grid=False)
mpl.rc('xtick.major',size=10,width=1)
mpl.rc('xtick.minor',visible=False,size=5,width=3)
mpl.rc('ytick.major',size=10,width=1)
mpl.rc('ytick.minor',visible=False,size=5,width=3)

# Load npy file
data = np.load("EulerRichardson.npy", allow_pickle=True)
iterations = len(data)




fig = plt.figure()

for i in range(len(Bodies)):
    xCoordinate = []
    yCoordinate = []

    for j in range(0,iterations):
        xCoordinate.append(data[j][i+4].position[0])
        yCoordinate.append(data[j][i+4].position[1])
    
    plt.plot(xCoordinate,yCoordinate,Colours[i], label=Bodies[i])








plt.xlabel("$x [m]$", fontsize=20)
plt.ylabel("$y [m]$", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend()



plt.show()

