## `str.isalnum`

```
str.isalnum()
```

Return `True` if all characters in the string are alphanumeric and there is at
least one character, `False` otherwise.  A character `c` is alphanumeric if one
of the following returns `True`: `c.isalpha()`, `c.isdecimal()`,
`c.isdigit()`, or `c.isnumeric()`. For example:

``` python
>>> 'abc123'.isalnum()
True
>>> 'abc123!@#'.isalnum()
False
>>> ''.isalnum()
False
>>> ' '.isalnum()
False
```
> Code: [example_01.py](example_01.py)
