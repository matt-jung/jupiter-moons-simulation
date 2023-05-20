import numpy as np

# Load Data

Euler = np.load("Euler.npy", allow_pickle=True)
EulerCromer = np.load("EulerCromer.npy", allow_pickle=True)
EulerRichardson = np.load("EulerRichardson.npy", allow_pickle=True)

# Print lists of the final positions of all bodies in the system for each of the three methods

print("Euler")
for i in range(5):
    print("{:.2f},{:.2f}".format(Euler[1036][4+i].position[0],Euler[1036][4+i].position[1]))

print("Euler-Cromer")
for i in range(5):
    print("{:.2f},{:.2f}".format(EulerCromer[1036][4+i].position[0],EulerCromer[1036][4+i].position[1]))

print("Euler-Richardson")
for i in range(5):
    print("{:.2f},{:.2f}".format(EulerRichardson[1036][4+i].position[0],EulerRichardson[1036][4+i].position[1]))
