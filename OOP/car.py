#delcaring a class looks like this

class Car: #Classic example :v
     """
     This is a docstring, it describes what the class is.
     Car models a car with tires and an engine
     """

     def __init__(self, engine, tires): #When a new class instance is created, this function executes.
          """
          Docstrings also can describe methods.
          """
          self.engine = engine
          self.tires = tires
     
     def description(self): 
          print(f"A car with an {self.engine} engine, and {self.tires} tires")
    
     #This separates the concern of calculating the wheel circ to the Tire, instead of the Car.
     def wheel_circumference(self):
          if len(self.tires) > 0:
               return self.tires[0].circumference()
          else:
               return 0