# remarquer l'import du built-in Enum
from enum import Enum


class Saison(Enum):
    PRINTEMPS = 1
    ETE = 2
    AUTOMNE = 3
    HIVER = 4

print(Saison.PRINTEMPS)
print(Saison.PRINTEMPS.name)
print(Saison.PRINTEMPS.value)
print(type(Saison.HIVER))

