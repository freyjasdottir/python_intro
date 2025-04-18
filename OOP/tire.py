import math
class Tire:
    """
    Tires on an autovelocitator.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type= tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        Returns tire's information in its standard notation.
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")
    
    def circumference(self):
        """
        The circumference of the tire in inches.
        This is a very simple doctest, I probably would not use it in a real project in favor of an outside testing framework.
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)
    
    #Start private methods with a single underscore
    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4

#Can create classes that inherit from superclasses
class SnowTire(Tire):
    
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand ='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness
    
    def circumference(self):
        """
        The circumference of a tire w/ snow chains in inches
        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)
    
    def __repr__(self):
        return super().__repr__() + " (Snow)"