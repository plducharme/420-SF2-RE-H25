# Définition d'ensembles
fruits = {'banane', 'pomme', 'poire', 'bleuet', 'fraise'}

panier = {'banane', 'bleuet', 'lait', 'pomme', 'beurre'}

garde_manger = set(['banane', 'poire'])

frigidaire = {x for x in panier if x not in garde_manger}
print(frigidaire)

# fruits dans panier moins ceux dans fruits (différence)
print(panier - fruits)

# fruits dans fruits moins ceux dans panier
print(fruits - panier)

# items dans fruits ou panier (union)
print(panier | fruits)

# items dans fruits et panier (intersection)
print(panier & fruits)

# items exclusivement dans le panier ou dans fruits (XOR)
print(panier ^ fruits)

# union entre fruits et panier (|)
print(fruits.union(panier))
# union entre fruits et itérable
print(fruits.union(('mure', 'pomme', 'mangue')))
