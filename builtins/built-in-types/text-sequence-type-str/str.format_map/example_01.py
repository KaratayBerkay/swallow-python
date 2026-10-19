class Default(dict):
    def __missing__(self, key):
        return key
print(repr('{name} was born in {country}'.format_map(Default(name='Guido'))))
