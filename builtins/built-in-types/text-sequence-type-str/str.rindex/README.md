## `str.rindex`

```
str.rindex(sub[, start[, end]])
```

Like `rfind()` but raises [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the substring *sub* is not
found.
For example:

``` python
>>> 'spam, spam, spam'.rindex('spam')
12
>>> 'spam, spam, spam'.rindex('eggs')
Traceback (most recent call last):
  File "<stdin-0>", line 1, in <module>
    'spam, spam, spam'.rindex('eggs')
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: substring not found
```
> Code: [example_01.py](example_01.py)

See also `index()` and `find()`.
