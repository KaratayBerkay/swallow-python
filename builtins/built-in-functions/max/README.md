## `max()`

```
max(iterable, /, *, key=None)
max(iterable, /, *, default, key=None)
max(arg1, arg2, /, *args, key=None)
```

Return the largest item in an iterable or the largest of two or more
arguments.

If one positional argument is provided, it should be an [iterable](https://docs.python.org/3.15/glossary.html#term-iterable).
The largest item in the iterable is returned.  If two or more positional
arguments are provided, the largest of the positional arguments is
returned.

There are two optional keyword-only arguments. The *key* argument specifies
a one-argument ordering function like that used for [list.sort()](https://docs.python.org/3.15/builtins/stdtypes.html#list.sort). The
*default* argument specifies an object to return if the provided iterable is
empty. If the iterable is empty and *default* is not provided, a
[ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised.

If multiple items are maximal, the function returns the first one
encountered.  This is consistent with other sort-stability preserving tools
such as `sorted(iterable, key=keyfunc, reverse=True)[0]` and
`heapq.nlargest(1, iterable, key=keyfunc)`.

> *Changed in version 3.4:* Added the *default* keyword-only parameter.

> *Changed in version 3.8:* The *key* can be `None`.
