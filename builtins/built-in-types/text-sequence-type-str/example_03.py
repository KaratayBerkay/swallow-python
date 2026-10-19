from fractions import Fraction
one_third = Fraction(1, 3)
print(repr(f'{one_third:.6f}'))
print(repr(f'{one_third:_^+10}'))
print(repr(f'{one_third!r:_^20}'))
print(repr(f'{one_third = :~>10}~'))
