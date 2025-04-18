from tire import Tire
from car import Car

tire = Tire('P', 205, 65, 15)
tires = [tire, tire, tire, tire]
honda = Car(tires=tires, engine="4-cyl")
print(honda.description())
print(honda.wheel_circumference())

honda.tires = []
print (honda.wheel_circumference())

print (tire.circumference())