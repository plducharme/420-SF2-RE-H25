"""
Algorithme de Dijkstra pour trouver le plus court chemin entre deux noeuds d'un graphe contenant des arêtes pondérées
non-négatives. On va utiliser une matrice d'adjacence pour représenter le graphe. Plus précisément, il calcule la
distance minimale entre un noeud de départ et tous les autres noeuds du graphe. On peut donc l'utiliser pour trouver le
plus court chemin entre un noeud de départ et un noeud d'arrivée. L'algorithme de Dijkstra est un algorithme glouton
(greedy), c'est-à-dire qu'il choisit toujours le noeud le plus proche du noeud de départ pour lequel on a la distance la plus
courte. On utilise un tableau de noeuds visités et un tableau de distances pour garder en mémoire les noeuds visités et
les distances respectives.

Si on veut savoir le plus court chemin entre deux noeuds, on doit garder en mémoire les noeuds précédents pour pouvoir
reconstruire le chemin. On peut utiliser un tableau de noeuds précédents pour cela.

Dans les faits, l'algorithme est un arbre de recherche où on explore les noeuds les plus proches du noeud de départ en
calculant la distance entre le noeud de départ et les noeuds adjacents.

"""
import sys


class Graphe:

    def __init__(self, matrice_adjacence, index_depart):
        self.noeuds = len(matrice_adjacence)
        self.matrice_adjacence = matrice_adjacence
        self.index_depart = index_depart

    # L'index du noeud de départ est passé en paramètre
    def plus_court_chemin(self):
        # Initialisation des variables
        # On initialise un tableau de noeuds visités; au départ, aucun noeud n'a été visité
        visites = [False for _ in range(self.noeuds)]
        # On initialise un tableau de distances; au départ, la distance entre le noeud de départ et tous les autres
        # noeuds est infinie
        distance = [sys.maxsize for _ in range(self.noeuds)]
        # La distance entre le noeud de départ et lui-même est de 0; ceci l'identifie comme le noeud de départ
        distance[self.index_depart] = 0

        # On initialise un tableau de noeuds précédents; au départ, aucun noeud n'a de noeud précédent
        precedents = [-1 for _ in range(self.noeuds)]
        # On initialise un noeud courant; au départ, c'est le noeud de départ
        courant = self.index_depart

        for _ in range(self.noeuds):
            # On marque le noeud courant comme visité
            visites[courant] = True

            # On cherche le noeud le plus proche du noeud de départ qui n'a pas encore été visité
            min_distance = sys.maxsize
            for i in range(self.noeuds):
                if not visites[i] and distance[i] < min_distance:
                    min_distance = distance[i]
                    courant = i


            # On récupère les distances entre le noeud courant et ses noeuds adjacents
            for i in range(self.noeuds):
                # On vérifie si le noeud n'a pas déjà été visité et si la distance entre le noeud courant et le noeud i
                # est plus petite que la distance actuelle
                if not visites[i] and self.matrice_adjacence[courant][i] != 0 and distance[courant] + self.matrice_adjacence[courant][i] < distance[i]:
                    # On met à jour la distance
                    distance[i] = distance[courant] + self.matrice_adjacence[courant][i]
                    # On met à jour le noeud précédent
                    precedents[i] = courant

        # On retourne le tableau de distances et le tableau de noeuds précédents
        return distance, precedents


    def afficher_chemin(self, noeud, precedents):
        if noeud == self.index_depart:
            print(noeud)
        elif precedents[noeud] == -1:
            print("Pas de chemin")
        else:
            self.afficher_chemin(precedents[noeud], precedents)
            print(f"{noeud} ", end="")


    def afficher_solution(self, distance, precedents):

        for i in range(self.noeuds):
            print(f"\nNoeud: {i}\tdistance: {distance[i]}\nchemin:")
            self.afficher_chemin(i, precedents)


graphe = [[0, 5, 3, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 12, 0],
         [6, 8, 0, 0, 7],
         [0, 0, 0, 0, 0]]


g = Graphe(graphe, 0)
distance, precedents = g.plus_court_chemin()
g.afficher_solution(distance, precedents)
