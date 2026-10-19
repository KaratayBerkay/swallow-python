from keyword import iskeyword
print(repr(('hello'.isidentifier(), iskeyword('hello'))))
print(repr(('def'.isidentifier(), iskeyword('def'))))
