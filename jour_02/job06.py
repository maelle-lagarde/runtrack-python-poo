class Vehicule:

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Portes :", self.portes)
        print("Année :", self.annee)
        print("Prix :", self.prix)

class Moto(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)
        print("Nombre de roue :", self.roue)

    def demarrer(self):
        print("Attention, je roule frère!")

# instanciation de la classe Véhicule.
vehicule1 = Vehicule("Audi", "A1", "2000", "45 000€")
vehicule2 = Voiture("Mercedes", "Classe A", "2020", "18 500€")
moto = Moto("Vespa", "Primavera", "2020", "4000€")

vehicule1.informationsVehicule()
vehicule2.informationsVehicule()
vehicule2.demarrer()

moto.informationsVehicule()
moto.demarrer()