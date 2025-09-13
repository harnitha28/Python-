fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("mango")
print(fruits)
fruits.extend(["orange", "kiwi"])
print(fruits)
fruits.insert(1, "grapes")  
print(fruits)
del fruits[3]  
print(fruits)
fruits.remove("kiwi")
print(fruits)
for item in fruits:
    print(item)
