
#--------DAY 2-------
#STRING
# A string is an array of characters.
#STRING SLICING-----This is the use of a state bracket [start:end:step]
#example:
#    mystrng = "I love chicken!"
#    print(mystrng[1:6]) ----it excludes the main terminating point.
#>>>love
#example 2
#splitted_val = mystring.split()
#print(splitted_val)
#mystrng = "I love chicken!"
#splitted_val = mystring.split()
#print(splitted_val)
#splitted_val = mystring.split()
#string Mthods
# capitalize()---just the first letter
# upper---caps all
# casefold() --changes to small caps all
# center()----
# find()----search the string for a specific value, returns the the first occurances of
#
#
#DATA TYPE COVERSION--TYPECASTING
#Convertig one datatype into another data type in order to convert for an ops
# int, float and str
# you cant convert str t int
#------READ ON ASCII IN PYTHON--------
# integer = 34
#string = int(integer)
#5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
# integer = 33
#print(integer *2) --normall arithematics
#integer = 33
#string = str(integer) ----"33"
#print(string)---------"33"
#print (integer *4) ---33333333
#-----ASSIGNMENT------
#Decimal points in python, using deciamal points
#write a string that is iterable
fruit = 'banana'
x = '*'.join(fruit.split('a'))
print(x)

fruit = 'banana'
print(fruit.find('na'))


names = 'Adekola*Hashim*Kabirat*Idris*Micheal'
x = names.split('*')
print(x)
friends = ", ".join(x)

names = 'Adekola*Hashim*Kabirat*Idris*Micheal'
friends = names.replace("*", ", ")
print(friends)

print(friends)


me = "cricket"
you = "football"
them = "hockey"
string = " ".join([me, you, them])
print(string)


char = "I love cooking"
cat = char[:6]  # --print 'i love'
print(cat)

for i in cat:
    print(i)

print(len(cat))

print(char + ' ' + cat)  # --concantenate

#WHY USE TAB AND SPACE
#if youre using a Spaces , memory is allocated 4 times while if you use TAB, memeroy is just allocated once compared to spaces.

#assignment
#Get an essay and get 10 words from it. pick from any start position you wish.

essay = "It is not the critic who counts, not the man who points out how the strong man stumbled, or where the doer of deeds could have done better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood, who strives valiantly, who errs and comes short again and again, who knows the great enthusiasms, the great devotions, and spends himself in a worthy cause, who at best knows achievement and who at the worst if he fails at least fails while daring greatly so that his place shall never be with those cold and timid souls who know neither victory nor defeat."

jug = essay.split("*")

print(jug)
print("CHECK THIS:\n")
first = ' '.join(jug[:6])
print(first)

#Real answer
print("\n")
words = "It is not the critic who counts, not the man who points out how the strong man stumbled, or where the doer of deeds could have done better."
son = words.split()[:6]
print(son)
print('\n\n')

sons = "   ".join(son)
print(sons)
print("\n This is the whole sentence!")
print(words)

#To get the alphabets by character
words = "It is not the critic who counts, not the man who points out how the strong man stumbled, or where the doer of deeds could have done better."
for i in words:
    print(i)

print("\n\n", words[0:9])  # printing as words


'''
print("PRINT Just 10 words from the essay \n\n")
cup = jug
print(cup)
#print("THIS IS GOING TO PRINT JUST 10 WORDS FROM ESSAY" + " " + )
'''
