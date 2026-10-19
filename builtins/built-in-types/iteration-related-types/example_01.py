def count_to_three():
    yield 0
    yield 1
    yield 2
    yield 3
print(repr(count_to_three()))
for number in count_to_three():
    print(number)
print(repr(list(count_to_three())))
