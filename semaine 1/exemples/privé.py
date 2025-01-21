class Personne:

    # constructeur
    def __init__(self,  nom, prenom):
        # variables d'instance
        self.__nom = nom
        self.__prenom = prenom

    def afficher(self):
        print(self.__nom + " " + self.__prenom)

pld = Personne("Ducharme", "Pier Luc")
pld.afficher()
# Va retourner une AttributeError car __nom est privé
print(pld.__nom)
# "mangling", le nom de la variable est modifié pour éviter les collisions (à ne pas faire, mais ne donne pas d'erreur)
print(pld._Personne__nom)

