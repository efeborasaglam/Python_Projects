def mal(x):
    def mal_x(y):
        return(x*y)
    return mal_x

malZwei = mal(2) # x
malDrei = mal(3)

print("5 mal Zwei gibt: ",malZwei(5)) # y
print("5 mal Drei gibt: ",malDrei(5))