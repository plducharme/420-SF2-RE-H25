# Héritage et Polymorphisme
1) Créer une classe représentant un instrument de musique
- Cette classe devra contenir des propriétés représentant un instrument
- Vous devez respecter l'encapsulation
- Ajouter 2 méthodes avec une implémentation de base (peut être un print())

2) Créer deux classes enfants qui représenteront des instruments de musique spécifique (guitare, piano, guimbarde, etc)
- Ces classes devront contenir des propriétés spécifiques à ces instruments
- Ajouter une méthode spécifique à chaque classe
- Redéfinir une des méthodes de la classe parente
- Respectez l'encapsulation
- Appelez les divers constructeurs et méthodes pour observer les résultats


3) Créer une classe représentant un orchestre
- Cette classe devra contenir une liste d'instruments (des exercices 1 et 2)
- Ajouter une méthode pour ajouter un instrument à l'orchestre basé sur un nom d'instrument passé en paramètre
- Ajouter une méthode pour jouer un morceau (un instrument à la fois)

# Créer des classes représentant un cours d'informatique
4) Créer les classes pour représenter un cours d'informatique
- Classe Personne
  - Cette classe devra contenir des propriétés représentant une personne
  - nom
  - prénom
- Classe Étudiant
  - Cette classe hérite de la classe Personne
  - Cette classe devra contenir des propriétés représentant un étudiant
  - numéro d'étudiant
- Classe Professeur
  - Cette classe hérite de la classe Personne
  - Cette classe devra contenir des propriétés représentant un professeur
  - numéro d'employé 
- Classe Cours
  - Cette classe devra contenir des propriétés représentant un cours
    - nom
    - sigle
    - professeur (de type Professeur)
    - liste d'étudiants (de type Étudiant)
- Toutes les classes devront respecter l'encapsulation