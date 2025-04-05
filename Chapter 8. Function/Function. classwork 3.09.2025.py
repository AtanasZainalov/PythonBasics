def greet_user():
    print('hello work')

varik = input('Which pill you"ere going to choose ? RED or BLUE ')
if varik.lower() == "red":
    greet_user()
else:
    print('go back to sleep')

def greet_user_by_name(user_name) : #function has parameter 1 usage
    """
    Prints Hello Along with the username. Function has a parameter,
    username is a parameter
    """
    print(f'Hello , {user_name.title()}!')

def describe_pet(anymamal_type,pet_name):
    print("\nI have a " + anymamal_type + ".")
    print("My "+ anymamal_type + "'s name is "+ pet_name.title() + ".")
greet_user_by_name('John')
greet_user_by_name('Kreig')
greet_user_by_name('Teenage Turtle')
print("Today", 'Is Sunday' ,2+2 , '= 5', ' is ' ,False, sep='||',end='(*Y@*#&Y*@&#\n')
print('SOKRAT')
def describe_pet_with_default_value(anymamal_type,pet_name,age =1):
    print("\nI have a " + anymamal_type + ".")
    print("My " + anymamal_type + "'s name is " + pet_name.title() + ".")
    print(f'.its age is  {age}')

describe_pet_with_default_value('Cat','pussy',3)

describe_pet('Horse','Roach')


###homework 8-3   /   8-5
