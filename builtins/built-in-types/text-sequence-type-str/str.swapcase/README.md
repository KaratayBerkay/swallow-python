## `str.swapcase`

```
str.swapcase()
```

Return a copy of the string with uppercase characters converted to lowercase and
vice versa. For example:

``` python
>>> 'Hello World'.swapcase()
'hELLO wORLD'
```
> Code: [example_01.py](example_01.py)

Note that it is not necessarily true that `s.swapcase().swapcase() == s`.
For example:

``` python
>>> 'straße'.swapcase().swapcase()
'strasse'
```
> Code: [example_02.py](example_02.py)

See also [str.lower()](../str.lower/README.md) and [str.upper()](../str.upper/README.md).
