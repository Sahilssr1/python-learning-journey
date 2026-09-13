# Practice Set
# 1. Write a program to store seven Marks in a list entered by the user.
Marks = []

f1 = int(input)("Enter Marks here: ")
Marks.append(f1)
f2 = int(input)("Enter Marks here: ")
Marks.append(f2)
f3 = int(input)("Enter Marks here: ")
Marks.append(f3)
f4 = int(input)("Enter Marks here: ")
Marks.append(f4)
f5 = int(input)("Enter Marks here: ")
Marks.append(f5)
print(Marks)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

Marks = []

f1 = int(input("Enter Marks here: "))
Marks.append(f1)
f2 = int(input("Enter Marks here: "))
Marks.append(f2)
f3 = int(input("Enter Marks here: "))
Marks.append(f3)
f4 = int(input("Enter Marks here: "))
Marks.append(f4)
f5 = int(input("Enter Marks here: "))
Marks.append(f5)
Marks.sort()
print(Marks)


# 3. Check that a tuple  cannot be changed in python.

a = (34, 234, "Harry")
a[2] = " larry"

# 4. Write a program to sum a list with 4 numbers.

l =(10,20,50,400)

print(sum(l))

# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)


a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)
