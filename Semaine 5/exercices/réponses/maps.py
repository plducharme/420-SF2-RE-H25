import random

mots = ["auto", "école", "patate", "pomme", "ornithorynque", "supercalifragilisticexpialidocious"]
positions = [random.randint(0, len(mots[i]) - 1) for i in range(len(mots))]

print(positions)

resultat = list(map(lambda mots, positions: mots[0:positions] + mots[positions].upper() + mots[positions+1:], mots, positions))
print(resultat)