from fractions import Fraction
one_third = Fraction(1, 3)
print(repr(f'{one_third}'))
print(repr(f'{one_third = }'))
print(repr(str(one_third)))
print(repr(repr(one_third)))
print(repr(f'{one_third!s} is {one_third!r}'))
string = "¡kočka 😸!"
print(repr(ascii(string)))
print(repr(f'{string = !a}'))
