# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

fact_func = lambda n : n * fact_func(n-1) if n > 1  else 1
# breakpoint()

# def fact_func(n):
#     return n + fact_func(n-1)

# exception handling
# import math as mth


try:
    print("Trying to execute value")
    ret = fact_func("5")
    print(ret)

except Exception as e:
    # pass
    print("Exception occurred")
    print(f"Exception detail : \n {e.args}")
finally:
    # 
    print("Function exe comp")



