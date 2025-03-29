from cmath import phase
from pydoc import describe


def my_favorite_book(language,title = 'Holy Quran',name = 'Atanas') :
    print(f'My name is {name}  and my favorite book is : {title} and I want to be able to read it in {language} , '
          f'one day I will InShaAllah!')
my_favorite_book('Arabic')


"""T-shirt total makeover"""

def t_shirt_make (size, text_of_a_message):
    print(f'For the size : {size} , the print will be  {text_of_a_message} ')
t_shirt_make('L', 'Send him 2-3 years to Dagestan and forget')
t_shirt_make(size='L',text_of_a_message='Call the police')

"""Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""
print('_____________________________')

def make_shirt_mod (size = 'L', message = 'I love MMA'):
    print(f"for size  {size} the message will be  {message}")
print(make_shirt_mod())
sizes = ['S','M','L','XL','XXL','XXXL','XXXXL']
for custom_size in sizes:
    if custom_size == 'L':
        make_shirt_mod()
    elif custom_size == 'XL':
        make_shirt_mod(custom_size)
    else: make_shirt_mod(custom_size,'you can eat all you want')

"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""
cities = ['Moscow', 'Makhachkala', 'SanDiego']
countries = ['Russia', 'USA']
def describe_city (city, country='Russia'):
    print(f' {city.title()} is in {country} ')

for city_match in cities:
      if city_match == 'SanDiego':
          for country in countries:
              if country == 'USA':
                  describe_city(city_match,country)
      else:describe_city(city_match)






"""Hello everyone, 

Interview question: 
Create a function that checks if the given phrase is palindrome, where input should be only letters. You can check if phrase is only letters and more than one character. Make sure you test your code. 

Example:
is_palindrome(‘mom’) -> True
is_palindrome(‘hello’) -> False
is_palindrome(‘kayak’) -> True"""

words= ['mom','hello','kayak']
"""def is_palindrome (word):"""
def is_palindrome(candidate):
    for i in range(len(words)):
        reversed_word = words[i][::-1]
        if reversed_word == words[i]:
            print(f" {words[i]} is a palindrome")
    else: print(f' {words[i]} is not a palindrome')

manual_entry = input(' what is the word!?')

def is_palindrome2(candidate):
    reversed_manual_entry= manual_entry[::-1]
    if reversed_manual_entry == manual_entry:
        print(f' {manual_entry} is actually a palindrome!')
    else: print(f' {manual_entry} is not a palindrome , try again ')

is_palindrome(manual_entry)

def if_palindrome3(phrase):
    reversed_phrase = ''
    for i in phrase ():
        reversed_phrase = i+ reversed_phrase
    return reversed_phrase.lower()==phrase.lower()

print(if_palindrome3('skota'))

