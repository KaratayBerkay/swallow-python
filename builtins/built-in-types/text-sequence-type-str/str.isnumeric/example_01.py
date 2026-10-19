print(repr('0123456789'.isnumeric()))
print(repr('٠١٢٣٤٥٦٧٨٩'.isnumeric()))
print(repr('⅕'.isnumeric()))
print(repr(('²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric())))
