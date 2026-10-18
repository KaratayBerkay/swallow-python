"""Representation Error: Why 0.1 is not exactly representable in binary floating point."""

# 1/10 ~= J / (2**N), where J is an integer with exactly 53 bits

N = 56
assert 2**52 <= 2**N // 10 < 2**53

# Best J by rounding the quotient
q, r = divmod(2**N, 10)
print(r)  # 6

# Remainder > half of 10, so round up
J = q + 1
print(J)  # 7205759403792794

# Best approximation to 1/10 in IEEE 754 double precision:
print(J / 2**N)

# Reduced form: divide numerator and denominator by 2
J_half = J // 2
N_half = N - 1
print(J_half / 2**N_half)  # 3602879701896397 / 2**55

# Verify: multiply float 0.1 by 2**55 to see the stored integer
print(0.1 * 2**55)  # 3602879701896397.0

# Full decimal expansion of stored value:
print(J_half * 10**N_half // 2**N_half)

# What Python displays (rounded to 17 significant digits):
print(format(0.1, '.17f'))  # '0.10000000000000001'
