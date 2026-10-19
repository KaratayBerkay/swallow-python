m = memoryview(b"abc")
print(repr(m.tobytes()))
print(repr(bytes(m)))
