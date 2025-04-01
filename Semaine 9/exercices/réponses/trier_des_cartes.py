import random
from enum import Enum


# Pour se faciliter la vie, on utilise un Enum pour les couleurs
# Un Enum est une classe qui permet de définir des constantes nommées associées à des valeurs
# Ceci aurait pu être une classe interne à Carte
class CouleurCarte(Enum):
    TREFLE = 1
    CARREAU = 2
    COEUR = 3
    PIQUE = 4


class Carte:

    def __init__(self, valeur, couleur):
        self.__valeur = valeur
        self.__couleur = couleur

    @property
    def valeur(self):
        return self.__valeur

    @property
    def couleur(self):
        return self.__couleur

    # __repr__ est une méthode spéciale qui permet de définir la représentation d'un objet (ce qui va s'afficher si on
    # fait un print(objet))
    # On redéfini cette méthode héritée de la classe object
    def __repr__(self):
        return f'{self.__valeur} de {self.__couleur.name}'

    # On compare les cartes en fonction de leur couleur en premier, puis leur valeur
    # Trèfle < Carreau < Coeur < Pique
    def __lt__(self, other):
        if self.couleur.value < other.couleur.value:
            return True
        elif self.couleur.value > other.couleur.value:
            return False
        else:
            return self.valeur < other.valeur

    @staticmethod
    def generer_jeu_de_cartes():
        jeu_de_cartes = []
        for couleur in CouleurCarte:
            for valeur in range(1, 14):
                jeu_de_cartes.append(Carte(valeur, couleur))
        # On brasse les cartes
        random.shuffle(jeu_de_cartes)
        return jeu_de_cartes


def tri_selection(jeu):
    for i in range(0, len(jeu)):
        min_jeu = jeu[i]
        min_index = i

        for j in range(i + 1, len(jeu)):
            if jeu[j] < min_jeu:
                min_jeu = jeu[j]
                min_index = j

        jeu[i], jeu[min_index] = jeu[min_index], jeu[i]
    return jeu


if __name__ == '__main__':
    print("Génération du jeu de cartes...")
    jeu = Carte.generer_jeu_de_cartes()
    print(jeu)
    print("Tri des cartes...")
    tri_selection(jeu)
    print(jeu)
