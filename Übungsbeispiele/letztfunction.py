from functools import reduce

def mult(x, y):
    print(("x=", x, " y=", y))
    return x*y

n = 6
fact = reduce(mult, range(1, n)) # zwischen 
print('Factorial of {} : {}'.format(n-1, fact))
