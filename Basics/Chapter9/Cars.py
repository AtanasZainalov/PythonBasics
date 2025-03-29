# Object-Oriented Programming concepts:
# 1. Class, object
# 2. Encapsulation - hiding the attribute or method from instance(object), or from child
# 3. Inheritance
# 4. Polymorphism - method overriding

class Car:
    """general car representation."""

    def __init__(self, make, model, year):
        """Constructor method of car class."""
        self.make = make
        self.model = model
        self.year = year
        # encapsulation with leading '__'
        self.__odometer_reading = 0  # attribute with default

    def get_description(self):
        print("**************************************")
        print(f"Car details: {self.make.upper()}, {self.model.title()} {self.year}")
        print(f"with {self.__odometer_reading} miles on it.")

    def update_odometer(self, milage):
        # new value should not be less than existing value
        # new value => milage
        # existing vale => self.odometer_reading
        # when new value > existing then update to a new value
        # when new value <= existing then dont update, print a message
        if milage > self.__odometer_reading:
            self.__odometer_reading = milage
        else:
            print(f"Odometer can not be set less than {self.__odometer_reading}.")

    def get_odometer_readings(self):
        return self.__odometer_reading

class ElectricCar(Car):
    """
    Inheritance of Car class.
    """
    def __init__(self, make, model, year, battery_size=85):
        """Constructor method of electric car class."""
        # call the constructor of parent class
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def charge(self, kwh):
        print("Charging is initiated ...")
        print(f"{self.model} charging reached intended {kwh} kwh.")
        print(f"Your batter size is {self.battery_size}")

    def get_description(self):
        print("#################################")
        print(f"Important information about your Electric Car")
        print(f"\n\t{self.make.upper()},\n\t{self.model.upper()} \n\t {self.model.title()} Model Year\n\t{self.year}")
        print(f"with {self.get_odometer_readings} miles on it.")
