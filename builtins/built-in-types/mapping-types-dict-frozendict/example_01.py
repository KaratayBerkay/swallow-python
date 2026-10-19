dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()
# iteration
n = 0
for val in values:
    n += val
print(n)
# keys and values are iterated over in the same order (insertion order)
print(repr(list(keys)))
print(repr(list(values)))
# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
print(repr(list(keys)))
# set operations
print(repr(keys & {'eggs', 'bacon', 'salad'}))
print(repr(keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}))
print(repr(keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}))
# get back a read-only proxy for the original dictionary
print(repr(values.mapping))
print(repr(values.mapping['spam']))
