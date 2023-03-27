class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

rectangle = Rectangle(10, 5)
print("La longueur initiale est", rectangle.getLongueur())
print("La largeur initiale est", rectangle.getLargeur())

rectangle.setLongueur(12)
rectangle.setLargeur(3)

print("La nouvelle longueur est", rectangle.getLongueur())
print("La nouvelle largeur est", rectangle.getLargeur())