# Classe parente ou superclasse, sera couvert dans un cours ultérieur
class Legume:

    def __init__(self, nom, couleur):
        self._nom = nom
        self._couleur = couleur

# classe enfant ou sous-classe ou dérivée
class Fruit(Legume):

    def __init__(self, nom, couleur, poids):
        super().__init__(nom, couleur)
        self._poids = poids

    def afficher(self):
        print(self._nom + " " + self._couleur + " " + str(self._poids) + "g")

pomme = Fruit("Pomme", "rouge", 150)
# à éviter, lorsque la variable est protégée, on ne devrait pas y accéder directement, on devrait utiliser un accesseur
print(pomme._nom)

