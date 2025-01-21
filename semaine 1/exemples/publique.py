class Mobile:

    def __init__(self, marque, modele, prix):
        self.marque = marque
        self.modele = modele
        self.prix = prix

    def afficher(self):
        # à l'intérieur de la classe, on peut accéder à toutes les variables (dont celles publiques)
        print(self.marque + " " + self.modele + " " + str(self.prix) + "$")

zflip_five_g = Mobile("Samsung", "Z Flip 5G", 2000)
# On accède à une variable publique en utilisant le point
print(zflip_five_g.marque)


