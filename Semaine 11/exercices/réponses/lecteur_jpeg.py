
# Par Dr. Philip Bethge — Collection particulière, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=2970659
with open("ornithorynque.jpg", "rb") as jpeg_file:
    soi = jpeg_file.read(2)

    if soi[0] != 0xFF or soi[1] != 0xD8:
        print("Ce fichier n'est pas un JPEG")

    marqueur = jpeg_file.read(2)
    while marqueur != b'\xFF\xDA':
        # print("marqueur ou contenu non supporté: ", marqueur)
        marqueur = jpeg_file.read(2)

    print("Marqueur de début de scan trouvé SOS: ", marqueur)
    reste_contenu = jpeg_file.read()
    print("Taille du contenu : ", len(reste_contenu))

