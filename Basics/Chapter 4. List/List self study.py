##do exersice in list
from os import remove
from xml.dom.minidom import ProcessingInstruction

print('remove from the list one of the guests')
guests = ['khabib','Pele','Mandela','Maradona']
print(f"here's our guests {guests}")


print(f'Greeteings Mr.{guests} we are happy invite you to a friend dinner next week at our house')
print(f'Very sadly Mr.{guests[0]} wont be able to come so we decided to send invitation to his boss Dana White')

guests.pop(0)
guests.insert(0,'Dana White')
print(f'Greetings Mr.{guests[0]} and thank you for making time to attend the dinner')
print(f"Turns out Mr.Khabib's close frined Mr.Cormier would like to come as well")

middle_index = len(guests)//2
guests.insert(middle_index,'Cormier')
print(f"Here's' updated list of our guests : {guests}")
print('URGENT UPDATE!! Mr.Khabib is coming ! Lets resend his invitation so he wont get lost in the woods!')

guests.append('Khabib')
print(guests)

print(f'Dear {guests} the catering service meesed up and the house is flodded and now we can invite only 2 people')
print(len(guests),' guests are invited')
print(f'Sorry Mr.{guests.pop()}, maybe nex time')
print(f'Sorry Mr.{guests.pop()}, maybe nex time')
print(f'Sorry Mr.{guests.pop()}, maybe nex time')
print(f'Sorry Mr.{guests.pop()}, maybe nex time')
print(f'Dear Mr{guests} you are still invited')
print(f'now the guests are gone and we have  {guests.clear()} of them at our home')
print(guests)






