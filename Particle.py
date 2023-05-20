import numpy as np

class Particle:

    """
    Class to set up particle species

    Parameters
    ----------
    position: numpy array
        Array containing the 3D position of the particle
    velocity: numpy array
        Array containing the 3D velocity of the particle
    acceleration: numpy array
        Array containing the 3D acceleration of the particle
    name: string
        Name of the species
    """

    G=6.67408E-11

    def __init__(
    self,
    position=np.array([0, 0, 0], dtype=float), 
    velocity=np.array([0, 0, 0], dtype=float), 
    acceleration=np.array([0, 0, 0], dtype=float), 
    name='Particle',
    mass=1
    ):

        if mass<=0.0:
            raise ValueError("The mass of your particle should be positive.")

        self.position = np.array(position,dtype=float)
        self.velocity = np.array(velocity,dtype=float)
        self.acceleration = np.array(acceleration,dtype=float)
        self.name = name
        self.mass = mass
        
        
    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
        )


    def Euler(self, deltaT):

        """
        Method to update the 3D position and velocity vectors using the Euler method.

        Parameters
        ----------
        deltaT: float
            Time difference between iterations of the method
        """

        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT
        
    
    def EulerCromer(self, deltaT):

        """
        Method to update the 3D position and velocity vectors using the Euler-Cromer method.

        Parameters
        ----------
        deltaT: float
            Time difference between iterations of the method
        """

        self.velocity += self.acceleration * deltaT
        self.position += self.velocity * deltaT
    

    def EulerRichardson(self,deltaT,bodies):        
                                                   

        """
        Method to update the 3D position and velocity vectors using the Euler-Richardson method.

        N.B. This method only works in the case where particle acceleration is purely gravitational, i.e. no other forces are present

        Parameters
        ----------
        deltaT: float
            Time difference between iterations of the method
        bodies: list
            List of all bodies in the system
        """
        


        v_mid = self.velocity + 0.5 * self.acceleration * deltaT
        self_pos_mid = self.position + 0.5 * self.velocity * deltaT
        acc_mid = 0

        for i in range(len(bodies)):

            if self != bodies[i]:

                body_pos_mid = bodies[i].position + 0.5 * bodies[i].velocity * deltaT
                displacement_mid = self_pos_mid - body_pos_mid
                acc_mid += (-self.G * bodies[i].mass) / ((np.linalg.norm(displacement_mid))**2) * ((displacement_mid)/(np.linalg.norm(displacement_mid)))
        
        self.velocity = self.velocity + (acc_mid*deltaT)
        self.position = self.position + (v_mid * deltaT) 



    def updateGravitationalAcceleration(self, bodies):

        """
        Method to update the 3D acceleration vector of a body caused by all other bodies in the system

        Parameters
        ----------
        bodies: list
            List of all bodies in the system
        """

        for i in range(len(bodies)):

            if self != bodies[i]: # Acceleration of a body due to its own gravity cannot be calculated

                displacement = self.position - bodies[i].position
                self.acceleration += (-self.G * bodies[i].mass) / ((np.linalg.norm(displacement))**2) * ((displacement)/(np.linalg.norm(displacement))) # Newton's theory of gravitation a = -GM/r
    

    def kineticEnergy(self):

        """
        Method to calculate the kinetic energy of the particle
        """

        return 0.5 * self.mass * ((np.linalg.norm(self.velocity))**2) # Kinetic energy = 1/2 * mv^2


    def potentialEnergy(self,body):

        """
        Method to calculate the gravitational potential energy of the particle due to another body in the system

        Parameters
        ----------
        body: Particle
            Another body in the system
        """

        if self == body:
            raise ValueError("You cannot calculate the potential energy of an object due to itself.")

        else:
            displacement = self.position - body.position
            return (-self.G * self.mass * body.mass) / (np.linalg.norm(displacement)) # Gravitational potential energy = -GMm/r


    def linearMomentum(self):

        """
        Method to calculate the linear momentum vector of the particle
        """

        return self.mass * self.velocity # Momentum = mv


    def angularMomentum(self):

        """
        Method to calculate the angular momentum vector of the particle
        """

        return self.mass * (np.cross(self.position,self.velocity)) # Angular momentum = mvr
