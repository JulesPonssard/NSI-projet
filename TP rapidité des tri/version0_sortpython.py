import time





def creer_liste(f): #créer une liste

    liste = f.readlines() #creer liste

    liste2=[]

    for i in range(0,len(liste)):
        liste2.append(int(liste[i]))
    return(liste2)






t=[]

somme=0




for i in range(0,100):
    f = open('Valeursscncf2000.txt','r')
    lignes=creer_liste(f)
    f.close()
    start_time = time.time()
    lignes.sort()#quellle procédure de tri?
    t.insert(i,(time.time()-start_time))
    somme= somme+t[i]

#♥print(lignes)
tempsmoyen = somme/100
print (t)
print("Temps moyen d'exécution (s)= ",tempsmoyen)


