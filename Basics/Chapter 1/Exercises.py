## do 2-6 from Python crash course page 29
from shlex import quote

from pyexpat.errors import messages

arist = 'quarke'
quote = ' dont touch my tra la la'
print (f'{arist} once said {quote} and there"s that')


##Data structure
##Create, access, read, modify(update), delete (CRUD operations)
## 1 CREATE LIST
students = []
engineers = ['umar','ahmad', 'hadidja','maryam']
numbers = [2,234,65,123,8]

#ACCESS THE DATA
## what is the index? index starts with 0 , index is not a count,
# last index is one less total count

print(f'\nthe forth element in the list is : {engineers[3].title()} ')
print(f'the first element in the list is : {engineers[0].title()}')
print(f'Sum of the first and last elements will be {numbers[0]+numbers[-1]}')
print (engineers)

##modify the list ['umar','ahmad', 'hadidja','maryam']

engineers[0] = ('atanas')
engineers.append('clasha') #adds to th elist
print (engineers)
engineers.insert(2,'stosha',) ## insert the element in the required place
print(engineers)

print(f'Romove elements from the list {engineers}')
print('Romove elements using del function,by index')
del engineers [1]
print(engineers)
print('Romove elements using pop function,last element by the index')
removed_engineer=engineers.pop()
removed_engineer2=(engineers.pop(2))
print(engineers)
print('Romove elements using remove function,last element by the index')
engineers.remove('stosha')
print(engineers)
print(removed_engineer)
outcast_engineers = [removed_engineer,removed_engineer2]
print(outcast_engineers)
outcast_engineers.append('clasha')
print(outcast_engineers)
outcast_engineers.remove('clasha')
print(outcast_engineers)
print(f'index of clasha {outcast_engineers.index('clasha')}')
print('all indexes of clasha : ', outcast_engineers.index("clasha"))






