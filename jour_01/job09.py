class Student:

    def __init__(self, nom, prenom, numstudent):
        self.__nom = nom
        self.__prenom = prenom
        self.__numstudent = numstudent
        self.__nbcredits = 0
        self.__level = self.__studentEval()

    def setNom(self, nom):
        self.__nom = nom
        return self.__nom

    def setPrenom(self, prenom):
        self.__prenom = prenom
        return self.__prenom

    def setNbcredits(self, nbcredits):
        self.__nbcredits = nbcredits
        return self.__nbcredits

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getNbcredits(self):
        return self.__nbcredits

    def add_credits(self, nombre):
        if nombre >= 0:
            self.__nbcredits = int(nombre)
            return self.__nbcredits
        else:
            print("Le nombre doit être un entier positif.")

    def __studentEval(self):
        if self.__nbcredits >= 90:
            return "Excellent"
        elif self.__nbcredits >= 80:
            return "Très bien"
        elif self.__nbcredits >= 70:
            return "Bien"
        elif self.__nbcredits >= 60:
            return "Passable"
        elif self.__nbcredits < 60:
            return "Insuffisant"
        else:
            return False

    def studentInfo(self):
        student = Student("Doe", "John", 145)
        print("Nom =", student.getNom())
        print("Prénom =", student.getPrenom())
        print("Id =", self.__numstudent)
        print("Niveau =", self.__level)

student = Student("Doe", "John", 145)
print("Le nombre de crédits de", student.getPrenom(), student.getNom(), "est de", student.add_credits(30), "points.")

print(student.studentInfo())