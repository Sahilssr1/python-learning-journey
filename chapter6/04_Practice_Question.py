# Practice Set


# 1. Write a program to find the greatest of four numbers entered by the user.

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))


# # Use Python's built-in max() function to instantly pinpoint the largest value
# greatest = max(a1, a2, a3, a4)
# print("Greater number is:", greatest)

# if(a1 > a2 and a1 > a3 and a1 > a4 ):
#     print("Greated number is a1: ", a1)
# elif(a2 > a1 and a2 > a3 and a2 > a4 ):
#     print("Greatest number is a2: ", a2)
# elif(a3 > a1 and a3 > a2 and a3 > a4 ):
#     print("Greatest number is a3: ", a3)
# else:
#      print("Greatest number is a4: ", a4)








# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

# sub1 = int(input("Enter Marks 1: "))
# sub2 = int(input("Enter Marks 2: "))
# sub3 = int(input("Enter Marks 3: "))

# #check for total percentage 
# total_percentage = (100*(sub1 + sub2 + sub3)) /300

# if(total_percentage >= 40 and sub1>=33 and sub2>=33 and sub3>=33):
#     print("You are pass")

# else:
#  print("Try next year:", total_percentage, "%")

# 3. A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# p1 ="Make a lot of money"
# p2 = "buy now"
# p3 =  "subscribe this"
# p4 = "click this"

# message = input("Enter your comment: ")

# if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
#    print("This comment is a spam")

# else:
#    print("This coomment is not spam")



# 4. Write a program to find whether a given username contains less than 10 characters or not.

# username = input("Enter a username: ")

# if(len(username) < 10):
#     print("Your username contain less than 10 character")
# else: 
#     print("Your username contain more than 10 character")
    

# 5. Write a program which finds out whether a given name is present in a list or not.

# l = ["Sahil", "Rohan", "Aman", "Ravi"]

# name = input("Enter your name: ")

# if(name in l):
#     print("Your name is in the list")

# else:
#     print("Your name is not in the list")


# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter your marks: "))

# if marks <= 100 and marks >= 90:
#     grade = "EX"
# elif marks < 90 and marks >= 80:
#     grade = "A"
# elif marks < 80 and marks >= 70:
#     grade = "B"
# elif marks < 70 and marks >= 60:
#     grade = "C"
# elif marks < 60 and marks >= 50:
#     grade = "D"
# elif marks < 50:
#     grade = "F"

# print("Your Grade is:", grade)
    
    

# 7. Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enterr the post: ")

if("sahil" in post.lower()):
    print("this post is taking about sahil")

else:
    print("this post is not taking about sahil")
