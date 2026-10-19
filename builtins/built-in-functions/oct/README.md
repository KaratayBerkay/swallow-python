## `oct()`

```
oct(integer, /)
```

Convert an integer number to an octal string prefixed with "0o".  The result
is a valid Python expression. If *integer* is not a Python [int](../int/README.md) object, it
has to define an [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method that returns an integer. For
example:

``` python
>>> oct(8)
'0o10'
>>> oct(-56)
'-0o70'
```
> Code: [example_01.py](example_01.py)

If you want to convert an integer number to an octal string either with the prefix
"0o" or not, you can use either of the following ways.

``` python
>>> '%#o' % 10, '%o' % 10
('0o12', '12')
>>> format(10, '#o'), format(10, 'o')
('0o12', '12')
>>> f'{10:#o}', f'{10:o}'
('0o12', '12')
```
> Code: [example_02.py](example_02.py)

See also [format()](../format/README.md) for more information.
