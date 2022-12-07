# def my_info(Fname, Lname):
# 	print("Your first name is " + Fname, "and your second name is " + Lname)
 

# print("Kindly, enter your Full name ")
# Fname = x = input("Fistname: ")
# Lname = y = input("Lastname: ")
    
# my_info(x, y)    
# #second method
# print("\n\n")




# def names(x, y):
#     print("Your first name is " + x, "and your Surname is " + y, "therefore, I will call you ", x, y)
    
# x = input("Fistname: ")
# y = input("Surname: ")
# names(x, y)

def my_info():
    name = input("Input your first name and last name: ")
    name_list = name.split()
    
    if len(name_list) > 1:  
        first_name = name_list[0]
        second_name = name_list[-1]
        
        return f"Your first name is {first_name},and your Surname is {second_name} therefore, I will call you "+ first_name + " " + second_name
        
    else:
        return f"Your first name is {name_list[0]}"
    
# info = my_info()
# print(info)


def decorator(function):
    def inner(*args):
        print("hello")
        returned_val = function(*args)
        print(returned_val)
        # return returned_val

    return inner

@decorator
def sum(a, b):
    return a+b

print(sum(2,4))
sum(2,3)