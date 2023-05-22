
#  With out factory design

"""
from abstract import Bike, Car

c1 = input()

if c1 == "bike":
    print(Bike().create_vehicle())
elif c1 == "car":
    print(Car().create_vehicle())

"""


# With Factory design
from factory import VehicleFactory

inp = input()
VehicleFactory.get_vehicle(inp)