x = [1, 2, 3]
y = [4, 5, 6]
print(repr(list(zip(x, y))))
x2, y2 = zip(*zip(x, y))
print(repr(x == list(x2) and y == list(y2)))
