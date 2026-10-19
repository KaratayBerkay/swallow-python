v = memoryview(b'abcefg')
print(repr(hash(v) == hash(b'abcefg')))
print(repr(hash(v[2:4]) == hash(b'ce')))
print(repr(hash(v[::-2]) == hash(b'abcefg'[::-2])))
