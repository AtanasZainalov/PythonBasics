# num = 0
# while num < 5:
#     print(f' current value if NUM: {num}')
#     num = num + 1
#
#     total = 0
#     green_count = 0
#     alien_color = ""
#     while alien_color.lower() != 'quit' or alien_color != 'q':
#         alien_color = input("Enter the color to earn points: ")
#
#         if alien_color.upper() == 'GREEN':
#             green_count += 1
#             if green_count <= 1:
#                 total += 5  # increment -> total = total + 5
#             print(f"You have just earned 5 points!\nTotal points: {total}")
#
#         elif alien_color.lower() == 'red':
#             if total >= 1:
#                 total -= 1
#                 print(f"1 point was deducted.\nTotal points: {total}")
#             else:
#                 print(f"Total points: {total}")
#         else:
#             print(f"No points earned. Try Again!\nTotal points: {total}")

################################

while True:
    age = input(' Enter you age to check the ticket price ')
    if age.lower() == 'quit':
        print(f'breaking point')
        break
    elif not age.isdigit():
        print(f'only positive numbers accepted. Try Again')
        continue
    if age == 0:
        print('Breaking the loop')
        break
    age = int(age)



    if 0 < age <= 3:
        print('Your ticket is free baby')
    elif 3 < age <= 12:
        print(f"Ticket price is #10")
    elif age > 12:
        print(f'the ticket price is $15')
    else:
        print(f'Please enter valid age')
print(f'Completed the execution of {__file__}')