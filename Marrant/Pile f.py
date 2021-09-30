class Pile:
    def __init__(self):
        self.data = []


    def empiler(self,element):
        self.data.append(element)

    def hauteur(self):
        return len(self.data)

    def est_vide(self):
        return self.hauteur() == 0

    def sommet(self):
        return self.data[-1]

    def depiler(self):
        return  self.data.pop()

L = Pile()

for i in range(10):
    Pile.empiler(L,i)
print(L.data)


#Exercice 1
def retourne(Piles):
    Q = Pile()
    while not Piles.est_vide():
        Carte = Piles.depiler()
        Q.empiler(Carte)
    print(Q.data)
    return Q

#retourne(L)
#Ne pas lançer tout les programmes en même tant

#Exercice 2

def Diviser(P):
    J = Pile()
    Q = Pile()
    while not P.est_vide():
        Carte = P.depiler()
        Q.empiler(Carte)
        Carte2 = P.depiler()
        J.empiler(Carte2)
    print(J.data)
    print(Q.data)
    return Q,J

Diviser(L)


#Exercice 3

I = Pile()
I.data = [0,1,2,3,4,5]
U = Pile()
U.data = [6,7,8,9,10,11]

def Fusion(P1, P2):
    Fusion = Pile()
    while not P1.est_vide():
        Carte1 = P1.depiler()
        Fusion.empiler(Carte1)
        Carte2 = P2.depiler()
        Fusion.empiler(Carte2)
    print(Fusion.data)
    return Fusion

Fusion(I,U)


#Exercice 4
import random

I = Pile()
I.data = [0,1,2,3,4,5]
U = Pile()
U.data = [6,7,8,9,10,11]

def Melange_Americain(P1,P2):
    MA = Pile()
    while not P1.est_vide():
        a = random.randint(1,2)
        if not P2.est_vide():
            if a == 1:
                Carte1 = P1.depiler()
                MA.empiler(Carte1)
                Carte2 = P2.depiler()
                MA.empiler(Carte2)
            if a == 2:
                Carte1 = P1.depiler()
                MA.empiler(Carte1)
                Carte2 = P2.depiler()
                MA.empiler(Carte2)
                Carte2 = P2.depiler()
                MA.empiler(Carte2)
        else:
            Carte1 = P1.depiler()
            Pile.empiler(MA,Carte1)
    print(MA.data)
    return MA

Melange_Americain(I,U)








