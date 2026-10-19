m = memoryview(bytearray(b'abc'))
mm = m.toreadonly()
print(repr(mm.tolist()))
mm[0] = 42
m[0] = 43
print(repr(mm.tolist()))
