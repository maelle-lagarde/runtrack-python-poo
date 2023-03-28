class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        perimetre = self.__longueur + self.__largeur + self.__longueur + self.__largeur
        print("Le périmètre du rectangle est de", perimetre)

    def surface(self):
        surface = self.__longueur * self.__largeur
        print("La surface du rectangle est de", surface)

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def getLongueur(self):
        return self.__longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def getLargeur(self):
        return self.__largeur

class Parallelepipede(Rectangle):

    def __init(self, hauteur):
        self.hauteur = hauteur

    def volume(self):
        return self.__longueur * self.__largeur * self.hauteur

# instanciation de la classe Rectangle.
perimetre1 = Rectangle(14, 6).perimetre()
surface1 = Rectangle(14, 6).surface()

print(perimetre1)
print(surface1)
