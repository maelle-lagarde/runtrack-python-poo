class Forme:

    def aire(self):
        return 0

class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        aire = self.largeur * self.hauteur
        print("L'aire du rectangle est de", aire)

# instanciation de la classe Rectangle.
aire1 = Rectangle(14, 6).aire()

print(aire1)
