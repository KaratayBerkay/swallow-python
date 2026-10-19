data = bytearray(b'abcefg')
v = memoryview(data)
print(repr(v.readonly))
v[0] = ord(b'z')
print(repr(data))
v[1:4] = b'123'
print(repr(data))
v[2:3] = b'spam'
v[2:6] = b'spam'
print(repr(data))
