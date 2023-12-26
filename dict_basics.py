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


