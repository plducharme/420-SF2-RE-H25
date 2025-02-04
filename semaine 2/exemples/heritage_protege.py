# classe parente ou superclasse définissant un polygone
# À noter que la classe Polygone aurait dû être abstraite (vu dans un cours ultérieur)
class Polygone:

    def __init__(self, nb_cotes):
        self._nb_cotes = nb_cotes
        self._nom = None

    def afficher(self):
        print(f"Je suis un polygone à {self._nb_cotes} côtés")


# La classe Triangle hérite de la classe Polygone
class Triangle(Polygone):

    def __init__(self):
        # Appel du constructeur de la classe parente Polygone avec 3 côtés
        super().__init__(3)
        # On définit le nom de ce polygone
        self._nom = "triangle"

    # On redéfinit la méthode afficher() de la classe parente
    def afficher(self):
        print(f"Je suis un triangle")


class TriangleIsocele(Triangle):

    # On définit un constructeur avec deux paramètres spécifiant la base et la hauteur du triangle isolcèle
    def __init__(self, base, hauteur):
        # On appelle le constructeur de la classe parente Triangle
        # qui appelle elle-même le constructeur de la classe Polygone
        super().__init__()
        # En plus d'hériter des attributs publiques et protégés des classes parentes,
        # on définit deux attributs spécifiques à cette classe
        self._base = base
        self._hauteur = hauteur
        self._nom = "triangle isocèle"

    # On redéfinit la méthode afficher() de la classe Triangle (qui elle-même redéfinit la méthode de la
    # classe Polygone)
    def afficher(self):
        print(f"Je suis un {self._nom} de base {self._base} et de hauteur {self._hauteur}")


triangle = TriangleIsocele(3, 4)
triangle.afficher()
# mro() est une méthode qui retourne l'ordre de résolution des méthodes
print(TriangleIsocele.mro())

