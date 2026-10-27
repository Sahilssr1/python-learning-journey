# Practice Set

# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "madad" : "Help",
    "kursi" : "Chair",
    "billi" : "Cat"
}

word = input("Enter the you want meaning of")
print(words[word])


# 2. Write a program to input eight numbers from the user and display all the unique numbers
# (once).

s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add("18")
print(s)

# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s)
print(len(s))  # len it give length size

# 5. s = {}
# What is the type of 's'?

s = {}
print(type(s))


# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

d = {} 
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)


# 7. If the names of 2 friends are same
# ; what will happen to the program in problem 6?

d = {} 
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})
print(d)


# 8. If languages of two friends are same; what will happen to the program in problem 6?

d = {} 
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)   #value can be same = lang , but key cannot be same = name 


# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}
# [1, 2]   # list → mutable ❌
# s = {8, 7, 12, "Harry", (1, 2)}
# print(s)  This works because tuples are immutable (unchangeable).

# Set + List     ❌
# Set + Tuple    ✅
# Set + String   ✅
# Set + Number   ✅


