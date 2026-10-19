import struct
buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
x = memoryview(buf)
y = x.cast('d', shape=[3,4])
print(repr(y.tolist()))
print(repr(len(y)))
print(repr(y.nbytes))
