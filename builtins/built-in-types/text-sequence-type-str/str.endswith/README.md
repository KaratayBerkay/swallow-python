## `str.endswith`

```
str.endswith(suffix[, start[, end]])
```

Return `True` if the string ends with the specified *suffix*, otherwise return
`False`.  *suffix* can also be a tuple of suffixes to look for.  With optional
*start*, test beginning at that position.  With optional *end*, stop comparing
at that position. Using *start* and *end* is equivalent to
`str[start:end].endswith(suffix)`. For example:

``` python
>>> 'Python'.endswith('on')
True
>>> 'a tuple of suffixes'.endswith(('at', 'in'))
False
>>> 'a tuple of suffixes'.endswith(('at', 'es'))
True
>>> 'Python is amazing'.endswith('is', 0, 9)
True
```
> Code: [example_01.py](example_01.py)

See also `startswith()` and `removesuffix()`.
