value = b'\xf0\xf1\xf2'
print(repr(value.hex('-')))
print(repr(value.hex('_', 2)))
print(repr(b'UUDDLRLRAB'.hex(' ', -4)))
