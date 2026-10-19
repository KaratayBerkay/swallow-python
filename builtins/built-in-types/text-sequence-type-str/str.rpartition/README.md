## `str.rpartition`

```
str.rpartition(sep, /)
```

Split the string at the last occurrence of *sep*, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
two empty strings, followed by the string itself.

For example:

``` python
>>> 'Monty Python'.rpartition(' ')
('Monty', ' ', 'Python')
>>> "Monty Python's Flying Circus".rpartition(' ')
("Monty Python's Flying", ' ', 'Circus')
>>> 'Monty Python'.rpartition('-')
('', '', 'Monty Python')
```
> Code: [example_01.py](example_01.py)

See also `partition()`.
