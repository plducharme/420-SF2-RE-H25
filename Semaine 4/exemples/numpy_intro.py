# np est l'alias conventionnel de numpy
import numpy as np

# Créer un tableau numpy 1D à partir d'une liste
tableau = np.array([1, 2, 3, 4, 5])
print(tableau)

# Les tableaux numpy permettent d'effectuer des opérations sur tous les éléments en même temps
tableau2 = tableau * 2
print(tableau2)

# Il est impossible de faire ceci avec une liste
liste = [1, 2, 3, 4, 5]

# ceci va doubler la liste avec les éléments répétés
liste2 = liste * 2
print(liste2)
# ceci va lever une exception
try:
    liste3 = liste / 3
except TypeError as e:
    print(e)

# Créer un tableau numpy 2D à partir d'une liste de listes
tableau_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Afficher le tableau
print(tableau_2d)

# Créer un tableau numpy 2D de 0 avec les dimensions 3x4
tableau_zeros = np.zeros((3, 4))
print(tableau_zeros)

# Créer un tableau numpy 2D de 1 avec les dimensions 3x4
tableau_ones = np.ones((3, 4))
print(tableau_ones)

# Créer un tableau numpy 2D de valeurs aléatoires entre 0 et 1 avec les dimensions 3x4x2
tableau_random = np.random.rand(3, 4, 2)
print("Tableau 3D aléatoire")
print(tableau_random)

# Créer un tableau numpy 1D à partir d'un range
# Fonction comme le range() de Python (début incl, fin excl, pas) mais retourne un tableau numpy
tableau_range = np.arange(2, 10)
print(tableau_range)

# Créer un tableau numpy 1D réparti en 5 valeurs entre 0 et 10
tableau_linspace = np.linspace(0, 10, 5)
print(tableau_linspace)

# Créer une matrice identité (1 sur la diagonale) de dimension 3x3
matrice_identite = np.eye(3)
print(matrice_identite)

# Créer une matrice avec des 5 sur la diagonale
matrice_5 = np.diag([5, 5, 5])
print(matrice_5)
# Alternativement
matrice_5_2 = matrice_identite * 5
print(matrice_5_2)

# Créer une matrice diagonale avec des valeurs croissantes
matrice_diag = np.diag(np.arange(1, 6))
print(matrice_diag)

# Un tableau à plusieurs dimensions est un tableau de tableaux
# On accède aux éléments avec des indices séparés par des virgules
# ou comme on le ferait pour une liste de listes
tableau_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tableau_3d)
# Accéder à un élément
print(tableau_3d[0, 1, 1])
# Équivalent
print(tableau_3d[0][1][1])

# Pour savoir la forme d'un tableau, on utilise la propriété shape
print(tableau_3d.shape)

# Pour faire le produit matriciel (dot product en anglais) de deux matrices, on utilise la fonction dot
print("Produit matriciel")
tableau_dot1 = np.array([[1, 2, 3], [4, 5, 6]])
tableau_dot2 = np.array([[7, 8], [9, 10], [11, 12]])
print(tableau_dot1)
print(tableau_dot2)
tableau_dot = np.dot(tableau_dot1, tableau_dot2)
print(tableau_dot)

# Produit terme à terme (element-wise) de deux tableaux
# Ceci multipliera chaque élément de tableau_t1 par chaque élément correspondant du tableau_t2
print("Multiplication terme à terme")
tableau_t1 = np.array([[1, 2], [3, 4]])
tableau_t2 = np.array([[5, 6], [7, 8]])
print(tableau_t1)
print(tableau_t2)
tableau_termes = tableau_t1 * tableau_t2
print(tableau_termes)

# Aplatir un tableau multidimensionnel en un tableau 1D
tableau_3d2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tableau_3d2)
tableau_aplati = tableau_3d2.flatten()
print(tableau_aplati)
# Flatten() retourne une copie du tableau, ravel() retourne une vue (view) du tableau. Si on modifie le tableau ravel,
# le tableau original est modifié
tableau_ravel = tableau_3d2.ravel()
print(tableau_ravel)

# L'opération inverse est reshape. On passe les dimensions voulues en argument (shape)
tableau_reshape = tableau_aplati.reshape(2, 4)
print(tableau_reshape)

# On peut transposer un tableau avec la méthode transpose
tableau_2_3 = np.array([[1, 2, 3], [4, 5, 6]])
print(tableau_2_3)
tableau_transpose = np.transpose(tableau_2_3)
print(tableau_transpose)

# On peut trouver le minimum, le maximum, la somme et la moyenne d'un tableau
tableau_ex = np.array([[66, 42, 34], [1, 2, 3], [4, 5, 6]])
# minimum du tableau
print(np.amin(tableau_ex))
# Minimum d'une colonne
print(np.amin(tableau_ex, axis=0))
# Minimum d'une ligne
print(np.amin(tableau_ex, axis=1))
# maximum du tableau
print(np.amax(tableau_ex))
# Maximum d'une colonne
print(np.amax(tableau_ex, axis=0))
# Maximum d'une ligne
print(np.amax(tableau_ex, axis=1))
# somme du tableau
print(np.sum(tableau_ex))
# Somme des colonnes
print(np.sum(tableau_ex, axis=0))
# Somme des lignes
print(np.sum(tableau_ex, axis=1))
# moyenne du tableau
print(np.mean(tableau_ex))
# Moyenne des colonnes
print(np.mean(tableau_ex, axis=0))
# Moyenne des lignes
print(np.mean(tableau_ex, axis=1))

# Il existe d'autres fonctions comme median (médiane), std (écart-type), var (variance), etc.

# On peut aussi calculer la moyenne pondérée
# On doit passer les poids en argument
tableau_notes = np.array([80, 90, 70, 85])
tableau_poids = np.array([0.2, 0.3, 0.1, 0.4])
moyenne_ponderee = np.average(tableau_notes, weights=tableau_poids)
print(moyenne_ponderee)
