class Personne:

    # constructeur
    def __init__(self,  nom, prenom):
        # variables d'instance
        self.__nom = nom
        self.__prenom = prenom

    def afficher(self):
        print(self.__nom + " " + self.__prenom)

    # accesseur en lecture pour la variable d'instance __nom (style classique) ou getter
    def get_nom(self):
        return self.__nom

    # accesseur en écriture pour la variable d'instance __nom (style classique) ou setter
    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom



pld = Personne("Ducharme", "Pier Luc")
pld.afficher()
# Va retourner une AttributeError car __nom est privé
print(pld.__nom)
# "mangling", le nom de la variable est modifié pour éviter les collisions (à ne pas faire, mais ne donne pas d'erreur)
print(pld._Personne__nom)
# accès via l'accesseur
print(pld.get_nom())

