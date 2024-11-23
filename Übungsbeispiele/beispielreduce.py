from functools import reduce

def mult(x, y):
    print(("x=", x, " y=", y))
    return x*y

n = int(input("wie viele bakterien hast du: "))
fact = reduce(mult, range(1, n)) # zwischen 
print('Du hast bakterien gehabt, {} : jetzt hast du soviele {} ich glaube du wirst sterben'.format(n-1, fact))