import array
a = array.array('i', [1,2,3,4,5])
m = memoryview(a)
print(repr(len(m)))
print(repr(m.nbytes))
y = m[::2]
print(repr(len(y)))
print(repr(y.nbytes))
print(repr(len(y.tobytes())))
