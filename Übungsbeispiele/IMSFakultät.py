
#Fakultät berechnen
import dis

def IMSfactorial(n):
    if n==1:
            return 1
    if n>1:
            return n*IMSfactorial(n-1)

result = IMSfactorial(4)

print (result)