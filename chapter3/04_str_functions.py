name = "Sahil"

print(len(name)) 
# use: get the length of the string
# output: 5


print(name.endswith("l")) 
# use: check whether the string ends with given character/text
# output: True


print(name.startswith("S")) 
# use: check whether the string starts with given character/text
# output: True


print(name.capitalize()) 
# use: capitalize the first letter
# output: Sahil


print(name.upper()) 
# use: convert all letters to uppercase
# output: SAHIL


print(name.lower()) 
# use: convert all letters to lowercase
# output: sahil


print(name.title()) 
# use: capitalize the first letter of each word
# output: Sahil


print(name.count("i")) 
# use: count how many times a character/text appears
# output: 1


print(name.find("h")) 
# use: find the index/position of given character
# output: 2


print(name.replace("Sahil", "Rahul")) 
# use: replace one text with another
# output: Rahul

# More important string functions
text = "  Hello World  "

print(text.strip())
# use: remove spaces from beginning and end
# output: Hello World


print(text.split())
# use: split string into a list
# output: ['Hello', 'World']


print(" ".join(["Hello", "World"]))
# use: join list elements into one string
# output: Hello World


print("Sahil".isalpha())
# use: check whether all characters are alphabets
# output: True


print("12345".isdigit())
# use: check whether all characters are digits
# output: True


print("Sahil123".isalnum())
# use: check whether characters contain only letters/numbers
# output: True


print("hello".islower())
# use: check whether all letters are lowercase
# output: True


print("HELLO".isupper())
# use: check whether all letters are uppercase
# output: True


# ⭐ The most important ones to learn first

# For your current Python chapter, focus on these first:

# len()          → length
# upper()        → uppercase
# lower()        → lowercase
# capitalize()   → first letter uppercase
# title()        → first letter of every word uppercase
# strip()        → remove spaces
# replace()      → replace text
# find()         → find position
# count()        → count occurrences
# startswith()   → check beginning
# endswith()     → check ending
# split()        → convert string into list
# join()         → join strings