class Personne:

    def __init__(self, age):
        self.age = age

    def afficherAge(self):
        return self.age

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):

    # métode publique.
    def allerEnCours(self):
        print("Je vais en cours.")

    def affichageAge(self):
        print("J'ai ", self.age, "ans.")

class Professeur(Personne):

    def __init(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    # métode publique.
    def enseigner(self):
        print("Le cours va commencer.")

# instanciation personne et élève.
personne1 = Personne(14)
eleve1 = Eleve(14)
professeur1 = Professeur(40)

eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
professeur1.bonjour()
professeur1.enseigner()