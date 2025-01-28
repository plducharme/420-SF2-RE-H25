class Aigle:

    def __init__(self):
        self.nb_ailes = 2

    def voler(self):
        print(f"Swoosh!! Il vole de ses {self.nb_ailes} ailes!")

    def crier(self):
        print("Hiiiiiiiiiiii!!")



class Licorne:

    def __init__(self):
        self.couleur_corne = "argent"

    def galoper(self):
        print(f"Il gallope avec sa corne {self.couleur_corne}!")

    def crier(self):
        print("Huuuuuuuuuuu!!")


# La classe Pegase hérite de Aigle et Licorne
# Elle va hériter des attributs (méthodes et variables) de Aigle puis de ceux de Licorne.
class Pegase(Aigle, Licorne):

    def __init__(self):
        # Appel du constructeur de la classe parente
        Aigle.__init__(self)
        # Appel du constructeur de la classe parente
        Licorne.__init__(self)

    # Si on ne redéfinit pas la méthode crier(), c'est la méthode de la classe parente Aigle qui sera appelée
    # car elle a été définie en premier dans la liste des classes parentes
    def crier(self):
        print(f"HiiiiiiHuuuuu!! Regardez mes {self.nb_ailes} ailes et ma jolie corne {self.couleur_corne}!")


p = Pegase()
p.galoper()
p.voler()
p.crier()
# mro() est une méthode qui retourne la liste des classes parentes dans l'ordre de priorité
# Ici, on voit que la classe Aigle est prioritaire par rapport à Licorne
# car elle a été définie en premier dans la liste des classes parentes
# À noter que l'on appelle la méthode mro() sur la classe et non sur un objet
print(Pegase.mro())

