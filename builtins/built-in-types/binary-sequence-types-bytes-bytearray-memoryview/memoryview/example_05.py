import array
a = array.array('I', [1, 2, 3, 4, 5])
b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
c = array.array('b', [5, 3, 1])
x = memoryview(a)
y = memoryview(b)
print(repr(x == a == y == b))
print(repr(x.tolist() == a.tolist() == y.tolist() == b.tolist()))
z = y[::-2]
print(repr(z == c))
print(repr(z.tolist() == c.tolist()))
