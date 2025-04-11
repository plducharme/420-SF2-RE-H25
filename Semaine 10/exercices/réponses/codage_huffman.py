import heapq
import struct


# Classe représentant un noeud de l'arbre de Huffman
# caractere : le caractère associé au noeud, None si c'est un noeud fusionné qui ne contient pas de caractère
# frequence : la fréquence d'apparition du caractère
# gauche : le fils gauche du noeud
# droite : le fils droit du noeud
class NoeudHuffman:
    def __init__(self, caractere = None, frequence = 0):
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = None
        self.droite = None

    def __lt__(self, autre):
        return self.frequence < autre.frequence

    # Méthode pour calculer la fréquence des caractères dans le texte
    @staticmethod
    def calculer_frequences(texte) -> dict:
        frequences = {}
        for caractere in texte:
            if caractere in frequences:
                frequences[caractere] += 1
            else:
                frequences[caractere] = 1
        return frequences

    # Méthode pour créer l'arbre de Huffman à partir des fréquences
    # frequences : dictionnaire contenant les caractères et leurs fréquences
    # À la place d'utiliser une liste de noeuds et la retrier à chaque fois, on aurait pu utiliser un tas (heapq) ou
    # une file de priorité pour optimiser la fusion des noeuds (se trie automatiquement)
    @staticmethod
    def batir_arbre_huffman(frequences):
        liste_noeuds = [NoeudHuffman(c, f) for c, f in frequences.items()]
        # On trie pour avoir les noeuds avec la plus petite fréquence en premier
        liste_noeuds.sort(key=lambda x: x.frequence)
        # On construit l'arbre de Huffman
        while len(liste_noeuds) > 1:
            # On fusionne les deux noeuds avec la plus petite fréquence
            gauche = liste_noeuds.pop(0)
            droite = liste_noeuds.pop(0)
            # On crée un nouveau noeud qui est la fusion des deux noeuds
            fusion = NoeudHuffman(None, gauche.frequence + droite.frequence)
            fusion.gauche = gauche
            fusion.droite = droite
            # On ajoute le noeud fusionné à la liste
            liste_noeuds.append(fusion)
            # On trie à nouveau la liste pour avoir les noeuds avec la plus petite fréquence en premier
            # Dans les fait, on replace le noeud fusionné à la bonne place dans la liste
            liste_noeuds.sort(key=lambda x: x.frequence)

        # On retourne le noeud racine de l'arbre de Huffman (quand il n'y a plus qu'un seul noeud dans la liste)
        return liste_noeuds.pop()

    # Méthode pour générer le code de Huffman à partir de l'arbre
    # noeud : le noeud actuel
    # prefixe : le code binaire associé au noeud actuel, où on est rendu dans l'arbre
    @staticmethod
    def generer_code_huffman(noeud, prefixe="", codes=None):
        if codes is None:
            codes = {}
        if noeud is None:
            return
        # Si le noeud est une feuille (caractère), on ajoute le code associé au caractère
        if noeud.caractere is not None:
            codes[noeud.caractere] = prefixe
        # On parcourt les fils gauche et droit de l'arbre
        NoeudHuffman.generer_code_huffman(noeud.gauche, prefixe + "0", codes)
        NoeudHuffman.generer_code_huffman(noeud.droite, prefixe + "1", codes)

        return codes

    # Méthode pour encoder le texte en utilisant le code de Huffman
    # texte : le texte à encoder
    # codes : le dictionnaire contenant les caractères et leurs codes de Huffman
    @staticmethod
    def encoder(texte, codes):
        code_binaire = ""
        for caractere in texte:
            # On ajoute le code associé au caractère au code binaire
            code_binaire += codes[caractere]
        return code_binaire

    # Méthode pour décoder le code binaire en utilisant l'arbre de Huffman
    # code_binaire : le code binaire à décoder
    # racine : la racine de l'arbre de Huffman
    @staticmethod
    def decoder(code_binaire, racine):
        texte_decode = ""
        noeud_courant = racine
        # On parcourt le code binaire
        for bit in code_binaire:
            # On descend dans l'arbre selon la valeur du bit (0 ou 1)
            if bit == "0":
                noeud_courant = noeud_courant.gauche
            else:
                noeud_courant = noeud_courant.droite
            # Si on atteint une feuille, on ajoute le caractère au texte décodé
            if noeud_courant.caractere is not None:
                texte_decode += noeud_courant.caractere
                # Comme on a atteint une feuille, on retourne à la racine pour continuer le décodage du prochain
                # caractère
                noeud_courant = racine

        return texte_decode

    # Méthode pour écrire le code binaire dans un fichier avec des bits
    # On compresse sur disque
    @staticmethod
    def ecrire_code_binaire_fichier(code_binaire, nom_fichier):
        with open(nom_fichier, "wb") as f:
            # On ajoute des bits pour que la longueur soit un multiple de 8
            padded_bit_string = code_binaire + '0' * ((8 - len(code_binaire) % 8) % 8)
            # On convertit le code binaire en tableau d'octets
            tableau_binaire = bytes(int(padded_bit_string[i:i+8], 2) for i in range(0, len(padded_bit_string), 8))
            # On écrit le tableau binaire dans le fichier
            f.write(tableau_binaire)

    # Méthode pour lire le code binaire à partir d'un fichier
    # On décompresse à partir du fichier
    # Pour le faire exactement, il faudrait savoir combien de bits on a ajouté pour le padding
    # (i.e passer la taille originale)
    @staticmethod
    def lire_code_binaire_fichier(nom_fichier, taille_originale=None):
        with open(nom_fichier, "rb") as f:
            # On lit le tableau binaire du fichier
            tableau_binaire = f.read()
            # On convertit le tableau binaire en code binaire
            code_binaire_str = ''.join(f"{byte:08b}" for byte in tableau_binaire)
        if taille_originale is not None:
            # On enlève le padding
            code_binaire_str = code_binaire_str[:taille_originale]
        return code_binaire_str


