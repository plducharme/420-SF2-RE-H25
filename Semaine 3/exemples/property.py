class NombrePositif:

    def __init__(self, valeur):
        self.__valeur = valeur

    @property
    def valeur(self):
        print('méthode getter appelée')
        return self.__valeur

    @valeur.setter
    def valeur(self, valeur):
        print('méthode setter appelée')
        if valeur < 0:
            raise ValueError('le nombre doit être positif')
        self.__valeur = valeur


bon_nombre = NombrePositif(3)
print(bon_nombre.valeur)
bon_nombre.valeur = 4
print(bon_nombre.valeur)

mauvais_nombre = NombrePositif(0)
mauvais_nombre.valeur = -1


