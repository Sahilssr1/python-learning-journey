marks = {
    "Harry": 100,
    "sahil": 56,
    "Rohan": 23
}

# 1. items()
print(marks.items())
# use: get all key-value pairs
# output: dict_items([('Harry', 100), ('sahil', 56), ('Rohan', 23)])


# 2. keys()
print(marks.keys())
# use: get all keys
# output: dict_keys(['Harry', 'sahil', 'Rohan'])


# 3. values()
print(marks.values())
# use: get all values
# output: dict_values([100, 56, 23])


# 4. update()
marks.update({"sahil": 99})
# use: add a new key-value pair or update an existing value
# output: {'Harry': 100, 'sahil': 99, 'Rohan': 23}

print(marks)


# 5. get()
print(marks.get("sahil"))
# use: get the value of a key
# output: 99



marks = {
    "Harry": 100,
    "sahil": 56,
    "Rohan": 23
}


# 6. pop()
print(marks.pop("sahil"))
# use: remove a key and return its value
# output: 56

print(marks)
# output: {'Harry': 100, 'Rohan': 23}


# 7. popitem()
print(marks.popitem())
# use: remove and return the last key-value pair
# output: ('Rohan', 23)


# 8. setdefault()
marks.setdefault("Aman", 50)
# use: add a key with a default value if the key does not exist

print(marks)
# output: {'Harry': 100, 'sahil': 56, 'Aman': 50}


# 9. copy()
new_marks = marks.copy()
# use: create a copy of the dictionary

print(new_marks)


# 10. clear()
marks.clear()
# use: remove all key-value pairs

print(marks)
# output: {}