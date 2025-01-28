class Polygone:

    def __init__(self, nb_cotes):
        self._nb_cotes = nb_cotes
        self._nom = None

    def afficher(self):
        print(f"Je suis un polygone à {self._nb_cotes} côtés")


class Triangle(Polygone):

    def __init__(self):
        super().__init__(3)
        self._nom = "triangle"

    def afficher(self):
        print(f"Je suis un triangle")


class TriangleIsocele(Triangle):

    def __init__(self, base, hauteur):
        super().__init__()
        self._base = base
        self._hauteur = hauteur
        self._nom = "triangle isocèle"

    def afficher(self):
        print(f"Je suis un {self._nom} de base {self._base} et de hauteur {self._hauteur}")


triangle = TriangleIsocele(3, 4)
triangle.afficher()
print(TriangleIsocele.mro())

