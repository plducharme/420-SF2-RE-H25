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
# labyrinthe.afficher()

## Trouver la solution

pile_solution = []
# Utiliser la pile pour trouver la solution
# On doit réinitialiser les cellules à non visitées
for x in range(labyrinthe.largeur):
    for y in range(labyrinthe.hauteur):
        labyrinthe.cellules[x][y].visitee = False
# On commence à la cellule d'entrée
cellule = labyrinthe.cellules[0][0]
pile_solution.append(cellule)
cellule.visitee = True
solution_trouvee = False
index_sortie = labyrinthe.largeur - 1, labyrinthe.hauteur - 1

while not solution_trouvee:
    # Regarder les voisins de la cellule actuelle
    voisins = []
    if cellule.x > 0 and not cellule.murs["ouest"]:
        ouest = labyrinthe.cellules[cellule.x - 1][cellule.y]
        if not ouest.visitee:
            voisins.append(ouest)
    if cellule.x < labyrinthe.largeur - 1 and not cellule.murs["est"]:
        est = labyrinthe.cellules[cellule.x + 1][cellule.y]
        if not est.visitee:
            voisins.append(est)
    if cellule.y > 0 and not cellule.murs["nord"]:
        nord = labyrinthe.cellules[cellule.x][cellule.y - 1]
        if not nord.visitee:
            voisins.append(nord)
    if cellule.y < labyrinthe.hauteur - 1 and not cellule.murs["sud"]:
        sud = labyrinthe.cellules[cellule.x][cellule.y + 1]
        if not sud.visitee:
            voisins.append(sud)

    if cellule.x == index_sortie[0] and cellule.y == index_sortie[1]:
        solution_trouvee = True
        break
    # On a plus de voisins à visiter, on remonte dans la pile
    if len(voisins) == 0:
            cellule = pile_solution.pop()
    # On choisi un voisin aléatoire à visiter
    else:
        cellule = voisins[random.randint(0, len(voisins) - 1)]
        pile_solution.append(cellule)
        cellule.visitee = True

# On imprime la solution
for cellule in pile_solution:
    print(cellule)

# On aurait pu modifier la classe pour avoir une méthode qui retourne les voisins visitables, cette méthode aurait pu être
# utilisée pour trouver la solution et pour générer le labyrinthe

