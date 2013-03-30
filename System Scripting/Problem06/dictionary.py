#Dictionary -> key - value
details = {'name': 'John', 'age':20, 'married': False}

print details

#Print value corresponding to the key 'name'
print details['name']

#changing values of a key
details['age'] = 25
print details['age']

for keys in details.keys():
    print keys, "->", details[keys]