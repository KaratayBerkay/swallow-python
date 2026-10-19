## `str.rfind`

```
str.rfind(sub[, start[, end]])
```

Return the highest index in the string where substring *sub* is found, such
that *sub* is contained within `s[start:end]`.  Optional arguments *start*
and *end* are interpreted as in slice notation.  Return `-1` on failure.
For example:

``` python
>>> 'spam, spam, spam'.rfind('sp')
12
>>> 'spam, spam, spam'.rfind('sp', 0, 10)
6
```
> Code: [example_01.py](example_01.py)

See also `find()` and `rindex()`.
