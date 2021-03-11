import numpy, random, os

lr = 1 #Taux d'apprentissage : valeur qui détermine à quelle vitesse le réseau de neurones apprendra

bias = 1 #valeur +1 pour les neurones

weights = [random.random(),random.random(),random.random()] #Le poids crée une list (3 poids , pour 2 neurone et le bias)

def John(input1, input2, output):
   ReponseJ = input1*weights[0]+input2*weights[1]+bias*weights[2]
   #ReponseJ est la variable correspondant à la réponse donnée par John
   #Pour rappeler, input1 et input2 sont les 2 nombres que John évaluera pour tester ET sur ses deux nombres
   #output est la sortie attendue

   if ReponseJ > 0 : #Activation de la fonction Heaviside (elle ramène toutes les valeurs à exactement 0 ou 1)
      ReponseJ = 1
   else :
      ReponseJ = 0
   error = output - ReponseJ # l'erreur est utilisée pour réajuster les poids de toutes les connexions au neurone de sortie juste après.

   weights[0] += error * input1 * lr
   weights[1] += error * input2 * lr
   weights[2] += error * bias * lr

for i in range(50) :
   John(1,1,1) #True or true
   John(1,0,1) #True or false
   John(0,1,1) #False or true
   John(0,0,0) #False or false
#Partie d'apprentissage, c'est ici que John va s'entrainer et comprendre le résonement




print("Choissisez le premier nombre")
x = int(input())

print("Choissisez le deuxieme nombre")
y = int(input())


ReponseJ = x*weights[0] + y*weights[1] + bias*weights[2]
if ReponseJ > 0 : #activation function
   ReponseJ = 1
else :
   ReponseJ = 0

if x and y > 1:
   print("Ces nombres ne sont pas des nombres binaires")
   ReponseJ = 0

else:
   print(x, "ET", y, "sont : ", ReponseJ)


ReponseJ = 1/(1+numpy.exp(-ReponseJ)) #sigmoid function


"""
NumPy est une bibliothèque pour langage de programmation Python, destinée à manipuler des matrices ou tableaux multidimensionnels ainsi que des fonctions mathématiques opérant sur ces tableaux.

Le module os est un module fournit par Python dont le but d'interagir avec le système d'exploitation, il permet ainsi de gérer l'arborescence des fichiers, de fournir des informations sur le système d'exploitation processus, variables systèmes, ainsi que de nombreuses fonctionnalités du systèmes

"""










