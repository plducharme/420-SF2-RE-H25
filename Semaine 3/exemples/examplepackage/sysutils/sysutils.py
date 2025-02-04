import sys

def afficher_chemin_python():
    print(sys.path)

# Code à la racine du module qui sera exécuté lors de l'importation
print("Ce code est exécuté depuis " + __name__ + " car il n'était pas dans la condition if __name__ == '__main__':")


if __name__ == '__main__':
    afficher_chemin_python()

