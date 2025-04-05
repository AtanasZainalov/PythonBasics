#Unit Testing:
#age = 10  -> pass
#age 17 # -> pass
#age = 'abc' # -> fail typeError
age=16
#age=int(input("type in the age"))
if 75<= age >= 17:
    print("now you're yang adult and can get a driving permit")
elif 0<= age <17: print(f"no you're too yang for it,you need to wait {17-age} yars")
elif age > 75:
    print('Ohh Drive carefully or just get an uber /lift')
    print("make sure you renew your driver's license")
else: print('Please check the entry age, it is not valid')

# alien_color = 'green'
# alien_color = 'red'
# alien_color = 5
# alien_color = 'Green' # FAIL -> fix -> pass

total = 0
green_count = 0
for i in range(5):
    alien_color = input("Enter the color to earn points: ")

    if alien_color.upper() == 'GREEN':
        green_count += 1
        if green_count <= 1:
            total += 5  # increment -> total = total + 5
        print(f"You have just earned 5 points!\nTotal points: {total}")

    elif alien_color.lower() == 'red':
        if total >= 1:
            total -= 1
            print(f"1 point was deducted.\nTotal points: {total}")
        else:
            print(f"Total points: {total}")
    else:
        print(f"No points earned. Try Again!\nTotal points: {total}")
