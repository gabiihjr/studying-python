import math

print("Hello World")
print("*" * 10)
# Python Enhancement Proposals: PEPs
# Famous PEP: PEP 8 - Style Guide for Python Code https://www.python.org/dev/peps/

x = 1  # declaring a variable
y = 2
unit_price = 3

# Fundamentals of Python
# Python is a case sensitive language!

students_count = 1000
rating = 4.99  # float
is_published = True  # boolean
print(students_count)

message = """
Testing long message!
"""

# Strings
course = "Python Programming"  # string
course_length = len(course)  # string length count
print(course_length)

first_char_course = course[0]  # index 0
print(first_char_course)

last_char_course = course[-1]  # last index!
print(last_char_course)

three_char_course = course[0:3]  # first three characters of the string
print(three_char_course)

all_characters_course = course[0:]  # all characters starting from index 0
print(all_characters_course)

three_first_char = course[:3]  # first three characters starting from index 0
print(three_first_char)

copy_original_course = course[:]  # copy original string
print(copy_original_course)

# Escape Sequences
# \"
# \'
# \\
# \n - new line

# Formatted Strings

first_name = "Gabriela"
last_name = "Hermenegildo"
full_name = first_name + " " + last_name
full_name_formatted_str = f"{first_name} {last_name}"
print(full_name)
print(full_name_formatted_str)

# String methods
upper_case = course.upper()
lower_case = course.lower()
capitalize = course.title()
trim_whitespaces = course.strip()
find = course.find("Pro")
replace = course.replace("P", "J")
print("Pro" in course)  # present in the string - boolean
print("swift" not in course)  # not present in the string - boolean

# number
x = 1
x = 1.1
x = 1 + 2j  # a + bi

x = 10
x = x + 3
x += 3

# Working with numbers
round_number = round(2.9)  # rounds to 3
abs_number = abs(-2.9)  # returns the absolute value of a number
math.ceil(2.2)  # ceiling of a number (3)

# Type conversion
x = input("x: ")  # get input from a user
y = x + 1
int(x)
float(x)
bool(x)
str(x)
type(x)

y = int(x) + 1

# Falsy
# ""
# 0
# None
