from xml.dom.minidom import ProcessingInstruction

# RANGE () FUNCTION
# RANGE (START_NUMBER_INC,END_NUMBER,STEP) :DEFAULTS START NUMBER_INC=0,STEP 1
# RANGE (5,10,2) -> 5,7,9

numbers = [1,5,6,7,10]



for num in range(10,16,2):
    print(num)
new_list = []
squares = []
print("Print numbers dividable by 4")
for num in range(160,170):
    print(f"the square of {num} is {num**2}")
    print(f"the cube of {num} is {num **3}")
    new_list.append(num)
    squares.append(num**2)
print( new_list)
print(squares)
cubes2 = [num**3 for num in range(160,171)]


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:4]) # partial list
print(players[:4]) #partial list starting by default at 0
print(players[3:6]) #print the middle from 3 to 5 elements
print(players[:]) #pint all elements from 0 to the last one
copy_players=players[:]  # this is a copy of the list
copyp_layers2=copy_players
print(players)
print(copy_players)
players.append('atanas')
copyp_layers2.append('sloksa')
print(players)
print(copy_players)
print(copyp_layers2)
print("--------------------looping-------------------------")
for player in players [3:6]:
    print(f'{player} кроссовка')


