## `str.format_map`

```
str.format_map(mapping, /)
```

Similar to `str.format(**mapping)`, except that `mapping` is
used directly and not copied to a [dict](../../mapping-types-dict-frozendict/dict/README.md).  This is useful
if for example `mapping` is a dict subclass:

``` python
>>> class Default(dict):
...     def __missing__(self, key):
...         return key
...
>>> '{name} was born in {country}'.format_map(Default(name='Guido'))
'Guido was born in country'
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.2.*
