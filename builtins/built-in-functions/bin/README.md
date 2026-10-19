## `bin()`

```
bin(integer, /)
```

Convert an integer number to a binary string prefixed with "0b". The result
is a valid Python expression. If *integer* is not a Python [int](../int/README.md) object, it
has to define an [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method that returns an integer. Some
examples:

``` python
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
```
> Code: [example_01.py](example_01.py)

If the prefix "0b" is desired or not, you can use either of the following ways.

``` python
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')
```
> Code: [example_02.py](example_02.py)

See also [enum.bin()](https://docs.python.org/3.15/library/enum.html#enum.bin) to represent negative values as twos-complement.

See also [format()](../format/README.md) for more information.
