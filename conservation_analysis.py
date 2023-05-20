# ANALYSIS TWO
# CONSERVATION OF ENERGY AND MOMENTUM

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



mpl.rc('font',size=18)
mpl.rc('lines',linewidth=2,marker='',markersize=6,markeredgewidth=3)
mpl.rc('errorbar',capsize=6)
mpl.rc('axes',linewidth=1,grid=False)
mpl.rc('xtick.major',size=10,width=1)
mpl.rc('xtick.minor',visible=False,size=5,width=3)
mpl.rc('ytick.major',size=10,width=1)
mpl.rc('ytick.minor',visible=False,size=5,width=3)

plt.rcParams['text.usetex'] = True


# Load npy file
Euler = np.load("Euler.npy", allow_pickle=True)
EulerCromer = np.load("EulerCromer.npy", allow_pickle=True)
EulerRichardson = np.load("EulerRichardson.npy", allow_pickle=True)
iterations = len(Euler)

time = []

EulerEnergy = []
EulerMomentum = []
EulerAngMomentum = []

EulerCromerEnergy = []
EulerCromerMomentum = []
EulerCromerAngMomentum = []

EulerRichardsonEnergy = []
EulerRichardsonMomentum = []
EulerRichardsonAngMomentum = []


for i in range(iterations):
    time.append(Euler[i][0])
    EulerEnergy.append(Euler[i][1])
    EulerMomentum.append(Euler[i][2])
    EulerAngMomentum.append(Euler[i][3])

for i in range(iterations):
    EulerCromerEnergy.append(EulerCromer[i][1])
    EulerCromerMomentum.append(EulerCromer[i][2])
    EulerCromerAngMomentum.append(EulerCromer[i][3])

for i in range(iterations):
    EulerRichardsonEnergy.append(EulerRichardson[i][1])
    EulerRichardsonMomentum.append(EulerRichardson[i][2])
    EulerRichardsonAngMomentum.append(EulerRichardson[i][3])


fig = plt.figure(figsize=(10,8))


# FIRST GRAPH
# CONSERVATION OF ENERGY

ax1 = fig.add_subplot(3,1,1)
ax1.set_xlabel("$t [s]$",fontsize=20)
ax1.set_ylabel("$\Delta E / E$",fontsize=20)
plot1, = ax1.plot(time,abs((EulerEnergy-EulerEnergy[0])/EulerEnergy[0]),'tab:blue', label = "Euler")
plot1, = ax1.plot(time,abs((EulerCromerEnergy-EulerCromerEnergy[0])/EulerCromerEnergy[0]),'tab:green', label = "Euler-Cromer")
plot1, = ax1.plot(time,abs((EulerRichardsonEnergy-EulerRichardsonEnergy[0])/EulerRichardsonEnergy[0]),'tab:orange', label = "Euler-Richardson")


# SECOND GRAPH
# CONSERVATION OF LINEAR MOMENTUM

ax2 = fig.add_subplot(3,1,2)
ax2.set_xlabel("$t [s]$",fontsize=20)
ax2.set_ylabel("$\Delta p / p$",fontsize=20)
#plot2, = ax2.plot(time,abs((EulerMomentum-EulerMomentum[0])/EulerMomentum[0]),'tab:blue', label = "Euler")
plot2, = ax2.plot(time,abs((EulerCromerMomentum-EulerCromerMomentum[0])/EulerCromerMomentum[0]),'tab:green', label = "Euler-Cromer")
plot2, = ax2.plot(time,abs((EulerRichardsonMomentum-EulerRichardsonMomentum[0])/EulerRichardsonMomentum[0]),'tab:orange', label = "Euler-Richardson")


# THIRD GRAPH
# CONSERVATION OF ANGULAR MOMENTUM

ax3 = fig.add_subplot(3,1,3)
ax3.set_xlabel("$t [s]$",fontsize=20)
ax3.set_ylabel("$\Delta L / L$",fontsize=20)
#plot3, = ax3.plot(time,abs((EulerAngMomentum-EulerAngMomentum[0])/EulerAngMomentum[0]),'tab:blue', label = "Euler")
plot3, = ax3.plot(time,abs((EulerCromerAngMomentum-EulerCromerAngMomentum[0])/EulerCromerAngMomentum[0]),'tab:green', label = "Euler-Cromer")
plot3, = ax3.plot(time,abs((EulerRichardsonAngMomentum-EulerRichardsonAngMomentum[0])/EulerRichardsonAngMomentum[0]),'tab:orange', label = "Euler-Richardson")

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
fig.tight_layout(pad=2.0)

ax1.legend(loc=5,prop={'size': 10})
ax2.legend(loc=5,prop={'size': 10})
ax3.legend(loc=5,prop={'size': 10})
plt.show()




