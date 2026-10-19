print(repr(b'1,2,3'.split(b',')))
print(repr(b'1,2,3'.split(b',', maxsplit=1)))
print(repr(b'1,2,,3,'.split(b',')))
print(repr(b'1<>2<>3<4'.split(b'<>')))
