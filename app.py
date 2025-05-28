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
