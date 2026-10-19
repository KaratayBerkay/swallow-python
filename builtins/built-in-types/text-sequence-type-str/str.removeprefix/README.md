## `str.removeprefix`

```
str.removeprefix(prefix, /)
```

If the string starts with the *prefix* string, return
`string[len(prefix):]`. Otherwise, return a copy of the original
string:

``` python
>>> 'TestHook'.removeprefix('Test')
'Hook'
>>> 'BaseTestCase'.removeprefix('Test')
'BaseTestCase'
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.9.*

See also `removesuffix()` and `startswith()`.
