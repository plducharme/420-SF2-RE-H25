import array
import sys

arr = array.array('i', (1, 2, 8, 9, 4))

# Supprimer l'élément à l'index 1
del arr[1]
print(arr)

arr.append(42)
print(arr)

arr[0] = 7
print(arr)


# Comparaison avec une liste normale
liste_normale = [x for x in range(1, 1000)]
print(str(sys.getsizeof(liste_normale)) + " bytes")
# Tableau d'entiers
arr2 = array.array('i', liste_normale)
print(str(sys.getsizeof(arr2)) + " bytes")







