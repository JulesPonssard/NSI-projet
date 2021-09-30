# -*- coding: utf-8 -*-
import time

def qsort(u):
    '''Quick-Sort : Algo du tri rapide'''
    if u == []: return []
    pivot, g, d = u[0], [], []
    for x in u[1:]: g.append(x) if x<pivot else d.append(x)
    return qsort(g)+[u[0]]+qsort(d)



def creer_liste(f): #créer une liste
    liste = f.readlines() #creer liste
    liste2=[]

    for i in range(0,len(liste)):
        liste2.append(int(liste[i]))
    return(liste2)





t=[]

somme=0




for i in range(0,100):
    f = open('Valeursscncf3000.txt','r')
    lignes=creer_liste(f)
    f.close()
    start_time = time.time()
    qsort(lignes)
    t.insert(i,(time.time()-start_time))
    somme= somme+t[i]


tempsmoyen = somme/100
#print (t)
print("Temps moyen d'exécution (s)= ",tempsmoyen)




