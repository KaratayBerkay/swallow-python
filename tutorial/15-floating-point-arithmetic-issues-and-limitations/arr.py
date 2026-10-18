import math
from fractions import Fraction

arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16, -143401161400469.7, 266262841.31058735, -0.003244936839808227]
float(sum(map(Fraction, arr)))   # Exact summation with single rounding
math.fsum(arr)                   # Single rounding
sum(arr)                         # Multiple roundings in extended precision
total = 0.0
for x in arr:
    total += x                   # Multiple roundings in standard precision

total                            # Straight addition has no correct digits!
