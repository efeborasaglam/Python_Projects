# IMS - KSB 2023 - Modul 323
# SW1-Bsp1
# Imperative vs. Funktionale Programmierung
# bilden einer Summe zweier Variabeln


num1 = 2
num2 = 3

def sum1(n1, n2):       # deklarativ funktional - pure function - könte noch vereinfacht werden --> wie?
    s = n1 + n2
    return(s)


def sum2():             # imperativ - impure function
    global num1
    global num2
    
    num1 = num1 + num2
    
def sum3(num1, num2):   # deklarativ funktional - pure function --> Vereinfachung von sum1
    return(num1 + num2)
    
print("Ausgangswerte vor sum1: ", num1, num2)
print("Zwischenwerte nach sum1: ", sum1(num1, num2), num1, num2)

print(sum2())
print("Zwischenwwerte nach sum2: ", num1, num2)

num1 = sum3(num1,num2)
print("Zwischenwwerte nach sum3: ", num1, num2)
print(sum3(num1,num2))
print("Endwerte nach sum3: ", num1, num2)
