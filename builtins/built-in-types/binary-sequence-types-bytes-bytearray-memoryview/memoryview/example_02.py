import array
a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(repr(m[0]))
print(repr(m[-1]))
print(repr(m[::2].tolist()))
