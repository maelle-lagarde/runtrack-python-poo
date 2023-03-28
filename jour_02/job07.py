import random

class Carte:

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:

    def __init__(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]

    def melanger(self):
        random.shuffle(self.paquet)

    def donnerCarte(self):
        return self.paquet.pop(0)

class Main:

    def __init__(self):
        selft.cartes = []

    def ajouterCarte(self, carte):
        self.cartes.append(carte)

    def calculerPoints(self):
        total = 0
        nb_as = 0
        for carte in self.cartes:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            elif carte.valeur == "As":
                nb_as += 10
                total += 11
            else:
                total += int(carte.valeur)
        while nb_as > 0 and total > 21:
            total -= 10
            nb_as -= 1
        return total