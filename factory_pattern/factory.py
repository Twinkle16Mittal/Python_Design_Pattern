from abstract import Bike, Car


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "bike":
            print(Bike().create_vehicle())
        elif vehicle_type == "car":
            print(Car().create_vehicle())
