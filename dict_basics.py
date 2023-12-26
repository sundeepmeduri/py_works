# create a dict

mydict = dict()

print('\n--create dict--------------')
print(type(mydict))
print(mydict)

mydict['type'] = 'honda'
mydict['model'] = 'crv'
mydict['year'] = 2015
print(mydict)

temp_dict = {'year': 2025, 'model': 'high end', 'type': 'range rover', 'price': 100000}

mydict.update(temp_dict)
print(mydict)

print('\n--another way to create dict-------------')

mydict2 = dict(name='sunny', age=36, country='usa')
print(mydict2)
print(type(mydict2))
mydict2['role'] = 'developer'
print(mydict2)

print('\n-- access items------------')

print(mydict)
key_list = mydict.keys()
value_list = mydict.values()

for key in key_list:
    print(key)

for val in value_list:
    print(val)

p = mydict['price']
print('price is:', p)

# get a key
# x = mydict['milage'] # this gives error

if mydict.get('milage') is None:
    print('milage is not present in mydict')
    mydict['milage'] = 25
    print(mydict)

print(key_list)  # milage is included automatically
print(value_list)  # milage value is also added dynamically

items = mydict.items()

print(items)
mydict['color'] = 'white'
print(items)

for item in items:
    print(item, type(item))

for key, val in items:
    print(key, val)

print('\n--- change dict------------')
print(mydict)
mydict['color'] = 'gold'
print(mydict)

mydict_update = {'milage': 22, 'price': 120000}
mydict.update(mydict_update)
print(mydict)

print('\n----add items------')
mydict_update['horse power'] = 550
mydict.update(mydict_update)
print(mydict)

mydict['seats'] = 4
print(mydict)

print('\n----del items-------------')
mydict1 = dict()
for key, val in mydict.items():
    mydict1[key] = val

print(mydict1)
del mydict1['model']
mydict1.pop('milage')
print('1', mydict1)
print('0', mydict)

mydict1.clear()
print(mydict1)

mydict1 = mydict.copy()  # right way to do copy
print(mydict1)
del mydict1['model']
print('mydict1', mydict1)
print('mydict', mydict)

mydict2 = dict(mydict)  # another way to copy dict
print('mydic2', mydict2)
print('mydict', mydict)

print('\n----nested dict-------------')
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

for mem in myfamily:
    print('-----', mem)
    curr_mem = myfamily[mem]
    for key, val in curr_mem.items():
        print(key, val)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfam = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print('\n---------')
for key in myfam:
    print(key)
    curr_mem = myfam[key]
    for k, val in curr_mem.items():
        print(k, val)

'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''