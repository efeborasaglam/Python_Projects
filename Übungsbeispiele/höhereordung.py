print(list(map(int, [2.3, 2.4, 5.4, 1.99, 4])))

def mal(x):
    def mal_x(y):
        return x * y
    return mal_x

def mult_liste(liste, faktor):
    mal_f = mal(faktor)
    return list(map(mal_f, liste)) # interative datenstruktur 

li = [10, 12, 3, 23, 4, 5, 11, 2]

print(mult_liste(li, 100))