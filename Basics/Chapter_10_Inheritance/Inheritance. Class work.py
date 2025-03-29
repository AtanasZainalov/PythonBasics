from Basics.Chapter9.Cars import *
# from classes9.cars import Car, ElectricCar   second option


# all attributes and methods are available to child.

print("-------- regular car --------")
car1 = Car('lambo', 'huracan', 2025)
car1.get_description()
car1.update_odometer(80)
car1.get_description()
# print(car1.__odometer_reading) encapsulation
# car1.charge(10)  # not available to Parent class (Car)


print("-------- electric car --------")
ecar1 = ElectricCar('tesla', 'Cybertrack', 2025)
# TypeError: Car.__init__() missing 1 required positional argument: 'year'
ecar1.get_description()
ecar1.update_odometer(80)
ecar1.get_description()
# print(ecar1.__odometer_reading) encapsulation
print(ecar1.make, ecar1.model, ecar1.year)
ecar1.charge(10)

print("------------------------")
ecar2 = ElectricCar('tesla', 'model3', 2025, 75)
ecar2.get_description()
ecar2.update_odometer(200)
ecar2.get_description()
print(ecar2.make, ecar2.model, ecar2.year)
ecar2.charge(20)
