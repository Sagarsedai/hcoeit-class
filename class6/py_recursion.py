# recursive function in python 


# Calculating the factorial of x where x >= 1

def factorial_func(x):
    # isinstance => 
    if not isinstance(x , int):
        return "Illegal value provided"
    if x < 1 :
        return 'Value cannot be less than 1'
    if x == 1:
        return 1
    else:
        print(f"Value in this iteration is : {x} * {x-1}")
        return x * factorial_func(x - 1)

# ret1 = factorial_func("abc")
# ret2 = factorial_func(0)
# ret3 = factorial_func(-1)
ret4 = factorial_func(5)

# print(f"First Call Returned : {ret1}")
# print(f"Second Call Returned : {ret2}")
# print(f"Third Call Returned : {ret3}")
print(f"Last Call Returned : {ret4}")

#  factorial_func(5)
# 5 * factorial_func(4)
# 5 * 4 * factorial_func(3)
# 5 * 4 * 3 * factorial_func(2)
# 5 * 4 * 3 * 2 * factorial_func(1)
# 5 * 4 * 3 * 2 * 1