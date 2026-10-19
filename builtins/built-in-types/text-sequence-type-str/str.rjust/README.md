## `str.rjust`

```
str.rjust(width, fillchar=' ', /)
```

Return the string right justified in a string of length *width*. Padding is
done using the specified *fillchar* (default is an ASCII space). The
original string is returned if *width* is less than or equal to `len(s)`.

For example:

``` python
>>> 'Python'.rjust(10)
'    Python'
>>> 'Python'.rjust(10, '.')
'....Python'
>>> 'Monty Python'.rjust(10, '.')
'Monty Python'
```
> Code: [example_01.py](example_01.py)

See also `ljust()` and `zfill()`.
