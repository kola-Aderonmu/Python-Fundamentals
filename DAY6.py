a:int = 10
b = int(40)

print(a > b)


'''    
FUNCTIONS

*A function is a block of code which only runs when it is called.
*You can pass data, known as parameters, into a function.



FUNCTION---they take arguements...
Function will not be performed until they are called.
Function have "return types"
**Decorations

ARGUMENTS --are basically the value we pass into the brackets
PARAMETERS --these are fields provided






    
   '''
   
   



def my_function():
  print("Hello from a function")


def my_function(fname):
    print(fname + " is a good child")


my_function("David")
my_function("Tobias")
my_function("Isa")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Rolfman")


#If the number of arguments is unknown, add a * before the parameter name, so that This way the function will receive a tuple of arguments, and can access the items accordingly.

def my_cars(*salon):
    print("My favorite car is a : ", salon[2])


my_cars("Benz", "G-Wagon", "Toyota Camry 22", "Highlander 22", "Ford 22")


def my_cloth(*swags):
    print("I dress in ", swags[2], "every Saturday night")


my_cloth("shirt and pants", "Kaftan and P-Cap", "g-strings and bra", "pijamas")


#You can also send arguments with the [key = value]

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


def phoneTypes(phon1, phon2, phone3):
    print("The smart phone I would recommend to you is ", phon1, "and", phon2)


phoneTypes(
    phon1="Samsung",
    phon2="Nokia",
    phone3="Redmi"
)


#IF the number of keyword arguments is unknown, add a double ** before the parameter name

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def class_grade(**grade):
    print("Daniel had an ", grade["averg2"], " result in the last test.")


class_grade(averg1="Good", averg2="Excellent", averg="bad")


#Using the default parameter

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#RETURN VALUES  >>used if yoy want a result to be outputed

def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("\n\n\n\n")

'''
Assignment>>>

use the input function to get a user name, input the 2 names and then store in a two variable
then print out "Welcome your first name is ... and your last name is .....  "

all of this is to be inside a function...
you will just call it.
'''


'''
def my_info(Fname, Lname):
	print("Your first name is " + Fname, "and your second name is " + Lname)


print("Kindly, enter your Full name ")
Fname = x = input("Fistname: ")
Lname = y = input("Lastname: ")
    
my_info(x, y)    

#second method
print("\n\n")

def names(x, y):
    print("Your first name is " + x, "and your Surname is " + y, "therefore, I will call you ", x, y)
    

x = input("Fistname: ")
y = input("Surname: ")

names(x, y)

'''
print("\n\n")



#print(ads)

#3rd method

def cats(ads, ads1):
    print("Based on your input, your first name is ", ads, "and your surname is ", ads1)

j: str = input("Type in your first name: ")
k: str = input("Type in your surname: ")

list = j, k,
#print(list)
#print(type(list))


ads = list[0]
ads1 = list[1]
    
cats(ads, ads1)    
    


"""
CLASSES
    
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""


#To create a class, use the keyword class:

class MyClass:
    x = 5


print(MyClass)       #>>>_______  < class '__main__.MyClass' >





class MyClass:
      x = 5

p1 = MyClass()
print(p1.x)  #>>>5


'''
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

'''


class Person:
  def __init__(self, name, age, height, best_color):
    self.name = name
    self.age = age
    self.height = height
    self.color = best_color


p1 = Person("John", 36, 175, "green")

print(p1.name)
print(p1.age)
print(p1.height, "cm")
print(p1.color)
