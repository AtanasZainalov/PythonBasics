from pydoc import describe


class Restaurant:
    '''A class represents general restaurant.'''
    def __init__(self,name, cuisine, location):
        self.name = name
        self.cuisine = cuisine
        self.location = location
    def describe_restaurant (self):
        print(f' The Restaurant {self.name.title()} servicing the {self.cuisine} cuisine to the people of {self.location.title()}')
    def open_restaurant (self):
        print(f'the {self.name} is now open in {self.location}')
    def closed_restaurant(self):
        print(f' {self.name} is finally colsed and for good!')

my_restaurant = Restaurant('marzilla', 'Mediterranian','San Diego')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_frineds_favorite_restaurant=Restaurant('Astorcio','Italian','San Francisco')
my_frineds_favorite_restaurant.describe_restaurant()
my_frineds_favorite_restaurant.closed_restaurant()

"""HOME WORK 
9-3:9-5. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user"""
firtsName = input("first name")
lastName=input("last name")
class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = 17

    def describe_user (self):
        print(f'the user that just logged in is {self.first_name} {self.last_name} and his age is {self.__age}')
    def greet_user (self):
        print(f'Hello you {self.first_name} {self.last_name}  in your  {self.__age}')

greeting= User (firtsName,lastName,70)
describer = User(firtsName,lastName,78)

greeting.greet_user()
describer.describe_user()



