## `str.count`

```
str.count(sub[, start[, end]])
```

Return the number of non-overlapping occurrences of substring *sub* in the
range [*start*, *end*].  Optional arguments *start* and *end* are
interpreted as in slice notation.

If *sub* is empty, returns the number of empty strings between characters
which is the length of the string plus one. For example:

``` python
>>> 'spam, spam, spam'.count('spam')
3
>>> 'spam, spam, spam'.count('spam', 5)
2
>>> 'spam, spam, spam'.count('spam', 5, 10)
1
>>> 'spam, spam, spam'.count('eggs')
0
>>> 'spam, spam, spam'.count('')
17
```
> Code: [example_01.py](example_01.py)
