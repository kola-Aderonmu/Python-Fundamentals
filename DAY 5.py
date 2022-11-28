'''
Dictionaries
'''

Food = {
    "rice": [20, 10,],
    "beans": [40, 70,],

}
for x in Food:
    print(Food[x])
    
#print(Food["rice"])    

square = {1: 2, 2: 6, 3: "error", 4: 16, 8: 64, 10: 100, 16: 42,}


print(square[4])

print(square[10])

print(square)

pairs = {
    1: "fruits",
    "cranberry": [2, 3, 4],
    True: False,
    None: "True",

}
print(pairs.get(12345, "I cant find it in the dictionary"))
print(pairs[1])

