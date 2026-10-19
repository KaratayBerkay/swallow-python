## `int.bit_count`

```
int.bit_count()
```

Return the number of ones in the binary representation of the absolute
value of the integer. This is also known as the population count.
Example:

``` python
>>> n = 19
>>> bin(n)
'0b10011'
>>> n.bit_count()
3
>>> (-n).bit_count()
3
```
> Code: [example_01.py](example_01.py)

Equivalent to:

``` python
def bit_count(self):
    return bin(self).count("1")
```

> *Added in version 3.10.*
