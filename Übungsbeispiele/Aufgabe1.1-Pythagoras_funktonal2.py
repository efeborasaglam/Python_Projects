# Funktionale Programmierung des Pythagoras
# Problembeschreibung:
# Berechnung der Hypotenuse als Wurzel aus der Summe der beiden quadrierten Katheten
# Daraus ergeben sich die folgenden Teilfunktionen:
# - summe() - Summe zweier Zahlen
# - quadrat() - Quadrat einer Zahl
# - power() - eine Zahl hoch eine andere Zahl
# - squareRoot() - die Quadratwurzel aus einer Zahl
# - hypotenuse() - Hauptfunktion zur Berechnung des übergeordneten Ergebnisses

def summe(sum1, sum2):
    return sum1+sum2

def power(base, exp):
    return base ** exp

def quadrat(x):
    return x*x

def squareRoot(x):
    return power(x, 0.5)

def hypotenuse(kat1, kat2):
    return squareRoot(summe(quadrat(kat1), quadrat(kat2)))

print(hypotenuse(3, 4))
    