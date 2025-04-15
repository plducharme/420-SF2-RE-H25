class Bibliotheque:
    def __init__(self):
        self.livres = {}  # Dictionnaire pour stocker les livres et leur disponibilité

    def ajouter_livre(self, titre, auteur):
        """Ajoute un livre à la bibliothèque."""
        if titre in self.livres:
            raise ValueError(f"Le livre '{titre}' existe déjà dans la bibliothèque.")
        self.livres[titre] = {"auteur": auteur, "disponible": True}

    def emprunter_livre(self, titre):
        """Permet d'emprunter un livre s'il est disponible."""
        if titre not in self.livres:
            raise ValueError(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")
        if not self.livres[titre]["disponible"]:
            raise ValueError(f"Le livre '{titre}' est déjà emprunté.")
        self.livres[titre]["disponible"] = False


    def retourner_livre(self, titre):
        """Permet de retourner un livre emprunté."""
        if titre not in self.livres:
            raise ValueError(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")
        if self.livres[titre]["disponible"]:
            raise ValueError(f"Le livre '{titre}' n'a pas été emprunté.")
        self.livres[titre]["disponible"] = True


    def disponibilite_livres(self):
        """Retourne une lsite de tuples avec le titre et la disponibilité des livres."""
        if not self.livres:
            raise ValueError("La bibliothèque est vide.")
        else:
            liste_disponibilite = []
            for titre, details in self.livres.items():
                statut = "Disponible" if details["disponible"] else "Emprunté"
                liste_disponibilite.append((titre, statut))
        return liste_disponibilite
