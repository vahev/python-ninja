# Creates a generator for numbers to the third power
def gencubes(n):
    for num in range(n):
        yield num**3


for x in gencubes(10):
    print(x)
# When: [a, b = b, a+b] statement is executed, the outcome will
# execute like:[ a = b; b = a + b] but simultaneously, neither the value of 'b'
# nor 'a' will change until during assignation phase
