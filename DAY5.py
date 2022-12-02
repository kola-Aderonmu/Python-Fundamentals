'''
IF...ELSE


Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

'''
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ELIF >>saying if the previous condition is not True, then try this 
print("\n\n")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#ELSE  >> this captures any other condition that might be left

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#AND >>when both conditions are True
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#OR >>when atleast one condition is True

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#NESTED IF...>>having more than one "if" in an IF condition

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
# NOTE

a = 33
b = 200

if b > a:
  pass       # having an empty if statement like this, would raise an error without the pass statement


# WHILE LOOPS >>this executes a statement as long as the condition is True

i = 1
while i < 6:
  print(i)
  i += 1   #>>>print 1,2,3,4,5

# BREAK STATEMENT  >>the break statement can stop the condition even if its true

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
  
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# For Loops  >> This is used ot iterate over a sequence ( either a list, tuple ,dictionary,set or string)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  

#loop through a string 

for x in "banana":
      print(x)
      
      
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
      
        
