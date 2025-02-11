
def ma_fonction_ou_methode():
    try:
        open('filename.txt')
        return 0
    except FileNotFoundError as e:
        print('hmmm, le fichier existe pas')
        return 1
    finally:
        print('Je suis toujours exécuté!')
        # Si on ajoute un return ici, il va remplacer le return 0 ou 1 car le block finally est toujours executé
        # avant le return


print(ma_fonction_ou_methode())

# Nettoyage automatique grâce au with (force l'appel du finally
with open('test.txt') as f:
    for ligne in f:
        print(ligne)


# Code équivalent sans with
f = open('test.txt')
try:
    for ligne in f:
        print(ligne)
finally:
    f.close()
    print('Fermeture du fichier!')
