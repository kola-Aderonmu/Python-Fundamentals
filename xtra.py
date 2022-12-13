'''
Extra Learning!

'''

#Python Lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.


def x(a): return a + 10


print(x(5))



x = lambda b : b - 5
print(x(50))

# Lambda function can take multiple argument


def x(a, b): return a * b


print(x(5, 6))
   
 
 
   
c = lambda l, k : l * k
print(c(2,5))   



def x(a, b, c): return a + b + c


print(x(5, 6, 2))



def myfunc(n):
      return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))




def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(2))


#CLASS

class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)




class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def myfunc(self):
         print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

'''
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

'''

class Person:
      def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

        def myfunc(abc):
         print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

        def myfunc(self):
         print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40  #>> Changing the value of age

print(p1.age)




