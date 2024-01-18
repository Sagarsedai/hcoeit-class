# Lists in python

"""
students = ["Ram","Shyam","Hari", "Surajan"]


count_of_students = len(students)

roll_count = roll.__len__()

print(count_of_students, roll_count)
"""

# List Operations

# List Declaration with no elements in it

# Looping In Python

roll = [1,2,3,4,5,6]

# For loop
# for i in roll:
#     print(i)

# True, False, None
# i = 0
# while(i <= 5):
#     print(i)
#     i += 1

students = [] 
students.append("Ram")

# Last Task
# WAP in such a way that
# when user enters input 'ram' as a name
# break loop and print the list
# otherwise keep on appending items to list 
# and ask for next input from terminal

name_list = ["adsad"]
while(name_list[-1] != "ram"):
    name_list.append(input("Enter your name: \n"))

print(name_list)



