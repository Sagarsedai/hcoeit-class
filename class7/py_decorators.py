"""def make_pretty(func):

    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()"""


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()


"""
def decorator(func=None):
    def wrapper():
        print("Something is happening before the function is called.")
        if func:
            func()
        print("Something is happening after the function is called.")

    return wrapper


@decorator
def say_whee():
    print("Whee!")


decorator()
# say_whee()
"""
