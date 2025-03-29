""" package manager
artifactory
library
pip install library
pyp"""

class Ork():
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def sit(self):
        print(f'{self.name.title()} is now sitting and getting ready to attack!')
    def smash(self):
        print(f'{self.name.title()} just smashed the olog"s face!')


my_ork = Ork('Grok',23)
print(f' my Ork name is {my_ork.name}')
print(f"Meet the Ork {my_ork.name.title()} and he is ready for  anything in his {my_ork.age} ")
my_ork.smash()
villian_ork = Ork('subasda',55)
print(f"Meet the Ork {villian_ork.name.title()} and he is ready to squat in his {villian_ork.age} ")
villian_ork.sit()
new_morron_ork = Ork ('clop',18)
new_morron_ork.smash()
new_morron_ork.sit()
my_ork.name = "Strepper"
my_ork.age =77
my_ork.smash()
my_ork.sit()
print(f' my Ork name is {my_ork.name}')


