# ouverture d'un fichier en mode lecture binaire
# 'rb' signifie 'read binary'
# Dans cet exemple, nous allons lire l'entête d'un fichier PNG
# https://en.wikipedia.org/wiki/PNG
with open('cc.xlarge.png', 'rb') as image_reader:
    # Type du lecteur de fichier, il s'agit d'un objet de type io.BufferedReader, une lecture avec un buffer (tampon)
    print(type(image_reader))
    # le paramètre de la fonction read() est le nombre d'octets à lire
    premier_octet = image_reader.read(1)
    print(premier_octet)
    # Nom
    nom = image_reader.read(3)
    print(nom)
    # Caharacter de fin de ligne pour DOS
    crlf = image_reader.read(2)
    print(crlf)
    # Character de fin de fichier
    fin = image_reader.read(1)
    print(fin)
    # Caractère de fin de fichier Unix
    eol = image_reader.read(1)
    print(eol)

with open("fichier_binaire.pld", "wb") as fichier_bin:
    # Écriture d'une chaîne de caractères dans le fichier
    fichier_bin.write(b"Texte en octets")
    # Écriture d'une liste de chaînes de caractères dans le fichier
    fichier_bin.writelines([b"Texte en octets", bytes.fromhex("2Ef0 F1f2")])






    