tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
tel['irv']
print(tel.get('irv'))
del tel['sape']
tel['irv'] = 4127
tel
list(tel)
sorted(tel)
'guido' in tel
'jack' not in tel
