alien = {'color':'red'}
alien['points'] = 5
alien['weight']=60
alien['x_position'] = 25
alien['y_position'] = 0


print(alien)
alien['weight'] = 70
print(alien['weight'])

alien['speed'] = 'fast'
print(alien)

if alien['speed'] == 'slow':
    x_increment =1
elif alien['speed'] == 'medium':
    x_increment =2
else:
    x_increment=3
alien['x_position'] = alien['x_position'] + x_increment
print(f'New x-position : {alien['x_position']}')

del alien['weight']
print(alien)


preffered_coding_language = {
    'Jared' : 'C++',
    'Ruby' : 'Pascal',
    'Gregory' : 'JavaScript',
    'Xavier' : "c#",
    'Atom' : 'Python',
}

print(preffered_coding_language)
print(f'Xavier prefferes this language to code : {preffered_coding_language['Xavier'].title()}')
print(f'Sara"s preferred conding language is {preffered_coding_language['Ruby'].lower()} ')


known_people = {
    'First name':'Ali',
    'Last name' : 'Aliev',
    'Address' : 'Kara-Karaeva 13',
    'City' : 'makchachkala',
}
print(known_people)

frinds_numbers = {
    'Mahach' : 911,
    'Serg': 722,
    'Seluha' : 8294871290,
    'Majid' : 7359,
    'Batyr' : 2083,

}

print(frinds_numbers)
print(frinds_numbers['Seluha'
                     ''])