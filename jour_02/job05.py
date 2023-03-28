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

class Cercle(Forme):

    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        aire = 3.14 * self.radius * self.radius
        print("L'aire du cercle est de", aire)

# instanciation de la classe Rectangle.
aire1 = Cercle(6).aire()
aire2 = Rectangle(14, 6).aire()

print(aire1)
print(aire2)