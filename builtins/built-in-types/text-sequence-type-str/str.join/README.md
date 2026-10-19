## `str.join`

```
str.join(iterable, /)
```

Return a string which is the concatenation of the strings in *iterable*.
A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) will be raised if there are any non-string values in
*iterable*, including [bytes](../../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) objects.  The separator between
elements is the string providing this method. For example:

``` python
>>> ', '.join(['spam', 'spam', 'spam'])
'spam, spam, spam'
>>> '-'.join('Python')
'P-y-t-h-o-n'
```
> Code: [example_01.py](example_01.py)

See also `split()`.
