import math

a = 1
b = 2

def langeSeite():
    a = int(input("Gib erste kurze Seite : "))
    b = int(input("Gib zweite kurze Seite: "))
    c = math.sqrt(a * a + b*b)
    return(c)

def kurzeSeite():
    a = int(input("Gib kurze Seite : "))
    c = int(input("Gib lange Seite : "))
    b = math.sqrt(c*c - a*a)
    return(b)
    
def Auswahl():
    ausw = int(input("Wähle: 1 für lange Seite berechnen, 2 für kurze Seite berechnen: "))
    if ausw == 1:
        return langeSeite()
    elif ausw == 2:
        return kurzeSeite()
    else:
        return "Ungültige Auswahl. Bitte wähle 1 oder 2."

print("Ergebnis: ",Auswahl())