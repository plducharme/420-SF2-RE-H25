from collections import ChainMap

peinture = {'La Joconde': 'DaVinci', 'Les Baigneuses': 'Courbet', 'La jeune fille à la perle': 'Vermeer'}
films = {'Full Metal Jacket': 'Kubrick', 'Metropolis': 'Fritz Lang'}
musiques = {'Thriller': 'Michael Jackson', 'Back in Black': 'AC/DC', "Metropolis": "Kraftwerk"}

cm = ChainMap(peinture, films, musiques)
# affiche la liste de clés-valeurs
for k, v in cm.items():
    print(k, v)
# Modification d'un dictionnaire du chainmap à l'extérieur du chainmap
# Comme celui-ci est passé par référence, la modification est visible dans le chainmap
peinture["La Joconde"] = "Léonard de Vinci"
print(cm.maps)
# Accéder via la clé, remarquez que Metropolis est dans les deux dictionnaires mais le premier trouvé est retourné
print(cm["Metropolis"])
# Recherche dans les dictionnaires
print('La Joconde' in cm)
print("Metropolis" in cm)

# Recherche dans les dictionnaires excluant le premier
print('Full Metal Jacket' in cm.parents)

print(cm["La Joconde"])

