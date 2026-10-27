# 1. Write a python program to display a user entered name followed by Good Afternoon using
# input() function.
name = input("Enter your name: ")
print("Good Afternoon " + name)  #String concatenation
print(f"Good Afternoon, {name}" )  # f-string The f tells Python that {name} should be replaced with the value stored in name


# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Sahil").replace("<|Date|>", "09 Sep 2026"))



# 3. Write a program to detect double space in a string.

name = "sahil is a good boy"

print(name.find("  "))
# use: find the position of double space
# output: -1

# 4. Replace the double space from problem 3 with single spaces.
name = "sahil is a  good boy"
print(name.replace("  ", ' '))



# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry,\n this python course is nice.\n Thanks!"

print(letter)