# Se référer au fichier graphe_ex.png pour visualiser le graphe

# graphe représenté par une matrice d'adjacence
# La liste principale représente les sommets du graphe (ex: la première liste représente le sommet 0, la deuxième liste
# représente le sommet 1, etc.)
# Chaque liste interne représente les sommets adjacents au sommet correspondant à la liste principale
# Les valeurs dans les listes internes représentent le poids (coût) des arêtes entre les sommets (0 signifie qu'il n'y a
# pas de sommets adjacents)
graph = [[0, 5, 3, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 12, 0],
         [6, 8, 0, 0, 7],
         [0, 0, 0, 0, 0]]

# graphe représenté par une liste d'adjacence (utilise un dictionnaire)
# La clé représente le sommet du graphe
# La valeur associée à la clé est une liste de tuples (identité, poids), où le premier élément du tuple est le sommet
# adjacent et le deuxième élément est le poids de l'arête entre les sommets
liste = {0: [(1, 5), (2, 3)],
         1: [],
         2: [(3, 12)],
         3: [(0, 6), (1, 8), (4, 7)],
         4: []}
