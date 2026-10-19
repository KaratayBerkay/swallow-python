b = bytearray(b'zyz')
x = memoryview(b)
x[0] = b'a'
y = x.cast('c')
y[0] = b'a'
print(repr(b))
