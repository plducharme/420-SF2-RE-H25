# Modéliser les classes pour un jeu de rôle
1) Créer une classe abstraite nommée "Classe" représentant une classe de personnage pour un jeu de rôle
- Cette classe devra contenir des propriétés représentant une classe de personnage
  - Doit contenir les propriétés:
    - nom
      - str: Le nom de la classe
    - sante
      - int: la santé de base de la classe
    - attaque
      - float: l'attaque de base de la classe
    - defense
      - float: la défense de base de la classe
    - vitesse
      - float: la vitesse de base de la classe
    - magie
      - float: la magie de base de la classe
  - Vous devez respecter l'encapsulation
    - Les propriétés doivent être protégées
    - Utiliser les décorateurs @property et @propriete.setter
    - Ajouter 2 méthodes abstraites
      - attaquer(self, pourcentage_de_touche: float) : méthode abstraite qui retourne un entier représentant les dégâts infligés
        - Les dégats infligés sont calculés en fonction de l'attaque ou la magie du personnage si le pourcentage de touche est respecté
          - Les dégats sont effectués si un nombre aléatoire entre 0 et 1 est inférieur ou égal au pourcentage de touche
      - defendre(self, pourcentage_de_touche: float) : méthode abstraite qui retourne un entier représentant les dégâts reçus
        - Les dégats reçus sont calculés en fonction de la défense du personnage si le pourcentage de touche est respecté
          - Les dégats sont reçus si un nombre aléatoire entre 0 et 1 est inférieur ou égal au pourcentage de touche
2) Créer deux classes enfants qui représenteront des classes de personnage spécifiques: guerrier et mage
    - Implémenter les méthodes abstraites de la classe parente
    - Mage:
      - Les dégâts infligés sont calculés en fonction de la magie du personnage
      - Les dégâts reçus sont calculés en fonction de la défense du personnage et de la présence ou nom d'un sort de bouclier magique
        - Si le bouclier magique est actif, les dégâts reçus sont réduits de 50%
      - Ajouter une propriété booléenne nommée "sort_bouclier_magique" qui indique si le mage a un bouclier magique actif
      - Ajouter une propriété nommée "mana: float" qui représente le mana du mage
3) Créer une classe abstraite "Monstre" représentant un monstre pour un jeu de rôle
    - Cette classe devra contenir des propriétés représentant un monstre
      - Doit contenir les propriétés:
        - nom
          - str: Le nom du monstre
        - sante
          - int: la santé de base du monstre
        - attaque
          - float: l'attaque du monstre
        - defense
          - float: la défense du monstre
    - Ajouter deux méthodes abstraites
      - attaquer(self, pourcentage_de_touche: float) : méthode abstraite qui retourne un entier représentant les dégâts infligés
        - Les dégats infligés sont calculés en fonction
        - Les dégats sont effectués si un nombre aléatoire entre 0 et 1 est inférieur ou égal au pourcentage de touche
      - defendre(self, pourcentage_de_touche: float) : méthode abstraite qui retourne un entier représentant les dégâts reçus
        - Les dégats reçus sont calculés en fonction de la défense du monstre
        - Les dégats sont reçus si un nombre aléatoire entre 0 et 1 est inférieur ou égal au pourcentage de touche
4) Implémenter une classe enfant de Monstre nommée "Kobold"
    - Les dégâts infligés sont calculés en fonction de l'attaque du monstre
    - Les dégâts reçus sont calculés en fonction de la défense du monstre
    - Ajouter une propriété nommée "butin" qui représente le butin que le monstre donne au joueur
      - Le butin est un nombre aléatoire entre 0 et 100
      - Le butin est donné au joueur si le monstre est vaincu
5) Créer une classe "JeuDeRole" qui implémente une logique de base pour le jeu
    - Créer une boucle while qui continue tant que le joueur et le monstre ont de la santé

6) Comment pourrions-nous changer le design des classes abstraites pour accommoder le fait que Classe et Monstres ont des propriétés et des méthodes en commun?

# Explorer la bibliothèque Pandas
1) Installer le package pandas
2) Importer le data du CSV Europe_GDP.csv
   - Voir la section Extras/pandas pour un exemple
3) Afficher les 5 premières lignes du DataFrame
4) Afficher les 5 dernières lignes du DataFrame
5) Afficher la moyenne du GDP de 1980 pour tous les pays
6) Afficher le GDP de la France pour toutes les années
7) Afficher le GDP moyen de la France pour toutes les années
8) Tester les diverses méthodes de pandas
