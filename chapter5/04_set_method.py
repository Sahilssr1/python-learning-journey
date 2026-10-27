s = {1, 2, 3, 4}


# 1. add()
s.add(5)
# use: add one item to the set
# output: {1, 2, 3, 4, 5}


# 2. remove()
s.remove(5)
# use: remove a specific item
# output: {1, 2, 3, 4}
# note: gives an error if the item does not exist


# 3. discard()
s.discard(10)
# use: remove a specific item
# note: does NOT give an error if item doesn't exist


# 4. pop()
item = s.pop()
# use: remove and return an arbitrary item
# note: sets are unordered, so you don't know which item will be removed


# 5. clear()
s.clear()
# use: remove all items
# output: set()


# 6. update()
s = {1, 2, 3}
s.update({4, 5, 6})
# use: add multiple items
# output: {1, 2, 3, 4, 5, 6}



a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# 7. union()
print(a.union(b))
# use: combine both sets
# output: {1, 2, 3, 4, 5, 6}


# 8. intersection()
print(a.intersection(b))
# use: find common items
# output: {3, 4}


# 9. difference()
print(a.difference(b))
# use: items that are in a but NOT in b
# output: {1, 2}


# 10. symmetric_difference()
print(a.symmetric_difference(b))
# use: items that are NOT common
# output: {1, 2, 5, 6}


a = {1, 2, 3}
b = {1, 2, 3, 4, 5}


# 11. issubset()
print(a.issubset(b))
# use: check if all items of a are inside b
# output: True


# 12. issuperset()
print(b.issuperset(a))
# use: check if b contains all items of a
# output: True


# 13. isdisjoint()
c = {10, 20}
print(a.isdisjoint(c))
# use: check if two sets have NO common items
# output: True


# 🔥 Set Cheat Sheet
# Method	Use
# add()	Add one item
# remove()	Remove an item
# discard()	Remove an item without error
# pop()	Remove an arbitrary item
# clear()	Empty the set
# update()	Add multiple items
# union()	Combine sets
# intersection()	Find common items
# difference()	Find items only in first set
# symmetric_difference()	Find non-common items
# issubset()	Check if one set is inside another
# issuperset()	Check if one set contains another
# isdisjoint()	Check if sets have no common items