## `str.isupper`

```
str.isupper()
```

Return `True` if all cased characters [^1] in the string are uppercase and
there is at least one cased character, `False` otherwise.

``` python
>>> 'BANANA'.isupper()
True
>>> 'banana'.isupper()
False
>>> 'baNana'.isupper()
False
>>> ' '.isupper()
False
```
> Code: [example_01.py](example_01.py)

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).
