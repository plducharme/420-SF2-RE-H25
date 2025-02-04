class Personne:

    def __init__(self, nom: str, prenom: str):
        self._nom = nom
        self._prenom = prenom


    def get_nom(self) -> str:
        return self._nom

    def get_prenom(self) -> str:
        return self._prenom

    def set_nom(self, nom: str) -> None:
        self._nom = nom

    def set_prenom(self, prenom: str) -> None:
        self._prenom = prenom


class Etudiant(Personne):

    def __init__(self, nom: str, prenom: str, no_da: int):
        super().__init__(nom, prenom)
        self._no_da = no_da

    def get_programme(self) -> int:
        return self._no_da

    def set_programme(self, no_da: int) -> None:
        self._no_da = no_da

class Professeur(Personne):

    def __init__(self, nom: str, prenom: str, no_employe: int):
        super().__init__(nom, prenom)
        self._no_employe = no_employe

    def get_no_employe(self) -> int:
        return self._no_employe

    def set_no_employe(self, no_employe: int) -> None:
        self._no_employe = no_employe


class Cours:

    def __init__(self, nom: str, sigle: str, prof: Professeur):
        self.__nom = nom
        self.__sigle = sigle
        self.__prof = prof
        self.__etudiants = []

    def get_nom(self) -> str:
        return self.__nom

    def get_sigle(self) -> str:
        return self.__sigle

    def get_prof(self) -> Professeur:
        return self.__prof

    def set_nom(self, nom: str) -> None:
        self.__nom = nom

    def set_sigle(self, sigle: str) -> None:
        self.__sigle = sigle

    def set_prof(self, prof: Professeur) -> None:
        self.__prof = prof

    def ajouter_etudiant(self, etudiant: Etudiant) -> None:
        self.__etudiants.append(etudiant)

    def get_etudiants(self) -> list:
        return self.__etudiants

    def set_etudiants(self, etudiants: list) -> None:
        self.__etudiants = etudiants

    def __str__(self) -> str:
        return f"{self.__nom} ({self.__sigle}) - Professeur: {self.__prof.get_nom()} - Étudiants: {', '.join([etudiant.get_nom() for etudiant in self.__etudiants])}"


pld = Professeur("Ducharme", "Pier-Luc", 1234)

alice = Etudiant("Beauregard", "Alice", 123456)
bob = Etudiant("Lemieux", "Bob", 654321)
charlie = Etudiant("Tremblay", "Charlie", 987654)
etudiants = [alice, bob, charlie]

cours = Cours("Programmation orientée objet", "420-SD2-HY", pld)
cours.set_etudiants(etudiants)

daniel = Etudiant("Lemieux", "Daniel", 456789)
cours.ajouter_etudiant(daniel)

print(cours)






