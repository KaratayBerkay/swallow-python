## `hex()`

```
hex(integer, /)
```

Convert an integer number to a lowercase hexadecimal string prefixed with
"0x". If *integer* is not a Python [int](../int/README.md) object, it has to define an
[__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method that returns an integer. Some examples:

``` python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```
> Code: [example_01.py](example_01.py)

If you want to convert an integer number to an uppercase or lower hexadecimal
string with prefix or not, you can use either of the following ways:

``` python
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```
> Code: [example_02.py](example_02.py)

See also [format()](../format/README.md) for more information.

See also `int()` for converting a hexadecimal string to an
integer using a base of 16.

> **Note**
>
> To obtain a hexadecimal string representation for a float, use the
> [float.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#float.hex) method.
