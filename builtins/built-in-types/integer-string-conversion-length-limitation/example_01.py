import sys
sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
_ = int('2' * 5432)
i = int('2' * 4300)
print(repr(len(str(i))))
i_squared = i*i
print(repr(len(str(i_squared))))
print(repr(len(hex(i_squared))))
assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.
