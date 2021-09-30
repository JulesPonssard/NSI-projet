# -*- coding: utf-8 -*-

import time


def triSelection(a) :
    n = len(a)
    for i in range(n) :
        k =i
        for j in range(i+1,n) :
            if a[k] > a[j] : k = j
            a[k],a[i] = a[i],a[k]




def creer_liste(f): #création d'une liste

    liste = f.readlines()
    liste2=[]
    for i in range(0,len(liste)):
        liste2.append(int(liste[i]))
    return(liste2)

#Prog principal

t=[]
somme=0

for i in range(0,100):
    f = open('Valeursscncf3000.txt','r')
    lignes=creer_liste(f)
    f.close()
    start_time = time.time()
    triSelection(lignes)
    t.insert(i,(time.time()-start_time))
    somme= somme+t[i]


tempsmoyen = somme/100
#print (t)
print("Temps moyen d'exécution (s)= ",tempsmoyen)
