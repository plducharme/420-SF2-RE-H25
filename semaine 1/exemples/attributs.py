class Personne:
    # variable de classe
    type_personne = 'humain'

    # constructeur
    def __init__(self,  nom, prenom):
        # variables d'instance
        self.nom = nom
        self.prenom = prenom

    def set_email(self, email):
        # création d'une variable d'instance en dehors du constructeur; légal, mais pas recommandé
        self.email = email


# instanciation d'un objet
prof = Personne("Ducharme", "Pier Luc")
# Appel de la méthode sur l'objet
prof.set_email("plducharme@cegepsth.qc.ca")

# appel d'une variable de classe (on utilise le nom de la classe)
print(Personne.type_personne)
# peut être appelé via l'objet
print(prof.type_personne)

# instanciation d'un autre objet
ada = Personne("Lovelace", "Ada")
# Va retourner une AttributeError car email n'existe pas pour ada
print(ada.email)


