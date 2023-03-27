class Operation:

    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def imprimer(self):
        print(f'Le nombre1 est {self.nombre1}.')
        print(f'Le nombre2 est {self.nombre2}.')

operation1 = Operation().imprimer()
print(operation1)

