class Personne:

    def __init__(self, age):
        self.age = 14

    def afficherAge(self):
        return self.age

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):

    # métode publique.
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai ", self.age, "ans.")

class Professeur:

    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee

    # métode publique.
    def enseigner(self):
        print("Le cours va commencer")

# instanciation personne et élève.
personne1 = Personne(14)
eleve1 = Eleve(14)

eleve1.affichageAge()