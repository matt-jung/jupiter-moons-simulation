# jupiter-moons-simulation
A simulation of the motion of Jupiter's moons, using three different methods of numerical integration.

**main.py** - main simulation file where instances of the class Particle are created, bodies are advanced and results are saved. Requires numpy and copy. Tested on Python 3.9.12

**Particle.py** - Particle class containing Euler, Euler-Cromer, and Euler-Richardson methods to update position and velocity, method to update gravitational acceleration, and methods to calculate kinetic energy, potential energy, linear momentum, and angular momentum. Requires numpy.

**orbits_analysis.py** - Post-processing script to plot the orbits. Requires matplotlib and numpy.

**conservation_analysis** - Post-processing script to plot the conservation of total energy, total linear momentum, and total angular momentum over the duration of the simulation. Requires matplotlib and numpy.

**tablevalues.py** - Post-processing script to print lists of the final position of each body in the system for each numerical method. Requires numpy.
