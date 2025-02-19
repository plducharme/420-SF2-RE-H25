import random

mots = ["auto", "école", "patate", "pomme", "ornithorynque", "supercalifragilisticexpialidocious"]
positions = [random.randint(0, len(mots[i]) - 1) for i in range(len(mots))]

print(positions)

