# exemple de classe interne
class Voiture:
    # Variable de classe, variable qui est commune à tous les objets instanciés de cette classe, existe au niveau de la
    # classe
    nombre_de_roues = 4

    def __init__(self, marque, modele):
        # déclaration de variables d'instance (ex: self.marque) et assignation à ce qui est passé en paramètres
        # (ex: marque)
        self.marque = marque
        self.modele = modele
        # Création d'une instance de la classe interne Moteur
        self.moteur = self.Moteur(470, "essence")

    def vroom(self):
        # impression des variables d'instance
        print(self.marque + "\t" + self.modele + "\tvroom!")

    # classe interne
    class Moteur:
        def __init__(self, puissance, carburant):
            self.puissance = puissance
            self.carburant = carburant

        def demarrer(self):
            print(f"Démarrage du moteur de {self.puissance} chevaux")

        def arreter(self):
            print("Arrêt du moteur")

# Création d'une instance de la classe en appelant le constructeur __init__(self, marque. modele)
challenger = Voiture("Dodge", "Challenger")
# accès à la classe interne
challenger.moteur.demarrer()
# appel d'une méthode de l'objet
challenger.vroom()


