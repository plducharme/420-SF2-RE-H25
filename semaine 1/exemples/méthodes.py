class Carotte:

    def __init__(self, couleur="orange"):
        print("Une carotte est plantée")
        self.__couleur = couleur

    def pousse(self):
        print(f"La carotte {self.__couleur} pousse")

carotte = Carotte()
# Appel de la méthode pousse de l'objet carotte
carotte.pousse()

