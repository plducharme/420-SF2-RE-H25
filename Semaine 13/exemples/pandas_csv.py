import pandas as pd

# Voir la section pandas sous le répertoire extras du dépôt
# Lire le fichier CSV pour créer un DataFrame
# D'autres formats sont supportés: read_excel(), read_json(),
# read_html(), read_sql(), read_clipboard(), read_parquet(), read_orc(), read_sas(), read_spss(), read_sql_query(),
# read_sql_table(), read_feather(), read_fwf(), read_gbq(), read_hdf(), read_pickle(), read_sas(), read_spss(), etc
# Pour certains formats, il faut installer des bibliothèques tierces (ex: openpyxl pour Excel, lxml pour HTML, pyarrow pour Parquet, etc)
df = pd.read_csv("chien.csv", sep=";", encoding="utf8")

# Afficher le DataFrame
print("DataFrame")
print(df)
# Afficher la colonne "Nom"
print("\nColonne Nom")
print(df["Nom"])
# Afficher la colonne "Nom" et "Race"
print("\nColonnes Nom et Race")
print(df[["Nom", "Race"]])

# Itérer sur les lignes du DataFrame
# df.iterrows() retourne un itérateur qui retourne un tuple (index, Series)
print("\nLignes d'itération")
for index, ligne in df.iterrows():
    print(f"{index}:\t{ligne["Nom"]}\t{ligne['Race']}\t{ligne['Couleur']}")

# Écrire le DataFrame dans un fichier CSV
# Si index=True, le DataFrame sera écrit avec l'index (comme première colonne)
df.to_csv("chien_export.csv", sep=";", encoding="utf8", index=False)
