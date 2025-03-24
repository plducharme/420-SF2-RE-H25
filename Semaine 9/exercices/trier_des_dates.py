import random


def generer_date() -> str:
    annee = random.randint(2023, 2025)
    mois = random.randint(1, 12)
    jour = None
    if mois == 2:
        jour = random.randint(1, 28)
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        jour = random.randint(1, 31)
    else:
        jour = random.randint(1, 30)
    return f"{jour}/{mois}/{annee}"

listes_des_dates = [generer_date() for _ in range(20)]

# Implémenter la classe Date et le tri par insertion


