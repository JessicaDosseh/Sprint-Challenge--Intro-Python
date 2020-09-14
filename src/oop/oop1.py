# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # Base class
    pass

# ---------------------------------------


class GroundVehicle(Vehicle):  # class composition (Vehicle has a GroundVehicle)
    pass


class Car(GroundVehicle):  # class inheritance (Car is a GroundVehicle)
    pass


class Motorcycle(GroundVehicle):  # class inheritance (Motorcycle is a GroundVehicle)
    pass

# ---------------------------------------


class FlightVehicle(Vehicle):  # class composition (Vehicle has a FlightVehicle)
    pass


class Starship(FlightVehicle):  # class inheritance (Starship is a FlightVehicle)
    pass


class Airplane(FlightVehicle):  # class inheritance (Airplane is a FlightVehicle)
    pass
