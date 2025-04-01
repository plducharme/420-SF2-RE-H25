import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("world_happiness_report.csv")

# Filtrer pour ne conserver que les lignes de 2022
df = df[df["Year"] == 2022]


# Classe pour représenter un pays
class Pays:
    def __init__(self, nom: str, score: float):
        self.__nom = nom
        self.__score = score

    @property
    def nom(self):
        return self.__nom

    @property
    def score(self):
        return self.__score

    def __repr__(self):
        return f"{self.nom}: {self.score}"

    def __lt__(self, other):
        return self.score < other.score


# Créer une liste de pays à partir des données du DataFrame
liste_pays = []
for index, row in df.iterrows():
    pays = Pays(row["Country"], row["Happiness_Score"])
    liste_pays.append(pays)


# Trier la liste de pays par score en utilisant un tri à bulles
def trier_bulles(liste_a_trier):
    for i in range(0, len(liste_a_trier)):
        deja_trie = True

        if liste_a_trier[i+1] < liste_a_trier[i]:
            liste_a_trier[i], liste_a_trier[i+1] = liste_a_trier[i+1], liste_a_trier[i]
            deja_trie = False


print("Liste des pays avant le tri:")
print(liste_pays)
# La bulle de Pépin: https://www.youtube.com/watch?v=ALVtyyipVs8
print("Trions avec le tri à bulles")
trier_bulles(liste_pays)
print("Liste des pays après le tri:")
print(liste_pays)
