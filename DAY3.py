"""
Methods available in the list class
___________________________________

"""

fruits = ['Apples', 'Mangoes', 'Oranges']

print(fruits)

fruits.append('Cashews')

print(fruits)

fruits.clear()

print(fruits)

x = fruits.copy()

print(x)
fruits = ['Apples', 'Mangoes', 'Oranges']

print(fruits.count('Apples'))

fruits.append('Apples')

print(fruits.count('Apples'))

people = ['Ahmad', 'Saad', 'Micheal', 'John']

students = ['Zara', 'Osofia', 'Hadiza']

print(people)
print(students)

students.extend(people)

print(students)

students.extend('cake')

print(students)

#Operation
list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_c = list_a + list_b

print(list_c)

list_d = [7, 8, 9]

list_d.extend(list_a)
list_d.extend(list_b)

print(list_d)

print(list_d[:4])


"""
Dictionary Methods
"""

# .get

database = {"user":
            {
                "name": "Adekola",
                "rank": "100",
                "class": 10,
                "title": "Mr."
            }
            }

print(database.get('user'))
print(database.get('user').get('name'))
print(database.get('user').get('rank'))
print(database.get('user').get('class'))
print(database.get('user').get('title'))

print("The user's name is "+database.get('user').get('title')+"" +
      database.get('user').get('name')+", his rank is "+database.get('user').get('rank'))
