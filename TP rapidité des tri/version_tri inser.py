import time

def insere(t, j):
    k = j
    while k > 0 and t[k] < t[k-1]:
        t[k-1], t[k] = t[k], t[k-1]
        k -= 1

def insertion_sort(t):
    for j in range(1, len(t)):
        insere(t, j)




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
    f = open('Valeursscncf2000.txt','r')
    lignes=creer_liste(f)
    #print(lignes)
    f.close()
    start_time = time.time()
    insertion_sort(lignes)
    #print (lignes)
    t.insert(i,(time.time()-start_time))
    somme= somme+t[i]



tempsmoyen = somme/100
#print (t)
print("Temps moyen d'exécution (s)= ",tempsmoyen)
