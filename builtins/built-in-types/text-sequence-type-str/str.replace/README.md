## `str.replace`

```
str.replace(old, new, /, count=-1)
```

Return a copy of the string with all occurrences of substring *old* replaced by
*new*.  If *count* is given, only the first *count* occurrences are replaced.
If *count* is not specified or `-1`, then all occurrences are replaced.
For example:

``` python
>>> 'spam, spam, spam'.replace('spam', 'eggs')
'eggs, eggs, eggs'
>>> 'spam, spam, spam'.replace('spam', 'eggs', 1)
'eggs, spam, spam'
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.13:* *count* is now supported as a keyword argument.
