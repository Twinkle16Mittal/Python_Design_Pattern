from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def create_vehicle(self):
        pass

class Car(Vehicle):
    def create_vehicle(self):
        return "creating Car"

class Bike(Vehicle):
    def create_vehicle(self):
        return "creating bike"
