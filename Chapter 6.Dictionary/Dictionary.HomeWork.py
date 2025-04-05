#H/W given a phrase, count each how many times easch letter was used
#H/W given a phrase, count each how many times vowels were used
# use dictionary ,for loop , if condition, setdefault()



phrase = input('воткни число или словО')
letter_count= {}

for char in phrase.lower() :
    if char in letter_count.keys():
        letter_count[char] += 1
    else:
        letter_count[char] =1


    # letter_count.setdefault(char,0)
    # letter_count[char] +=1
    print(letter_count)






