

class Restaurant:
    '''A class represents general restaurant.'''
    def __init__(self,name, cuisine, location):
        self.name = name
        self.cuisine = cuisine
        self.location = location
    def describe_restaurant (self):
        print(f' The Restaurant {self.name.title()} servicing the {self.cuisine} cuisine to the people of {self.location.title()}')
    def open_restaurant (self):
        print(f'*** WELCOME to the  {self.name} is now open in {self.location}')
    def closed_restaurant(self):
        print(f' {self.name} is finally colsed and for good!')


class IceCreamStand (Restaurant):
    flavors = ['Vanilla','chocolate','caramel','strawberry']

    def list_of_icecream_flavors(self):
        """returns all available flavors."""
        for flavor in self.flavors:
            print(f"We have {flavor} ice-cream: ")
''''
ice_stand = IceCreamStand("carvel","american","downtown")
ice_stand.open_restaurant()
ice_stand.list_of_icecream_flavors()
ice_stand.describe_restaurant()
'''
# HW 9-7,9-8,9-9