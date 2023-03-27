class Personne:

    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        return "Je suis " + self.prenom + " " + self.nom + "."

personne1 = Personne('John', 'Doe').sePresenter()
personne2 = Personne('Jean', 'Dupond').sePresenter()
print(personne1)
print(personne2)