import random
import logging


class Tas:
    def __init__(self, liste):
        self.liste = liste
        self.creation_tas_max()

    def creation_tas_max(self):
        n = len(self.liste)
        for i in range(n // 2 - 1, -1, -1):
            self.tas_max(i, n)

    # méthode qui tamise vers le bas
    # i est l'index de l'élément à tamiser
    # n est la taille du tas (longueur de la liste), techniquement, n n'est pas nécessaire et pourrait être remplacé
    # par len(self.liste)
    def tas_max(self, i, n):
        index_plus_grand = i
        index_fils_gauche = 2 * i + 1
        index_fils_droite = 2 * i + 2

        # On regarde si le fils de gauche existe et s'il est plus grand que le père
        # Dans ce cas, on garde l'index du fils gauche, ça devient le plus grand
        if index_fils_gauche < n and self.liste[index_fils_gauche] > self.liste[index_plus_grand]:
            index_plus_grand = index_fils_gauche
        # On regarde si le fils de droite existe et s'il est plus grand que le père
        # Dans ce cas, on garde l'index du fils droit, ça devient le plus grand
        if index_fils_droite < n and self.liste[index_fils_droite] > self.liste[index_plus_grand]:
            index_plus_grand = index_fils_droite

        # Si on a trouvé un fils plus grand que le père, on l'échange avec le père
        if index_plus_grand != i:
            self.liste[i], self.liste[index_plus_grand] = self.liste[index_plus_grand], self.liste[i]
            # On appelle la méthode récursivement sur le fils qui a été échangé
            self.tas_max(index_plus_grand, n)

    # Pour l'insertion, on va ajouter l'élément à la fin de la liste
    # puis on tamise vers le haut (on compare l'élément avec son parent et on l'échange si nécessaire)
    # On recommence jusqu'à ce que l'élément soit à sa place
    def insertion(self, valeur):
        self.liste.append(valeur)
        # On se garde l'index de l'élément inséré
        index = len(self.liste) - 1
        # Si l'index est inférieur à 0, on est à la racine
        while index > 0:
            # On calcule l'index du parent, la formule inverse de celle pour calculer l'enfant
            index_parent = (index - 1) // 2
            # Si son parent est plus petit que lui, on l'échange
            if self.liste[index] > self.liste[index_parent]:
                self.liste[index], self.liste[index_parent] = self.liste[index_parent], self.liste[index]
                index = index_parent
            else:
                # Si le parent est plus grand, on a un tas max valide, on arrête la boucle
                break

    # Pour la suppression, on va remplacer la racine par le dernier élément du tas
    # Puis on tamise vers le bas
    # Cette opération est l'équivalent d'un popleft() (ou pop(0)) sur une liste
    def extraction(self):
        element_enleve = self.liste[0]
        # On remplace la racine par le dernier élément
        self.liste[0] = self.liste[-1]
        # On enlève le dernier élément
        # On aurait pu le faire en une instruction à la ligne précédente (i.e self.liste[0] = self.liste.pop())
        self.liste.pop()
        # On tamise vers le bas
        self.tas_max(0, len(self.liste))

        return element_enleve

    def remplacement(self, valeur):
        # On remplace la racine par la nouvelle valeur
        self.liste[0] = valeur
        # On tamise vers le bas
        self.tas_max(0, len(self.liste))


if __name__ == "__main__":
    # Utilisation d'un logger pour afficher les messages
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Création d'une liste de 12 entiers aléatoires entre 0 et 50
    # _ signifie que la variable n'est pas utilisée (any)
    liste_valeurs = [random.randint(0, 50) for _ in range(12)]
    logger.info(f"Liste initiale avant tas: {liste_valeurs}")

    tas = Tas(liste_valeurs)
    logger.info(f"Liste après création du tas: {tas.liste}")
    logger.info(f"Valeur extraite: {tas.extraction()}")
    logger.info(f"Liste après extraction: {tas.liste}")
    tas.insertion(42)
    logger.info(f"Liste après insertion de 42: {tas.liste}")
    tas.remplacement(37)
    logger.info(f"Liste après remplacement de la racine par 37: {tas.liste}")



