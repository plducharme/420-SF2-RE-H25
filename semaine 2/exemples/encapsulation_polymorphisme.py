# Ceci est un exemple plus complet d'encapsulation et de polymorphisme.
# On définit une classe Livre qui a trois attributs privés: titre, auteur et prix.
class Livre(object):
    def __init__(self, titre, auteur, prix: float):
        self.__titre = titre
        self.__auteur = auteur
        self.__prix = self.__valider_prix(prix)

    # On définit des méthodes pour accéder et modifier les attributs privés
    # getter et setter de style classique
    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_prix(self):
        return self.__prix

    def set_prix(self, prix):
        self.__prix = self.__valider_prix(prix)

    # Méthode privée pour valider le prix
    # Cette méthode privée est statique, car elle n'utilise pas d'attributs de l'objet ou de la classe
    # Cette notion sera vue dans un cours ultérieur
    @staticmethod
    def __valider_prix(self, prix):
        if prix < 0:
            raise ValueError("Le prix doit être positif")
        return prix

    # On redéfinit la méthode __str__ pour afficher les informations du livre
    # Cette méthode est héritée de la classe object
    def __str__(self):
        return f"{self.__titre} de {self.__auteur} coûte {self.__prix} $"

    # On redéfinit la méthode __gt__ pour comparer les deux livres (dans ce cas, sur le prix)
    # ceci permet d'utiliser le comparateur > entre deux objets de la classe Livre; en temps normal, ceci lèverait
    # une exception TypeError
    def __gt__(self, other):
        return self.__prix > other.get_prix()

    # On redéfinit la méthode __eq__ pour comparer les deux livres (dans ce cas, sur le prix)
    # ceci permet d'utiliser le comparateur == entre deux objets de la classe Livre; en temps normal, retournerait True
    # seulement si les deux objets sont identiques (i.e. même adresse mémoire, le comparer à lui-même)
    def __eq__(self, other):
        return self.__prix == other.get_prix()

    # On redéfinit la méthode __add__ pour additionner les deux livres
    # ceci permet d'utiliser l'opérateur + entre deux objets de la classe Livre; en temps normal, ceci lèverait
    # une exception TypeError
    # On crée un nouveau livre avec le titre et l'auteur des deux livres et le prix total
    def __add__(self, other):
        titre = self.__titre + " et " + other.get_titre()
        auteur = self.__auteur + " et " + other.get_auteur()
        prix = self.__prix + other.get_prix()
        return Livre(titre, auteur, prix)


# Exemples d'utilisation des méthodes redéfinies
miserable = Livre("Les Misérables", "Victor Hugo", 14.99)
alice = Livre("Alice au pays des merveilles", "Lewis Carroll", 9.99)

if miserable > alice:
    print("Le premier livre est plus cher que le deuxième")
elif miserable == alice:
    print("Les deux livres ont le même prix")
else:
    print("Le premier livre est moins cher que le deuxième")

addition_livres = miserable + alice

print(addition_livres)

