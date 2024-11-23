# Funktionale Programmierung des Pythagoras
# Problembeschreibung:
# Berechnung der Hypotenuse als Wurzel aus der Summe der beiden quadrierten Katheten

import math

def quadrat(kat):
    return kat*kat

def wurzel(base):
    return math.pow(base, 0.5)

def summe(sum1, sum2):
    return sum1 + sum2

def hypotenuse(kat1, kat2):
    hypotenuse = math.sqrt(kat1*kat1 + kat2*kat2)
    return hypotenuse

print(hypotenuse(3, 4))

print(wurzel(summe(quadrat(3), quadrat(4))))