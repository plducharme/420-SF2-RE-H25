import zipfile
import os
import tarfile
import shutil

# On regarde si un répertoire temporaire existe déjà
if os.path.exists("compression"):
    # On supprime les fichiers du répertoire
    for nom_fichier in os.listdir("compression"):
        os.remove(os.path.join("compression", nom_fichier))
else:
    os.mkdir("compression")

print("Compression avec zipfile")
# Avec une zip
with zipfile.ZipFile("./compression/citations.zip", "w") as fichier_zip:
    # On liste tous les fichiers du répertoire citations
    for nom_fichier in os.listdir("./citations"):
        # On ajoute le fichier au zip si ce n'est pas une archive
        if not nom_fichier.endswith(".zip") or not nom_fichier.endswith(".tar.gz") or not nom_fichier.endswith(".bz2"):
            fichier_zip.write(os.path.join("./citations", nom_fichier), nom_fichier)

print("Compression avec zipfile en utilisant shutil")
# Avec shutil (zipfile)
# shutil est un module de haut niveau qui utilise zipfile, tarfile, gztar, bztar ou xztar
shutil.make_archive("./compression/citations2", "zip", "./citations")

print("Compression avec tarfile")
# Avec tarfile
with tarfile.open("./compression/citations.tar.gz", "w:gz") as fichier_tar:
    # On liste tous les fichiers du répertoire citations
    for nom_fichier in os.listdir("./citations"):
        # On ajoute le fichier au tar
        if not nom_fichier.endswith(".zip") or not nom_fichier.endswith(".tar.gz") or not nom_fichier.endswith(".bz2"):
            fichier_tar.add(os.path.join("./citations", nom_fichier), nom_fichier)

print("Compression avec bz2")
# Avec bz2
# Pour faciliter, la compression, on va utiliser un tarfile pour compresser l'ensemble des fichiers en un tarball
# avant de le compresser.
with tarfile.open("./compression/citations.tar.bz2", "w:bz2") as fichier_tar:
    # On liste tous les fichiers du répertoire citations
    for nom_fichier in os.listdir("./citations"):
        # On ajoute le fichier au tar
        if not nom_fichier.endswith(".zip") or not nom_fichier.endswith(".tar.gz") or not nom_fichier.endswith(".bz2"):
            fichier_tar.add(os.path.join("./citations", nom_fichier), nom_fichier)


