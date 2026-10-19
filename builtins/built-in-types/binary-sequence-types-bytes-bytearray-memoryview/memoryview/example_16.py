b  = bytearray(b'xyz')
m = memoryview(b)
print(repr(m.obj is b))
