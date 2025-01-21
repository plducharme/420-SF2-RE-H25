class Pomme:
    def __init__(self, couleur, variete, prix):
        self.couleur = couleur
        self.variete = variete
        self._prix = prix

    # accesseur en lecture pour la variable d'instance _prix (style classique) ou getter
    def get_prix(self):
        return self._prix

    # accesseur en écriture pour la variable d'instance _prix (style classique) ou setter
    def set_prix(self, prix):
        if prix < 0:
            raise ValueError("Le prix doit être positif")
        self._prix = prix

grannysmith = Pomme("verte", "Granny Smith", 0.75)
print(grannysmith.get_prix())
grannysmith.set_prix(0.50)
print(grannysmith.get_prix())

