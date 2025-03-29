from operator import truediv
from traceback import print_tb

network_coverage = 1
if network_coverage == 1:
    print("I can make and receive calls")
else:
    print("nah I cant make or receive a call")
weather = 'tornado'
if weather == 'sunny':
    print ('I probaly can go for a walk')
else:
    print('you should stay home for now')

wage = 75
work_remotely = True

if wage>70 and work_remotely == True:
    print('I should give it a go and apply for a job')
else:
    print('Do some more research and study')

job_description = ['QA','QA Analyst',"QA Engineer","Senior QA Analyst",'Burger_king flipper']
if 'Burger_king flipper' in job_description:
    print('Do better and learn Python')

score = 10
if score + 17 > 20:
    print("you scored more then 20 points ansd here's your pay rise")
else: print("you scored less then 20 points adn you're are fired")
