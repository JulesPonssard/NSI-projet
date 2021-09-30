import random

class labyrinthe:

    #Création du labyrinthe
    tableau = \
    [[1, 1, 1, 1, 1, 1, 1, 1, 8, 1], \
    [1, 2, 1, 0, 1, 0, 0, 1, 0, 1], \
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1], \
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], \
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1], \
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1], \
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1], \
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1], \
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1], \
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], \
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], \
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]] \




#Méthode pour afficher le labyrinthe en ligne et colonne
def PrintT(T):
    for ii in T:
        print(ii)




class joueur:

    #Création du Joueur et de ses attributs
    def __init__(self):
        self.values = 2
        self.nom = "Alix"
        self.posColonne = 1
        self.posLigne = 1

    #Création du méthode permettant de faire descendre d'une case le Joueur
    def moveDOWN(self):

            #Gestion des collisions avec les murs (1)
            if not labyrinthe.tableau[self.posColonne + 1][self.posLigne] == 1 or labyrinthe.tableau[self.posColonne + 1][self.posLigne] == 7 :

                labyrinthe.tableau[self.posColonne + 1][self.posLigne] =  labyrinthe.tableau[self.posColonne][self.posLigne]
                self.posColonne = self.posColonne + 1
                #Permet de mettre la position du Joueur avant le déplacement = 0
                labyrinthe.tableau[self.posColonne - 1][self.posLigne] = 0
                PrintT(labyrinthe.tableau)

            else:
                print("non")

    # Création du méthode permettant d'aller à droite d'une case le Joueur
    def moveRIGHT(self):
            if not labyrinthe.tableau[self.posColonne][self.posLigne + 1] == 1:
                labyrinthe.tableau[self.posColonne][self.posLigne + 1] = labyrinthe.tableau[self.posColonne][self.posLigne]
                self.posLigne = self.posLigne + 1
                labyrinthe.tableau[self.posColonne][self.posLigne - 1] = 0
                PrintT(labyrinthe.tableau)

            else:
                print("non")

    # Création du méthode permettant de monter d'une case le Joueur
    def moveUP(self):
            if not labyrinthe.tableau[self.posColonne - 1][self.posLigne] == 1:
                if labyrinthe.tableau[self.posColonne - 1][self.posLigne] == 8:

                    print("t'as gagné bgt")
                labyrinthe.tableau[self.posColonne - 1][self.posLigne] = labyrinthe.tableau[self.posColonne][self.posLigne]
                self.posColonne = self.posColonne - 1
                labyrinthe.tableau[self.posColonne + 1][self.posLigne] = 0
                PrintT(labyrinthe.tableau)

            else:
                print("non")

    # Création du méthode permettant d'aller à gauche d'une case le Joueur
    def moveLEFT(self):
            if not labyrinthe.tableau[self.posColonne][self.posLigne - 1] == 1:
                labyrinthe.tableau[self.posColonne][self.posLigne - 1] = labyrinthe.tableau[self.posColonne][self.posLigne]
                self.posLigne = self.posLigne - 1
                labyrinthe.tableau[self.posColonne][self.posLigne + 1] = 0
                PrintT(labyrinthe.tableau)

            else:
                print("non")

    # Création d'une méthode nous permettant de nous déplacer selon des touches prédéfinis selon une même fonction
    def Move(self,dir):
        if dir == "q":
            self.moveLEFT()
        elif dir == "d":
            self.moveRIGHT()
        elif dir == "s":
            self.moveDOWN()
        elif dir == "z":
            self.moveUP()







#Création d'une variable Joueur ayant les attributs de la class joueur()
Joueur = joueur()




PrintT(labyrinthe.tableau)



def auto():
    for i in range(2000):
        Mv = random.randint(0,3)
        v = 0
        v = v + i
        print(v)
        print(Mv)
        if Mv == 0:
            Joueur.Move("z")
        if Mv == 1:
            Joueur.Move("d")
        if Mv == 2:
            Joueur.Move("q")
        if Mv == 3:
            Joueur.Move("s")




