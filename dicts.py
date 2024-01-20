# Dictionaries (Dicts) are datastores. They function like JSON objects.

sub_dict = {
    'foo': 'bar',
    'foos': ['foo', 'bar']
}

example_dict = {
    'key1': 'value1',
    'key2': 9,
    'key3': sub_dict
}

# You can access keys directly:
print(example_dict['key2'])
print(example_dict['key3']['foo'])
print(example_dict['key3']['foos'][0])

# New variable pointing to a Dict value is a deep copy
ex_value = example_dict['key1']
print(ex_value)
example_dict['key1'] = 'value2'
print(ex_value)
print(example_dict['key1'])
ex_value = example_dict['key1']
print(ex_value)

# New KVPs can be directly assigned
example_dict['key4'] = False
sub_dict['faz'] = ['baz']
print(example_dict)

# Dicts can start empty
fresh_dict = {}

# Simple example
fresh_dict['x-pos'] = 0
fresh_dict['y-pos'] = 25
fresh_dict['speed'] = 'medium'

print(f"Original position of Unit: {fresh_dict['x-pos']}")

if (fresh_dict['speed'] == 'slow'):
    fresh_dict['x-pos'] += 1
elif(fresh_dict['speed'] == 'medium'):
    fresh_dict['x-pos'] += 2
elif(fresh_dict['speed'] == 'fast'):
    fresh_dict['x-pos'] += 3
else:
    print('Invalid speed')

print(f"New Position: {fresh_dict['x-pos']}")


# KVPs can be removed with del statements
del fresh_dict['y-pos']
print(fresh_dict)

# The .get() method has a built in error response argument
print(fresh_dict.get('x-pos', 'No x-pos found'))
print(fresh_dict.get('y-pos', 'No y-pos found'))

# The .get() method will return None if no second argument is provided for an invalid search
# None is a datatype
print(fresh_dict.get('y-pos'))

# You can use a for loop to iterate over a Dict, but will need to assigned a playholder for both the key and the value
# You will also need to use the DICT.items() method, which returns a Tuple containing a List of the KVPs
for key,value in example_dict.items():
    print(f"Key: {key}, Value: {value}")

print(example_dict.items())

# You can also use the .keys() and .values() methods to just return arrays of the keys/values respectively
print(example_dict.keys())
print(example_dict.values())

# A For loop iterating over a Dict without a method call will default to iterating over the keys
for key in example_dict:
    print(key)

# Since these are all Lists, we can use the sorted() function ahead of iteration if we want
for key in sorted(example_dict, reverse=True):
    print(key)


big_dict_energy = []

for index in range(30):
    new_car = {
        'Maker': 'Toyota',
        'Year': 1999,
        'Color': "Yellow"
    }

    big_dict_energy.append(new_car)

print(len(big_dict_energy))

for index in range(len(big_dict_energy)):
    if (len(big_dict_energy) - index)%3 == 0:
        big_dict_energy[index]['Year'] = 2008

    if (len(big_dict_energy) - index)%2 == 0:
        big_dict_energy[index]['Maker'] = 'Ford'

    if (len(big_dict_energy) - index)%4 == 0:
        big_dict_energy[index]['Color'] = 'Blue'
    elif(len(big_dict_energy) - index)%4 == 1:
        big_dict_energy[index]['Color'] = 'Red'

for car in big_dict_energy[1:13]:
    print(car)


