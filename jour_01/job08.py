class Livre:

    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = True

    def setTitre(self, titre):
        self.__titre = titre
        return self.__titre

    def setAuteur(self, auteur):
        self.__auteur = auteur
        return self.__auteur

    def setNbpages(self, nombre):
        if nombre >= 0:
            self.__nbpages = int(nombre)
            return self.__nbpages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def setDisponible(self, disponible):
        self.__disponible = disponible
        return self.__disponible

    def getTitre(self):
        return self.__titre

    def getAuteur(self):
        return self.__auteur

    def getNbpages(self):
        return self.__nbpages

    def getDisponible(self):
        return self.__disponible

    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False

    def emprunter(self):
        if self.verification() == True:
            return False
        else:
            return True

    def rendre(self):
        if self.emprunter() == True:
            return False
        else:
            return True

livre = Livre("Le Parfum", "Patrick Süskind", 359)
print("Le titres est", livre.getTitre())
print("L'auteur est", livre.getAuteur())
print("Le nombre de pages est de", livre.getNbpages())
print("Disponible : ", livre.verification())
print("Empruntable : ", livre.emprunter())
print("Rendre : ", livre.rendre())

livre.setDisponible(False)
print(livre.getDisponible())