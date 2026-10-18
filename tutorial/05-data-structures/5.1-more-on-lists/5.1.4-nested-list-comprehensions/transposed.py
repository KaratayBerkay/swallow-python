from .matrix import matrix

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
