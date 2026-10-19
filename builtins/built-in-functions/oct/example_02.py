print(repr(('%#o' % 10, '%o' % 10)))
print(repr((format(10, '#o'), format(10, 'o'))))
print(repr((f'{10:#o}', f'{10:o}')))
