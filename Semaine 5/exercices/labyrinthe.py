import random

class Cellule:

    def __init__(self, x: int, y: int):
        # True si la cellule a été visitée, False sinon
        self._visitee = False
        # True si le mur est présent, False sinon
        self._murs = {
            "nord": True,
            "est": True,
            "sud": True,
            "ouest": True
        }
        self._x = x
        self._y = y

    @property
    def visitee(self):
        return self._visitee

    @visitee.setter
    def visitee(self, visitee: bool):
        self._visitee = visitee

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y

    @property
    def murs(self):
        return self._murs

    def __repr__(self):
        return f"({self._x}, {self._y}, murs: {self._murs})"


class Labyrinthe:

    def __init__(self, largeur: int, hauteur: int):
        """Initialisation d'un labyrinthe.

        largeur, hauteur -- dimensions du labyrinthe
        """
        self.__largeur = largeur
        self.__hauteur = hauteur
        self._cellules = [[Cellule(x, y) for y in range(hauteur)] for x in range(largeur)]
        self.__sortie_visitee = False


    @property
    def largeur(self):
        return self.__largeur

    @property
    def hauteur(self):
        return self.__hauteur

    @property
    def cellules(self):
        return self._cellules


    def generer_labyrinthe(self):
        # On entre en haut à gauche et on sort en bas à droite
        entree = self._cellules[0][0]
        sortie = self._cellules[self.__largeur - 1][self.__hauteur - 1]

        self.visiter_voisins(entree)


    def visiter_voisins(self, cellule: Cellule):
        cellule.visitee = True

        if cellule.x == 0 and cellule.y == 0 and self.__sortie_visitee:
            return

        if cellule.x == self.__largeur - 1 and cellule.y == self.__hauteur - 1:
            self.__sortie_visitee = True
            return

        # On regarde les voisins possibles de la cellule
        voisins = []
        if cellule.x > 0:
            voisins.append("ouest")
        if cellule.x < self.largeur - 1:
            voisins.append("est")
        if cellule.y > 0:
            voisins.append("nord")
        if cellule.y < self.hauteur - 1:
            voisins.append("sud")

        # On mélange les voisins pour les visiter dans un ordre aléatoire
        random.shuffle(voisins)
        # Pour chaque voisin visité, on marque le voisin comme visité et on casse le mur entre la cellule et le voisin
        for voisin in voisins:
            if voisin == "nord":
                nord = self._cellules[cellule.x][cellule.y - 1]
                cellule.murs["nord"] = False
                nord.murs["sud"] = False
                if not nord.visitee:
                    self.visiter_voisins(nord)
            elif voisin == "est":
                est = self._cellules[cellule.x + 1][cellule.y]
                cellule.murs["est"] = False
                est.murs["ouest"] = False
                if not est.visitee:
                    self.visiter_voisins(est)
            elif voisin == "sud":
                sud = self._cellules[cellule.x][cellule.y + 1]
                cellule.murs["sud"] = False
                sud.murs["nord"] = False
                if not sud.visitee:
                    self.visiter_voisins(sud)
            elif voisin == "ouest":
                ouest = self._cellules[cellule.x - 1][cellule.y]
                cellule.murs["ouest"] = False
                ouest.murs["est"] = False
                if not ouest.visitee:
                    self.visiter_voisins(ouest)


    def afficher(self):
        for x in range(self.__largeur):
            for y in range(self.__hauteur):
                cellule = self._cellules[x][y]
                print(cellule)



labyrinthe = Labyrinthe(10, 10)
labyrinthe.generer_labyrinthe()
labyrinthe.afficher()

pile_solution = []
# Utiliser la pile pour trouver la solution
