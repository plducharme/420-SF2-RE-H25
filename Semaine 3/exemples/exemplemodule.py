import math as m
from datetime import date
import json
from pprint import *
from examplepackage.sysutils import *
from examplepackage import example


print(m.pi)
sysutils.afficher_chemin_python()
print(date.today())

json_string = {"nom": "Alice", "age": 18, "qualite": {"gentil": True}}
pprint(json.dumps(json_string, indent=6))
classe_ex = example.UneClasse()

print(__name__)
