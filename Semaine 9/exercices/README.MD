# Exercices sur les tris

## Trier des dates par insertion
 - Créer une classe Date qui contient trois attributs: jour, mois et année.
 - Ajouter le constructeur `__init__` qui initialise les attributs.
 - Encapsuler les attributs.
 - Ajouter une méthode statique "from_date_string(date_str: str)" qui prend une date de la forme "jj/mm/aaaa" et retourne une instance de la classe Date.
 - Implémenter les opérateurs de comparaisons pour comparer deux dates.
 - Créer une liste de dates avec les dates incluses dans le fichier trier_des_dates.py 


# Trier des cartes par sélection
 - Créer une classe Carte qui contient deux attributs: valeur et couleur.
 - Ajouter le constructeur `__init__` qui initialise les attributs.
 - Encapsuler les attributs.
 - Implémenter la méthode créant le jeu de carte au complet; doit retourner une liste de Carte mélangée.
 - Implémenter les opérateurs de comparaisons pour comparer deux cartes. (trèfle < carreau < coeur < pique; 1 à 13)
 - Créer une liste de cartes avec les cartes incluses dans le fichier trier_des_cartes.py


# Trier les pays les plus heureux par bulle
 - Créer une classe Pays qui contient deux attributs: nom, et score (Happiness_Score)
 - Ajouter le constructeur `__init__` qui initialise les attributs.
 - Encapsuler les attributs.
 - Implémenter les méthodes de comparaisons pour comparer deux pays.
 - Utiliser Pandas pour importer les données du fichier trier_des_pays.py
   - Voir les exemples dans la section extras du dépôt
   - Vous pouvez utiliser le fichier `world-happiness-report.csv` pour cet exercice
   - Filtrer les données pour ne garder que les pays de l'année 2022 (colonne Year)
   - Créer une liste de Pays avec les données filtrées
   - Ne pas utiliser le tri de Pandas
 - Implémenter le tri par bulle pour trier les pays par score de bonheur