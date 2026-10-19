## `str.isidentifier`

```
str.isidentifier()
```

Return `True` if the string is a valid identifier according to the language
definition, section [Names (identifiers and keywords)](https://docs.python.org/3.15/reference/lexical_analysis.html#identifiers).

[keyword.iskeyword()](https://docs.python.org/3.15/library/keyword.html#keyword.iskeyword) can be used to test whether string `s` is a reserved
identifier, such as `def` and `class`.

Example:

``` python
>>> from keyword import iskeyword

>>> 'hello'.isidentifier(), iskeyword('hello')
(True, False)
>>> 'def'.isidentifier(), iskeyword('def')
(True, True)
```
> Code: [example_01.py](example_01.py)
