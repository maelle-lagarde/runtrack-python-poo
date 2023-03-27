class Voiture:

    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50

    def setMarque(self, marque):
        self.__marque = marque
        return self.__marque

    def setModele(self, modele):
        self.__modele = modele
        return self.__modele

    def setAnnee(self, annee):
        self.__annee = annee
        return self.__annee

    def setKm(self, km):
        self.__km = km
        return self.__km

    def setEn_marche(self, en_marche):
        self.__en_marche = en_marche

    def getMarque(self):
        return self.__marque

    def getModele(self):
        return self.__modele

    def getAnnee(self):
        return self.__annee

    def getKm(self):
        return self.__km

    def getEn_marche(self, en_marche):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            lets_go = self.__en_marche = True
            return lets_go
        else:
            return False

    def arreter(self):
        stop = self.__en_marche = False
        return stop

    def __verifier_plein(self):
        return self.__reservoir

voiture = Voiture("Audi", "A1", "2000", "17230")
print("\nLa marque :", voiture.getMarque(), "\nLe modèle :", voiture.getModele(), "\nL'année :", voiture.getAnnee(), "\nLes km :", voiture.getKm())
print("La voiture peut-elle démarrer ? :", voiture.demarrer())