## `str.center`

```
str.center(width, fillchar=' ', /)
```

Return centered in a string of length *width*. Padding is done using the
specified *fillchar* (default is an ASCII space). The original string is
returned if *width* is less than or equal to `len(s)`.  For example:

``` python
>>> 'Python'.center(10)
'  Python  '
>>> 'Python'.center(10, '-')
'--Python--'
>>> 'Python'.center(4)
'Python'
```
> Code: [example_01.py](example_01.py)
