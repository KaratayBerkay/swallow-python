import array, struct
m = memoryview(array.array('H', [32000, 32001, 32002]))
print(repr(m.itemsize))
print(repr(m[0]))
print(repr(struct.calcsize('H') == m.itemsize))
