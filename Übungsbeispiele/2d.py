# Beispiel: Pure Functions
# Score-Verwaltung für ein Spiel
# --> Globale Variable currentUser verwendet
# --> Struktur users ist ebenfalls global
# --> currentUsre als Parameter f. Update-Funktionen
# --> ID- name ist nicht eindeutig



currentUser = 0

users = [{"name" : "Holger", "score" : 30, "tries" : 1},            # Datenstruktur users ist global, aber zentrale Datenstruktur
         {"name" : "Verena", "score" : 110, "tries" : 4},           # Es ist zu beachten, dass hier die Namen als Id's nicht eindeutig sind!
         {"name" : "Peter", "score" : 80, "tries" :3}]              # Hier wäre eine numerische Id oder ein anderer eindeutiger Identifier sicher besser!
  
print()

def updateScore(newScore):
    users[currentUser]["score"] += newScore

def returnUsers():
    return users

def updateTries():
    users[currentUser]["tries"] += 1

def updateUsers(newUser):
    global currentUser
    currentUser = newUser

print(returnUsers())
updateScore(300)
print(returnUsers())
updateUsers(2)
updateTries()
print(returnUsers())