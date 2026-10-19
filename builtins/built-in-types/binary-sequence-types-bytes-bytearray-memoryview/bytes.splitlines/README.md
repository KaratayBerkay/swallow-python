## `bytes.splitlines`

```
bytes.splitlines(keepends=False)
bytearray.splitlines(keepends=False)
```

Return a list of the lines in the binary sequence, breaking at ASCII
line boundaries. This method uses the [universal newlines](https://docs.python.org/3.15/glossary.html#term-universal-newlines) approach
to splitting lines. Line breaks are not included in the resulting list
unless *keepends* is given and true.

For example:

``` python
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
[b'ab c', b'', b'de fg', b'kl']
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
[b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']
```
> Code: [example_01.py](example_01.py)

Unlike [split()](../bytes.split/README.md) when a delimiter string *sep* is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line:

``` python
>>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
([b''], [b'Two lines', b''])
>>> b"".splitlines(), b"One line\n".splitlines()
([], [b'One line'])
```
> Code: [example_02.py](example_02.py)
