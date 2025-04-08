#Dictionaries, aka dicks, hashes, associative arrays, key:value pairs, you know the drill.
#Indicies have *names* instead of numerical values

ages = { 'bart': 3, 'nutmeg': 5, 'scrungus': 10 }

#Keys in dicts are not mutable, but can be removed via del method. But this is unsafe if you pass the entire dict.

del ages['bart']

#Instead, pop an index off
ages.pop('nutmeg')
print(ages)

#keys() and values() get you those like you'd expect
print(ages.keys())
print(ages.values())