if __name__ == "__main__":
    texte_ex = "Le cours de programmation est le meilleur cours de l'univers"

    def encoder_decoder(texte_a_encoder, afficher_texte=True):
        if afficher_texte:
            print("Texte à encoder : ", texte_a_encoder)

        racine = NoeudHuffman.batir_arbre_huffman(NoeudHuffman.calculer_frequences(texte_a_encoder))
        # On génère le code de Huffman à partir de l'arbre
        codes_huffman = NoeudHuffman.generer_code_huffman(racine)
        print("Codes de Huffman : ", codes_huffman)
        # On encode le texte en utilisant le code de Huffman
        code_binaire = NoeudHuffman.encoder(texte_a_encoder, codes_huffman)
        # Ceci est la représentation binaire mais sous forme de texte
        # Donc chaque "bit" est un caractère, donc 8 bits
        # Dans la réalité, pour encoder, on aurait besoin de convertir la représentation dans un tableau de bits
        if afficher_texte:
            print("Code binaire : ", code_binaire)

        # On décode le code binaire en utilisant l'arbre de Huffman
        texte_decode = NoeudHuffman.decoder(code_binaire, racine)
        if afficher_texte:
            print("Texte décodé : ", texte_decode)
        print("Grandeur du texte original : ", len(texte_a_encoder))
        print("Grandeur du texte encodé (sans padding): ", len(code_binaire) / 8)
        print("Taux de compression : ", (len(code_binaire) / 8) / len(texte_a_encoder))
        return racine, code_binaire

    encoder_decoder(texte_ex)
    # On teste avec un texte plus long
    with open("les_miserables.txt", "r", encoding="utf-8") as f:
        texte_long = f.read()
        racine, code_binaire_miserable = encoder_decoder(texte_long, False)
        # On va le compresser sur disque en binaire
        NoeudHuffman.ecrire_code_binaire_fichier(code_binaire_miserable, "les_miserables.bin")
        # On va le décompresser sur disque
        code_binaire = NoeudHuffman.lire_code_binaire_fichier("les_miserables.bin", len(code_binaire_miserable))
        # On va le décoder
        texte_decode = NoeudHuffman.decoder(code_binaire, racine)
        print("Longueur du texte décodé : ", len(texte_decode))




