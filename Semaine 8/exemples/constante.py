import array

arr = array.array('i', [3, 4, 6, 8, 9, 1, 7])


def constante(x):
    return 6


resultats = [constante(x) for x in arr]
print(resultats)

