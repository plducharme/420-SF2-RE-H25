class Animal:

    def bouger(self):
        print("Un animal qui bouge")

    def manger(self, nourriture):
        print(f"Un animal qui mange {nourriture}")


# Chien hérite de Animal
# La classe va hériter de tous les attributs (variables et méthodes) de la classe Animal
class Chien(Animal):

    def manger(self, nourriture):
        print(f"Un chien qui mange de la nourriture pour chien: {nourriture}")


# Oiseau hérite de Animal
# La classe va hériter de tous les attributs (variables et méthodes) de la classe Animal
class Oiseau(Animal):

    # Redéfinition du comportement de la méthode bouger(self) qui a été héritée
    def bouger(self):
        print("Un oiseau qui vole")


chien = Chien()
chien.bouger()
chien.manger("de la viande")

oiseau = Oiseau()
oiseau.bouger()
oiseau.manger("des graines")

