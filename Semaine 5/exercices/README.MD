# Piles

## Labyrinthe
Le code donnée génère un labyrinthe. Utiliser une pile pour trouver un chemin partant de la case (0,0) jusqu'à la 
case (n-1,n-1) où n est la taille du labyrinthe.

- Chaque fois que vous visitez une case, ajoutez la case à la pile.
- Si vous ne pouvez pas avancer, retirez la case de la pile et revenez en arrière.
- Vous pouvez seulement vous déplacer vers une case adjacente où le mur est absent (False).


# Arbres
Créer un arbre servant à encoder des mots. Chaque noeud de l'arbre contient une lettre. Les enfants d'un noeud sont les
lettres suivantes du mot.

La classe pour le noeud d'un arbre devra s'appeler Lettre.
Les enfants d'un noeud seront stockés dans un dictionnaire où la clé est la lettre suivante et la valeur est le noeud.

- Implémenter une méthode pour ajouter un mot à l'arbre.
- Implémenter une méthode pour vérifier si un mot est dans l'arbre.
- Implémenter une méthode pour afficher tous les mots de l'arbre.


# Map
Utiliser un map et un lambda pour créer une liste où la lettre d'un mot (de la liste mots) sera changer en majuscule à la position donnée (de
la liste positions).

>Exemple:  
>mots = ['bonjour', 'salut', 'allo']  
>positions = [1, 2, 3]  
>resultat = ['bOnjour', 'saLut', 'allO']


# Reduce
Utiliser un reduce et un lambda pour trouver le total de la valeur des codes ASCII des lettres d'un mot':

- Faites-le pour un mot.
- Essayez de le faire pour une liste de mots.
- Essayez de le faire pour une liste de mots en utilisant un map et un reduce.

