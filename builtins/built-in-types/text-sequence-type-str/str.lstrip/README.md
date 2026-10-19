## `str.lstrip`

```
str.lstrip(chars=None, /)
```

Return a copy of the string with leading characters removed.  The *chars*
argument is a string specifying the set of characters to be removed.  If omitted
or `None`, the *chars* argument defaults to removing whitespace.  The *chars*
argument is not a prefix; rather, all combinations of its values are stripped:

``` python
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
```
> Code: [example_01.py](example_01.py)

See [str.removeprefix()](../str.removeprefix/README.md) for a method that will remove a single prefix
string rather than all of a set of characters.  For example:

``` python
>>> 'Arthur: three!'.lstrip('Arthur: ')
'ee!'
>>> 'Arthur: three!'.removeprefix('Arthur: ')
'three!'
```
> Code: [example_02.py](example_02.py)
