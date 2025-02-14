from abc import ABC, abstractmethod
import random


class Classe(ABC):
    def __init__(self, nom, sante, attaque, defense, magie):
        self._nom = nom
        self._sante = sante
        self._attaque = attaque
        self._defense = defense
        self._magie = magie

    @property
    def nom(self):
        return self._nom

    @property
    def sante(self):
        return self._sante

    @property
    def attaque(self):
        return self._attaque

    @property
    def defense(self):
        return self._defense

    @property
    def magie(self):
        return self._magie

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @sante.setter
    def sante(self, sante):
        self._sante = sante

    @attaque.setter
    def attaque(self, attaque):
        self._attaque = attaque

    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @magie.setter
    def magie(self, magie):
        self._magie = magie

    @abstractmethod
    def attaquer(self, pourcentage_de_touche: float):
        pass

    @abstractmethod
    def defendre(self, pourcentage_de_touche: float):
        pass


class Guerrier(Classe):
    def __init__(self, nom, sante, attaque, defense, magie):
        super().__init__(nom, sante, attaque, defense, magie)

    def attaquer(self, pourcentage_de_touche: float):
        if pourcentage_de_touche >= random.random():
            return self.attaque
        else:
            return 0

    def defendre(self, pourcentage_de_touche: float):
        if pourcentage_de_touche >= random.random():
            return self.defense
        else:
            return 0


class Mage(Classe):
    def __init__(self, nom, sante, attaque, defense, magie, mana):
        super().__init__(nom, sante, attaque, defense, magie)
        self._mana = mana
        self._bouclier_actif = False

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana):
        self._mana = mana

    @property
    def bouclier_actif(self):
        return self._bouclier_actif

    @bouclier_actif.setter
    def bouclier_actif(self, bouclier_actif):
        self._bouclier_actif = bouclier_actif

    def attaquer(self, pourcentage_de_touche: float):
        if pourcentage_de_touche >= random.random():
            return self.attaque
        else:
            return 0

    def defendre(self, pourcentage_de_touche: float):
        if pourcentage_de_touche >= random.random():
            degats_amortis = self.defense
            if self.bouclier_actif:
                degats_amortis = degats_amortis * 1.5
            return degats_amortis
        else:
            return 0


class Monstre(ABC):
    def __init__(self, nom, sante, attaque, defense):
        self._nom = nom
        self._sante = sante
        self._attaque = attaque
        self._defense = defense
        self._butin = random.randint(0, 100)

    @property
    def nom(self):
        return self._nom

    @property
    def sante(self):
        return self._sante

    @property
    def attaque(self):
        return self._attaque

    @property
    def defense(self):
        return self._defense

    @property
    def butin(self):
        return self._butin

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @sante.setter
    def sante(self, sante):
        self._sante = sante

    @attaque.setter
    def attaque(self, attaque):
        self._attaque = attaque

    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @butin.setter
    def butin(self, butin):
        self._butin = butin

    @abstractmethod
    def attaquer(self, pourcentage_de_touche: float):
        pass

    @abstractmethod
    def defendre(self, pourcentage_de_touche: float):
        pass


class Kobold(Monstre):
    def __init__(self, nom, sante, attaque, defense):
        super().__init__(nom, sante, attaque, defense)

    def attaquer(self, pourcentage_de_touche: float):
        if pourcentage_de_touche >= random.random():
            return self.attaque
        else:
            return 0

    def defendre(self, pourcentage_de_touche: float):
        if pourcentage_de_touche >= random.random():
            return self.defense
        else:
            return 0


class JeuDeRole:

    def __init__(self):
        self._joueur = None
        self._monstre = None
        # Cette propriété aurait pu être un attribut de la classe "Classe"
        self._butin_joueur = 0

    @property
    def joueur(self):
        return self._joueur

    @property
    def monstre(self):
        return self._monstre

    @property
    def butin_joueur(self):
        return self._butin_joueur

    @joueur.setter
    def joueur(self, joueur):
        self._joueur = joueur

    @monstre.setter
    def monstre(self, monstre):
        self._monstre = monstre

    @butin_joueur.setter
    def butin_joueur(self, butin_joueur):
        self._butin_joueur = butin_joueur

    def combat(self):
        print("-" * 30)
        print(f"{self.joueur.nom} rencontre {self.monstre.nom}")
        while self.joueur.sante > 0 and self.monstre.sante > 0:
            # le joueur a un minimum de 25% de chance de toucher
            attaque_joueur = self.joueur.attaquer(max(random.random(), 0.25))
            # le monstre a un minimum de 10% de chance de se défendre
            defense_monstre = self.monstre.defendre(max(random.random(), 0.10))
            degats = max(0, attaque_joueur - defense_monstre)
            self.monstre.sante -= degats
            print(f"{self.joueur.nom} attaque {self.monstre.nom} pour {degats} points de dégâts")

            attaque_monstre = self.monstre.attaquer(random.random())
            defense_joueur = self.joueur.defendre(max(random.random(), 0.25))
            degats_monstre = max(0, attaque_monstre - defense_joueur)
            self.joueur.sante -= degats_monstre
            print(f"{self.monstre.nom} attaque {self.joueur.nom} pour {degats_monstre} points de dégâts")
        if self.joueur.sante <= 0:
            print(f"{self.joueur.nom} est mort")
        if self.monstre.sante <= 0:
            print(f"{self.monstre.nom} est mort")
            print(f"{self.joueur.nom} a obtenu {self.monstre.butin} pièces d'or")
            self.butin_joueur += self.monstre.butin

    def creer_joueur(self):
        nom = input("Entrez le nom de votre personnage: ")
        classe = input("Entrez la classe de votre personnage (Guerrier/Mage): ")
        if classe == "Guerrier":
            return Guerrier(nom, 100, 10, 5, 0)
        if classe == "Mage":
            return Mage(nom, 100, 5, 2, 10, 100)
        else:
            print("Classe invalide")
            self.creer_joueur()


noms_kobold = ["Hogger", "Gnasher", "Gnawbone", "Gnawtooth", "Gnawface"]

jdr = JeuDeRole()
jdr.joueur = jdr.creer_joueur()

while jdr.joueur.sante > 0:
    jdr.monstre = Kobold(random.choice(noms_kobold), random.randint(25, 51), random.randint(2, 5),
                         random.randint(1, 3))
    jdr.combat()

print(f"Vous avez obtenu {jdr.butin_joueur} pièces d'or")

# Améliorations possibles:
# Utiliser une classe abstraite commune pour Classe et Monstre au lieu de dupliquer les méthodes et propriétés
# Ajouter la logique pour l'utilisation du bouclier du Mage
# Ajouter des sorts pour le Mage
# Ajouter des armes pour le Guerrier
# Ajouter des monstres de différents types
# Ajouter un système de niveaux
# Implémenter le système de mana pour le Mage
