friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)

friends.append("Harry")
print(friends)


l1 = [1, 8, 7, 2, 21, 15]

# 1. append()
l1.append(10)
# use: add an item at the end
# output: [1, 8, 7, 2, 21, 15, 10]


# 2. insert()
l1.insert(2, "Sahil")
# use: add an item at a specific index
# output: [1, 8, "Sahil", 7, 2, 21, 15]


# 3. remove()
l1.remove(7)
# use: remove a specific VALUE
# output: [1, 8, 2, 21, 15]


# 4. pop()
l1.pop(2)
# use: remove an item using INDEX
# output: [1, 8, 2, 21, 15]


# 5. sort()
l1.sort()
# use: arrange items in ascending order
# output: [1, 2, 7, 8, 15, 21]


# 6. reverse()
l1.reverse()
# use: reverse the list
# output: [15, 21, 2, 7, 8, 1]


# 7. index()
l1.index(7)
# use: find the index of a value
# output: 2


# 8. count()
l1.count(7)
# use: count how many times a value appears
# output: 1


# 9. extend()
l1.extend([30, 40])
# use: add multiple items to the end
# output: [1, 8, 7, 2, 21, 15, 30, 40]


# 10. copy()
l2 = l1.copy()
# use: create a copy of the list


# 11. clear()
l1.clear()
# use: remove all items from the list
# output: []