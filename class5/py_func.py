# functions in python
# arguments to functions
# returns in function
# *args, **kwargs




# no args no return
def nn_name_printer():
    print("My name is don!") 
    # return "adds"

# single args no return
def sn_name_printer(name):
    print(f"My name is {name}!") 
    # return "adds"
# no args but return
def ns_name_printer():
    print("My name is default!") 
    return "My name is default!"

# single args  single return
def ss_name_printer(name):
    print(f"My name is {name}!") 
    return "My name is {name}!".format(name=name)


# Calling functions

# nn_name_printer()
# sn_name_printer("Aarpan Gautam")
# name  = ns_name_printer()

# print("Returned Name Is ",name)

"""
name  = ss_name_printer("Bishwo Mohan Shah")

print("Returned name is ", name)

"""

# Named arguments, default values to args

"""
def calculate_sum(a=0, b=0,c=0):
    return a+b+c


total_sum = calculate_sum(1,a=2)

print(total_sum)"""


"""
def display(*args, **kwargs):
    lw = kwargs.get("last_words")
    print(lw)
    return args[0], args[1]

print(display("My", "Name", last_words = "Don"))
"""

"""
WAP in python to find the sum of all numbers in a list using function.
Create a function in such that it accepts kwargs as a list of numbers,
calclate sum ,return the sum and print it.
"""

"""
numbers = [1,2,5,4,5,6,]



def sum_calc(*args, **kwargs):
    return sum( [ * list(args), * kwargs.get("nums") ] )

sum_of_nums = sum_calc(1,2,3,4,5, nums = numbers)

print(f"Sum of numbers given is : {sum_of_nums}")

"""


def args_kwargs_handler(*args, **kwargs):
    print("Args are",list(args))
    print("KwArgs are",kwargs)

args_kwargs_handler("Siddhartha","Kumar","Singh" ,surname = "Bajracharya", address = "Patan Dhoka")


# One Last
# WAP to merge two dict
# Pass a dict obj in args, and then n no of keyword arguments 
# Merge those two dictionaries and return it , print it



def args_kwargs_handler(*args, **kwargs):
    return {**args[0], **kwargs}

result = args_kwargs_handler(
        {"fname":"Siddhartha", "mname":"Kumar", "mmname":"Singh"},
        surname = "Bajracharya", 
        address = "Patan Dhoka"
    )

print(result)