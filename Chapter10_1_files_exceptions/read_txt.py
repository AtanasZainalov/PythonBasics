print('READING')
real_path= 'data/flavors.txt'
with open('data/flavors.txt') as  file_obj:
    contents = file_obj.read().strip().upper()

print('Reading the file as a whole')
print(contents)
print("_________________________")
print("Reading the file line by line")
with open('data/flavors.txt') as  file_obj:
    for line in file_obj:
        print(line.strip())

new_flavors = ["\ncrocodile_tears","\nhappiness","\ngenuinejoy"]
with open(real_path,'a') as file_obj:
    file_obj.write("\ncrocodile_tears")
    file_obj.write("\nhappiness")
    file_obj.write("\ngenuinejoy")

    for flavor in new_flavors:
        file_obj.appemd


"""for flavor in flavors:
    print(f'we have {flavor} ice-scream')"""

