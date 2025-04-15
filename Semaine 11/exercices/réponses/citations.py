import os

# Il y a plusieurs stratégies pour accomplir l'extraction des citations vers des fichirrs séparés
# On peut soit lire toutes les citations dans un dictionnaire, puis générer les fichiers
# Ou on peut lire les citations et les écrire au fur et à mesure dans les fichiers
# Nous allons utiliser la deuxième méthode pour pratiquer l'écriture

# On regarde si un répertoire temporaire existe déjà
if os.path.exists("citations"):
    # On supprime les fichiers
    for fichier in os.listdir("citations"):
        os.remove(f"citations/{fichier}")
else:
    os.mkdir("citations")

with open("citations.txt", "r", encoding="utf-8") as citations:
    # On lit le fichier ligne par ligne
    for citation in citations:

        # On sépare la citation de l'auteur
        citation, auteur = citation.split("~")
        # On supprime le caractère de fin de ligne pour l'auteur
        auteur = auteur.rstrip("\n")
        # On écrit la citation dans un fichier
        with open(f"citations/{auteur}.txt", "a", encoding="utf-8") as auteur_fichier:
            auteur_fichier.write(citation + "\n")

