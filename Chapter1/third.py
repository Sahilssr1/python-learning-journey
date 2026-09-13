# 3. Write a python program to print the contents of a directory using the os module. Search
# online for the function which does that

import os

# Specify the directory
directory = "."

# Get the contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)
