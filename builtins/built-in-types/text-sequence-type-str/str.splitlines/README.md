## `str.splitlines`

```
str.splitlines(keepends=False)
```

Return a list of the lines in the string, breaking at line boundaries.  Line
breaks are not included in the resulting list unless *keepends* is given and
true.

This method splits on the following line boundaries.  In particular, the
boundaries are a superset of [universal newlines](https://docs.python.org/3.15/glossary.html#term-universal-newlines).

| Representation | Description |
| --- | --- |
| `\n` | Line Feed |
| `\r` | Carriage Return |
| `\r\n` | Carriage Return + Line Feed |
| `\v` or `\x0b` | Line Tabulation |
| `\f` or `\x0c` | Form Feed |
| `\x1c` | File Separator |
| `\x1d` | Group Separator |
| `\x1e` | Record Separator |
| `\x85` | Next Line (C1 Control Code) |
| `\u2028` | Line Separator |
| `\u2029` | Paragraph Separator |

> *Changed in version 3.2:* `\v` and `\f` added to list of line boundaries.

For example:

``` python
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```
> Code: [example_01.py](example_01.py)

Unlike [split()](../str.split/README.md) when a delimiter string *sep* is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line:

``` python
>>> "".splitlines()
[]
>>> "One line\n".splitlines()
['One line']
```
> Code: [example_02.py](example_02.py)

For comparison, `split('\n')` gives:

``` python
>>> ''.split('\n')
['']
>>> 'Two lines\n'.split('\n')
['Two lines', '']
```
> Code: [example_03.py](example_03.py)
