d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(repr(d))
print(repr(list(d)))
print(repr(list(d.values())))
d["one"] = 42
print(repr(d))
del d["two"]
d["two"] = None
print(repr(d))
