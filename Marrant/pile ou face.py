#Pile ou face
import random
P = 0
F = 0
z = 50
for i in range(z):
    x = random.randint(1,2)
    if x == 1:
        P += 1
        ecart = abs(0.5 - P/z)
    else:
        F += 1

print("Il y a eu "+str(z)+' lancés')
print("La pièce est tomber "+str(F)+' fois sur Face')
print(ecart)
print("Il y a "+str(F/z*100)+' % de chance que la piece tombe sur Face')
print("La pièce est tomber "+str(P)+' fois sur Pile')
print("Il y a "+str(P/z*100)+' % de chance que la piece tombe sur Pile')



#924
import random
d = 0
resultat = []
z = 100
for i in range(z):
    d = random.randint(1,6)
    resultat.append(d)
print(resultat)
print("il y a eu "+str(resultat.count(1))+' 1')
print("il y a eu "+str(resultat.count(2))+' 2')
print("il y a eu "+str(resultat.count(3))+' 3')
print("il y a eu "+str(resultat.count(4))+' 4')
print("il y a eu "+str(resultat.count(5))+' 5')
print("il y a eu "+str(resultat.count(6))+' 6')













