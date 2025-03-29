cars = ['tesla model x','byd','bmw i7','rivian rlt', 'lucid air']
#temporarily : ascending and descending - creates a copy of the list
#permanently  ascending and descending - orders original list
#reversing list : reverses the original list
print(cars)
print(cars.sort())
print('_______________________')
cars.reverse() #reversing the list
print(cars)
cars.sort()   #sorting th elist ascending permanently
print('a',cars[0],cars [2],sep='|',end="\t\t")
#Function - something with a code behind that will execute or solve somenthing
#parameter -
cars_sold=[]
print("Welcome to the Shitshow Sales")
for car in cars:
    print(f'We got a great offer fro our crappy {car}')
    print(f'{car.upper()} is sold!!!')
    ##remove the car from the list
    cars_sold.append(cars.pop(1))
    print(f'we still have this cars for you : {cars}')
    print(f'we have sold those cars {cars_sold}')
    print("==============")

for i in range(4):
    print({cars[0].title()})
####Akmals notes

print("-------------------------- option 2 -------------------------------------")

cars_sale = ['dugati vayron', 'tesla Model Y', 'bmw m5', 'ferrari F80']
cars_sold = []
print("Welcome to Limited Sale!")
print(f"Check out our discounted car list today: {cars_sale}")

for i in range(4):  # 0, 1, 2, 3
    print(f'We got a great offer for {cars_sale[0].title()}')
    print(f"{cars_sale[0].upper()} is sold!!!!")
    # remove the car from the list
    cars_sold.append(cars_sale.pop(0))
    print(f"We still have these cars for you : {cars_sale}")
    print("==============================================")

print(f"Here is the list of sold cars today: {cars_sold}")
print("********* All cars are sold out!!! *********")



sum = 0
for num in range (160,171):
    print(f"num is {num}")
    print(f'num is {sum}')
    sum = sum +num
    print("_____________________________")