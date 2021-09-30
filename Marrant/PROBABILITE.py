#Probabilités
import random as rd


def Proba():
    L = []

    m = g = B = R = Y = X = A = 0
    C = 50
    while not len(L) == 1:
        A += 1
        for i in range(C):
            p = rd.randint(1,2)

            if p == 1:
                g += 1
                B += 1
                m = 0
                if not g == 0:
                    if Y < g:
                        Y = g

            else:
                g = 0
                R += 1
                m += 1
                if not m == 0:
                    if X < m:
                        X = m

        if Y > 20:
            L.append(Y)

        if X > 20:
            L.append(X)
    print(L)

    print("Sur "+str(C)+" cartes, " +str(R) +" sont Rouges")
    print("Sur "+str(C)+" cartes, " +str(B) +" sont Noires")
    print("Il y a eu " + str(Y) + " Cartes Rouges qui ont été tirés à la suite")
    print(" soit une probabilité de "+ str(((1/(2**Y))*100)) + " %")
    print("Il y a eu " + str(X) + " Cartes Noires qui ont été tirés à la suite")
    print(" soit une probabilité de "+ str(((1/(2**X))*100)) + " %")
    print("Il y a eu "+str(A)+" Avant d obtenir cette probabilité")

Proba()



