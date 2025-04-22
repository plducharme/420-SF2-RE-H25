

class Voiture:

    def __init__(self, marque: str, modele: str, annee: int, kilometrage: int = 0):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._vitesse = 0

    @property
    def marque(self):
        return self._marque

    @property
    def modele(self):
        return self._modele

    @property
    def annee(self):
        return self._annee

    @property
    def kilometrage(self):
        return self._kilometrage

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, valeur: int):
        self._vitesse = valeur

    @kilometrage.setter
    def kilometrage(self, valeur: int):
        if valeur < 0:
            raise ValueError("Le kilométrage ne peut pas être négatif.")
        self._kilometrage = valeur

    @marque.setter
    def marque(self, valeur: str):
        if not isinstance(valeur, str):
            raise ValueError("La marque doit être une chaîne de caractères.")
        self._marque = valeur

    @modele.setter
    def modele(self, valeur: str):
        if not isinstance(valeur, str):
            raise ValueError("Le modèle doit être une chaîne de caractères.")
        self._modele = valeur

    @annee.setter
    def annee(self, valeur: int):
        if not isinstance(valeur, int) or valeur < 1886:
            raise ValueError("L'année doit être un entier supérieur ou égal à 1886.")
        self._annee = valeur

    def avancer(self, temps: float, vitesse: float):
        if temps < 0 or vitesse < 0:
            raise ValueError("Le temps et la vitesse doivent être positifs.")
        distance = vitesse * temps
        self.kilometrage += distance
        self.vitesse = vitesse
        return distance

