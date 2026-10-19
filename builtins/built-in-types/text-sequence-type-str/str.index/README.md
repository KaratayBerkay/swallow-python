## `str.index`

```
str.index(sub[, start[, end]])
```

Like [find()](../str.find/README.md), but raise [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the substring is
not found. For example:

``` python
>>> 'spam, spam, spam'.index('spam')
0
>>> 'spam, spam, spam'.index('eggs')
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    'spam, spam, spam'.index('eggs')
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: substring not found
```
> Code: [example_01.py](example_01.py)

See also `rindex()`.
