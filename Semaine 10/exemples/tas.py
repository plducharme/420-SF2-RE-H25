from random import randint


class TasMax:

    def __init__(self, tableau):
        self.tableau = tableau
        self.creation_tas_max(self.tableau)

    def tasser_max(self, tableau, index):
        max_index = index
        index_fils_gauche = 2 * index + 1
        index_fils_droit = 2 * index + 2

        # Compare le père avec le fils gauche pour déterminer si un fils est plus grand que le père; si oui, lequel des
        # deux. On garde l'index de celui-ci
        if index_fils_gauche < len(tableau) and tableau[index_fils_gauche] > tableau[max_index]:
            max_index = index_fils_gauche
        if index_fils_droit < len(tableau) and tableau[index_fils_droit] > tableau[max_index]:
            max_index = index_fils_droit
        # Si max == index, le père est plus grand que les fils
        if max_index != index:
            # On a trouvé le plus grand fils, plus grand que le père. On les permute
            tableau[index], tableau[max_index] = tableau[max_index], tableau[index]
            self.tasser_max(tableau, max_index)

    def creation_tas_max(self, tableau):
        # trouve l'index du dernier pere
        index_dernier_pere = len(tableau) // 2 - 1

        # On commence par le dernier père inséré et on tasse les pères de droite à gauche et de bas en haut
        for i in range(index_dernier_pere, -1, -1):
            self.tasser_max(tableau, i)


liste = [randint(1, 100) for x in range(10)]
print(liste)
tas = TasMax(liste)
print(liste)
