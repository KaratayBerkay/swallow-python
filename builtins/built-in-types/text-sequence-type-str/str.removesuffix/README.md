## `str.removesuffix`

```
str.removesuffix(suffix, /)
```

If the string ends with the *suffix* string and that *suffix* is not empty,
return `string[:-len(suffix)]`. Otherwise, return a copy of the
original string:

``` python
>>> 'MiscTests'.removesuffix('Tests')
'Misc'
>>> 'TmpDirMixin'.removesuffix('Tests')
'TmpDirMixin'
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.9.*

See also `removeprefix()` and `endswith()`.
