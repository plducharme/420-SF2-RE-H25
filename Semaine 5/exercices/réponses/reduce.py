import functools

mots = ["programmation", "code", "prorogation", "procrastination", "proclamation", "protection", "coder", "amas", "amasser"]



# Obtenir le total des valeurs ascii des lettres d'un mot en utilisant la fonction reduce
def total_ascii(mot):
    # Une str est déjà un itérable, on peut donc l'utiliser directement. Pour avoir la valeur en ascii d'une lettre, on
    # doit d'abord l'encoder en ascii car par défaut, une str est en unicode. Pour les valeurs en bas de 128, l'encodage
    # ascii est le même que l'encodage unicode.
    return functools.reduce(lambda total, lettre: total + ord(lettre), mot.encode("ascii").decode(), 0)

# Pour une liste de mots, avec une boucle for
total = 0
for mot in mots:
    total += total_ascii(mot)
print(total)


# Pour une liste de mots, avec la fonction reduce
# On utilise la fonction map pour obtenir une liste des totaux ascii de chaque mot
# On utilise ensuite la fonction reduce pour obtenir le total de ces totaux
total = functools.reduce(lambda total, mot: total + mot, map(total_ascii, mots), 0)
print(total)







