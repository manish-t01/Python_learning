
# A string literal is any sequence of characters written inside:

# single quotes '...'
# double quotes "..."
# triple quotes '''...''' or """..."""
import math
name = "Shiv"
message = 'Hello World'
paragraph = """This is a multi-line string"""

first = "Manish"
last = "Thakur"

# Concatenation
fullname = first + " " + last  # I am using " " for space between to words.
print(fullname)

fullname += " ""!!"
print(fullname)


# casting a number to a string
decade = str(1980)
print(decade)
print(type(decade))

statement = "I like the rock music from" " " + decade + "s."
print(statement)

# Multilines
# multilines = '''

# Hey! How are u?

# I am good.

#              How do u do?

# '''

# print(multilines)
multilines = """

Hey! How are u?

I am good. 
  
             How do u do?
"""

print(multilines)

# string method
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multilines.title())
print(multilines.replace("good", "okay..."))
print(multilines)

# Adding white spaces
print(len(multilines))
multilines += "                                         "
multilines = "                " + multilines
print(len(multilines))
print("")

# Removing white spaces
print(len(multilines.strip()))  # removes white spaces
print(len(multilines.lstrip()))  # removes white spaces from  left side
print(len(multilines.rstrip()))  # removes white spaces from right side
print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("")
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Cake".ljust(16, ".") + "$4".rjust(4))
print("Butter tea".ljust(16, ".") + "$3".rjust(4))
print("Cheese Cake".ljust(16, ".") + "$5".rjust(4))
print("Cheese Bread".ljust(16, ".") + "$2".rjust(4))
print("")

# string index values
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
print(first[5])
print("")
print(first[-1])
print("")
print(first[0:])
print(first[1:])
print(first[2:])
print(first[3:])
print(first[4:])
print(first[5:])
print('')

# some methods return boolean data
print(first.startswith("M"))
print(first.endswith("k"))
print('')

# Numuric Data Types

# (1) integer data type
print("Working With Integer Data Type")
price = 100
best_price = int(90)
print(type(price))
print(isinstance(best_price, int))  # this is for cheaking
print('')

# (2) float data type
name = "working with float data type"
print(name.title())
cgpa = 8.35
my_cgpa = float(9.5)
print(type(cgpa))
print(isinstance(my_cgpa, float))
print("")

# (3) Complex Type ( mostly used in engneering )
name = "working with complex type"
print(name.title())
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print("")

# Built in functions for numbers
print(abs(cgpa))  # abs stands for absolute value.
print(abs(cgpa * -1))
print(round(cgpa))
print(round(cgpa, 1))  # it rounds to 1 place.
print('')

print(math.pi)
print(math.sqrt(25))
print(math.lcm(3, 5))
print(math.ceil(cgpa))
print(math.floor(cgpa))
print('')

# casting a string to a number.
pincode = "802152"
pin_value = int(802152)
print(type(pincode))
print(type(pin_value))
print("")

# Error if you attemp to cast incorrect data
pin_value = int("BIHIYA")  # put str in place of int the error will disapear.
