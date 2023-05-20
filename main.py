import numpy as np
import copy
from Particle import Particle




# Create class instances for Jupiter and some of its moons using JPL ephemeris data: https://ssd.jpl.nasa.gov/horizons/app.html#/ 
# N.B. Data was collected with Coordinate Center: Jupiter (body center) [500@599]3 and Time Specification: Start=2022-11-23 TDB
# N.B. Ephemeris data (inside the arrays) is in km and km/s - the factor of 1E3 outside each array converts to m and m/s

Jupiter = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Jupiter",
    mass=1.8982E27 #https://en.wikipedia.org/wiki/Jupiter
)

Ganymede = Particle(
    position=1E3*np.array([-3.830690977125093E+05, 1.001060365280042E+06, 3.285284395783878E+04]), 
    velocity=1E3*np.array([-1.015213367410711E+01, -3.852220246483439E+00, -2.877588085504559E-01]), 
    acceleration=np.array([0, 0, 0]),
    name="Ganymede",
    mass=1.4819E23 #https://en.wikipedia.org/wiki/Ganymede_(moon)
)

Callisto = Particle(
    position=1E3*np.array([1.127695971697591E+05, 1.875771116631672E+06, 6.057062001657067E+04]), 
    velocity=1E3*np.array([-8.198091675280645E+00, 5.536572051411509E-01, -9.189396136179334E-02]), 
    acceleration=np.array([0, 0, 0]),
    name="Callisto",
    mass=1.0759E23 #https://en.wikipedia.org/wiki/Callisto_(moon)
)

Io = Particle(
    position=1E3*np.array([-2.796659157335864E+05,3.176282484756653E+05 ,6.990008994911055E+03 ]), 
    velocity=1E3*np.array([-1.299021364167695E+01, -1.137285204844673E+01,-6.005303347461712E-01 ]), 
    acceleration=np.array([0, 0, 0]),
    name="Io",
    mass=8.9319E22 #https://en.wikipedia.org/wiki/Io_(moon) 
)

Europa = Particle(
    position=1E3*np.array([3.712647483927379E+05,5.604013190172540E+05,2.857493604879908E+04 ]), 
    velocity=1E3*np.array([-1.149296817740253E+01,7.467833671425606E+00,8.900302604355925E-03]), 
    acceleration=np.array([0, 0, 0]),
    name="Europa",
    mass=4.7998E22 #https://en.wikipedia.org/wiki/Europa_(moon) 
)


Bodies=[Jupiter,Io,Europa,Ganymede,Callisto]


# Set time parameters
deltaT=10000 # Time interval of 100 seconds
stopTime=10368000 # Simulation will continue for 10,368,000 seconds, or 120 Days
elapsedTime = 0


# Create empty data set
data = []


# Temporal cycle
for i in range(0,stopTime,deltaT):


    # Update accelerations for all bodies
    for item1 in Bodies:
        item1.acceleration = 0 # Reset body's acceleration, to avoid adding to the previous iteration's value
        item1.updateGravitationalAcceleration(Bodies)
    
# Update positions and velocities of all bodies using numerical method of choice [Euler, Euler-Cromer, or Euler-Richardson]
# N.B. Euler-Ricahrdson method takes a list of bodies, i.e. Bodies, as an additional argument as well as deltaT
    for item in Bodies:
        item.EulerCromer(deltaT)

    # Update elapsed time in seconds
    elapsedTime += deltaT


    if ((i/stopTime)*100) % 10 ==0:
        print("Simulation loading.......{0:.0f}%".format((i/stopTime)*100))



    # Collect data every 10000 seconds
    if (i%(10000)) == 0: 

        

        # Calculate total energy of the system

        K=0 # Total kinetic energy of the system
        U=0 # Total potential energy of the system

        # Add each body's kinetic and potential energy to the total
        for item1 in Bodies:
            K += item1.kineticEnergy()
                
            for item2 in Bodies:
                if item1 != item2:
                    U += item1.potentialEnergy(item2)
        
        totalEnergy = U + K


        # Calculate total linear momentum of the system
        totalLinearMomentum = 0
        for item in Bodies:
            totalLinearMomentum += item.linearMomentum()
            

        
        #Calculate total angular momentum of the system
        totalAngularMomentum = 0
        for item in Bodies:
            totalAngularMomentum += item.angularMomentum()
            



        myList = [elapsedTime, totalEnergy, np.linalg.norm(totalLinearMomentum), np.linalg.norm(totalAngularMomentum)]


        # Create copies of all bodies
        copies = []
        for item in Bodies:
            copies.append(copy.deepcopy(item))
        myList.extend(copies)   
        
        data.append(myList)



# Save data as an npy file        
np.save("EulerRichardson", data, allow_pickle=True)


