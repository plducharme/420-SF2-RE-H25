from datetime import date

class Personne:

    # variable de classe
    nom_drapeau = "Apatride"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    # Cette méthode va modifier la variable de classe nom_drapeau pour tous les objets de la classe Personne
    @classmethod
    def set_drapeau_pour_tous(cls, nom_drapeau):
        cls.nom_drapeau = nom_drapeau

    # Cette méthode va instancier un objet de la classe Personne à partir de l'année de naissance
    @classmethod
    def from_annee_naissance(cls, nom, date_naissance: date):
        age = cls.calculer_age(date_naissance)
        return cls(nom, )

    # Cette méthode va calculer l'âge de la personne en fonction de la date de naissance
    # On peut remarquer que cette méthode utilise seulement des variables passées en paramètre
    @staticmethod
    def calculer_age(date_naissance: date):
        return (date.today() - date_naissance).days // 365


alice = Personne('Alice', 19)
print(alice.nom_drapeau)
# Une méthode statique peut être appelée sur la classe ou sur une instance (objet)
bob = Personne.from_annee_naissance('Bob', date(2000, 3, 12))
print(Personne.calculer_age(date(1980, 4, 19)))
# Peut être appelé sur la classe
Personne.set_drapeau_pour_tous("Fleurdelysé")
# Peut être appelé sur une instance (objet)
bob.set_drapeau_pour_tous("Fleurdelysé")
print(alice.nom_drapeau)
print(bob.nom_drapeau)
