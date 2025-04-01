import random


def generer_date() -> str:
    annee = random.randint(2023, 2025)
    mois = random.randint(1, 12)
    jour = None
    if mois == 2:
        jour = random.randint(1, 28)
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        jour = random.randint(1, 31)
    else:
        jour = random.randint(1, 30)
    return f"{jour}/{mois}/{annee}"


listes_des_dates = [generer_date() for _ in range(20)]


# Implémenter la classe Date et le tri par insertion
class Date:

    def __init__(self, jour, mois, annee):
        self.__jour = jour
        self.__mois = mois
        self.__annee = annee

    @property
    def jour(self):
        return self.__jour

    @property
    def mois(self):
        return self.__mois

    @property
    def annee(self):
        return self.__annee

    def __gt__(self, other):
        if self.annee > other.annee:
            return True
        elif self.annee == other.annee:
            if self.mois > other.mois:
                return True
            elif self.mois == other.mois:
                if self.jour > other.jour:
                    return True
        return False

    def __repr__(self):
        return f"{self.jour}/{self.mois}/{self.annee}"

    @staticmethod
    def from_date_string(date_str: str):
        jour, mois, annee = date_str.split("/")
        return Date(int(jour), int(mois), int(annee))


liste_a_trier = [Date.from_date_string(date) for date in listes_des_dates]


def tri_insertion(liste: list):
    for i in range(1, len(liste)):
        courant = liste[i]
        p = i
        while p > 0 and liste[p - 1] > courant:
            liste[p] = liste[p - 1]
            p -= 1

        liste[p] = courant


if __name__ == '__main__':
    print(liste_a_trier)
    tri_insertion(liste_a_trier)
    print(liste_a_trier)
