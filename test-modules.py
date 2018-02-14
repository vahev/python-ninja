from modules.hellomodule import helloWorld
from functools import reduce

# The use of a created module
helloWorld()


def fahrenheit(T):
    """ Function for converting to Fahrenheit degrees using map

    """
    return (9.0/5)*T + 32


temp = [0, 22.5, 40, 100]
map(fahrenheit, temp)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
# Making a sum of array elements using Map function
map(lambda x, y, z: x + y + z, a, b, c)

# Finding the max value of a List using Reduce function
reduce(lambda a, b: a if a > b else b)


# This is a decorator Function
def new_decorator(func):

    def wrap_func():
        print('code here, before executing the func')

        func()

        print('Code here will execute after the func')

    return wrap_func


@new_decorator
def func_needs_decorator():  # The function that needs the new_decorator
    print('This function needs a decorator')


func_needs_decorator = new_decorator(func_needs_decorator)
# Making the above is the same as: using @new_decorator
