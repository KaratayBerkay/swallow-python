m = memoryview(b'abc')
m.release()
print(repr(m[0]))
