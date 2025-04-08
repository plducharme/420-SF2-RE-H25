import unicodedata


u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)
print(u)
# Afficher la catégorie de chaque caractère et son nom
for i, c in enumerate(u):
    print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
    print(unicodedata.name(c))

# Le caractère 0x0bf2 sous forme numérique
print(unicodedata.numeric(u[1]))


# Pour transformer un fichier latin-1 en utf-8, on peut utiliser la fonction encode/decode
with open("encodage-latin-1.txt", "rb") as fichier:
    with open("encodage-utf-8.txt", "wb") as fichier_utf8:
        for ligne in fichier:
            # On encode la ligne en utf-8 et on écrit dans le fichier utf-8
            fichier_utf8.write(ligne.decode("latin-1").encode("utf-8"))



