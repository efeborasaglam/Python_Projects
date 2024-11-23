def mal(x):

    def mal_x(y):
        return(x*y)
    return mal_x


print("Lohn rechner")
print("_____________")
print()
Lohnsohn = mal(int(input("Schick dein Lohn mein Sohn: ")))
Lohntochter = mal(int(input("Schick dein Lohn meine Tochter: ")))

SohnMonat = int(input("Wie viele Monate hast du gearbeitet? (Sohn) : "))
TochterMonat = int(input("Wie viele Monate hast du gearbeitet? : (Tochter) : "))

print("Der Sohn wird so viel Geld verdienen wenn er  ",SohnMonat," Monate arbeitet: ",Lohnsohn(SohnMonat))
print("Die Tochter wird so viel Geld verdienen wenn sie  ",TochterMonat," Monate arbeitet: ",Lohntochter(TochterMonat))