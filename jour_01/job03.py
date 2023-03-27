class Operation:

    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def addition(self):
        return self.nombre1 + self.nombre2

    def imprimer(self):
        return(f'Le résultat est {self.addition()}.')

operation1 = Operation().imprimer()
print(operation1)
