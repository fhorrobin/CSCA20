"""
A program that takes a list of classes with marks in the format:
L = [['CSCA20', 'Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98'], ['CSCA08', 'Bob, 63, 95, 90', 'Joe, 80, 40', 'Rob, 98.5, 67, 95.5, 99']]

Where L is a list of lists of strings where the first item of each sublist is
the class name and the second item is strings containing the name and marks for
the students in the class.

We will use the functions to find a student's average mark for the class
as well as to get the average mark for the whole class.

We will use the function from ex4 to complete the program.
"""
from ex4 import *

CLASS_L = [['CSCA20', 'Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98'], ['CSCA08', 'Bob, 63, 95, 90', 'Joe, 80, 40', 'Rob, 98.5, 67, 95.5, 99']]


valid = False
# Repeat until valid entry is made
while not valid:

    # First get the input for what class we want to query
    class_code = input("Enter the code for the class: ")

    cls_count = 0

    # Iterate until we find class
    while (not valid) and cls_count < len(CLASS_L):
        # Check if the class is in this index
        if CLASS_L[cls_count][0] == class_code:
            valid = True
        else:
            # Remember to increment count
            cls_count += 1

    # If the class is not found then tell them to to enter another class
    if not valid:
        print("Class does not exist. Try again.")


# Now we have found the class
# We know that count represents position in list

# Split the class into a list of lists containing names and grades separately
# Only take [1:] to remove the course code
my_class = string_list(CLASS_L[cls_count][1:])

# Show the marks list
print("The class contains the following:\n", my_class)


# Get input of student name
# We verify the entry in the same way as above

valid = False

while not valid:
    student = input("Enter the name of a student: ")

    stu_index = 0
    while (not valid) and stu_index < len(my_class):
        # Check if the student is in this class
        if my_class[stu_index][0] == student:
            valid = True
        else:
            stu_index += 1

    if not valid:
        print("Student is not in class. Try again")

# Now we know which class and which student we want to work with.
# cls_count stores the index of class list
# stu_index stores the index of student in class list

# Copy the marks and names part of the class
CLASS = CLASS_L[cls_count][1:]

# Get the average for the student
string_avg_update(CLASS)
# List is now mutated
student_avg = CLASS[stu_index]


# Get the class average
class_avg = average(CLASS)


print("The student %s achieved average %d. The class average is %d." % (student, student_avg, class_avg))
