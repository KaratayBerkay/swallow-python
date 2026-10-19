## `str.partition`

```
str.partition(sep, /)
```

Split the string at the first occurrence of *sep*, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
the string itself, followed by two empty strings.

For example:

``` python
>>> 'Monty Python'.partition(' ')
('Monty', ' ', 'Python')
>>> "Monty Python's Flying Circus".partition(' ')
('Monty', ' ', "Python's Flying Circus")
>>> 'Monty Python'.partition('-')
('Monty Python', '', '')
```
> Code: [example_01.py](example_01.py)

See also `rpartition()`.
