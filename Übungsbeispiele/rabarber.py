a = 3
b = 5

liste = [1,23,44,7,12]

def sum(x, y):
    x = x+y
    return x


def replace(l):
    l[0] = 0 # überschreibt den 0 also den ersten zahl mit 0
    return l

# Beispiel call by Value
print(sum(a,b))
print(a,b)

# Beispiel call by Reference
print(replace(liste))
print(liste)