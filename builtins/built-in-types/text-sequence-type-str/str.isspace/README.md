## `str.isspace`

```
str.isspace()
```

Return `True` if there are only whitespace characters in the string and there is
at least one character, `False` otherwise.

For example:

``` python
>>> ''.isspace()
False
>>> ' '.isspace()
True
>>> '\t\n'.isspace() # TAB and BREAK LINE
True
>>> '\u3000'.isspace() # IDEOGRAPHIC SPACE
True
```
> Code: [example_01.py](example_01.py)

A character is *whitespace* if in the Unicode character database
(see [unicodedata](https://docs.python.org/3.15/library/unicodedata.html#module-unicodedata)), either its general category is `Zs`
("Separator, space"), or its bidirectional class is one of `WS`,
`B`, or `S`.

See also `isprintable()`.
