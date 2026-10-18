t = 12345, 54321, 'hello!'
t[0]
t
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# Tuples are immutable:
t[0] = 88888
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# they support unpacking just like lists:
x = [1, 2, 3]
0, *x, 4
