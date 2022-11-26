'''
SO bASICALLY, I WILL BE FOCUSING ON MORE DATA TYPES 

'''
# -----DICTIONARIES------

primary = {
    "red" : [255,0,1],
    "blue" : [0,56,20],
    "green" : [721,564,2],
    
}

print(primary)

print(primary["blue"])

square = {1:2, 2:6, 3:"error", 4:16,}
square[8] = 64
square[10] = 100

print(square)

primes = {1:4, 2:8, 3:12, 8:16,}
print(primes[2]) 


nums = {
    1:"one",
    2:"two",
    3:"three",
    
}

print(1 in nums)  #True
print(5 in nums) # False


pairs = {
    1:"fruits",
    "cranberry": [2,3,4],
    True:False,
    None:"True",
    
}
# to get a value in a key-value pair in python, you use square brackets and refer to the key in the pair
print(pairs["cranberry"])
print(pairs.get(1)) # NOTE that the value for 1 is default at True
print(pairs)


'''
TUPLES
'''
#items in tuple can not be changed because they are immutable

words = ("egg", "beans", "cake")
print(words[0])


message = "spam", "inbox", "outbox"
print(message[2])


#assign as packed
# this is called unpacking in a list

fruits = ("apple", "orange", "guava")
f1, f2, f3 = fruits

print(f1)
print(f2)
print(f3)

'''
LIST SLICING

sytax >> lower limit : upper limit : steps 
'''

market = [0,1,2,3,4,5,6,7,8,9,50.70,90]
print(market[2:6]) # give me the first 8 spaces but omit the first 2
print(market[::-1]) # prints the words reversely
print(market[3:8]) # give me the first 8 spaces but omit 3


#LIST COMPREHENSION

nums = [x**3 for x in range(10)]
print(nums) # so the result is a list of even number to 18(==0,2,4,6,8,10,12,14,16,18)

'''
STRING FORMATING 

'''
a = "{x},{y}".format(x=5, y=6)
print(a)  #>>>5,6

name = input()
age = int(input())

sent = ("{0} is {1} years old".format(name, age))
print(sent)



str = ("{c}, {b}, {f}". format(a=4, b=10, c=100))
print(str)



nums = [4,5,6,10,16]
msg = "numbers: {0} {3} {1}".format(nums)
print(msg)# give me the index of the value in the curly brace of the list [nums] >> 4,10,5
a
