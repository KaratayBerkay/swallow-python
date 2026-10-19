## `zip()`

```
zip(*iterables, strict=False)
```

Iterate over several iterables in parallel, producing tuples with an item
from each one.

Example:

``` python
>>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
...     print(item)
...
(1, 'sugar')
(2, 'spice')
(3, 'everything nice')
```
> Code: [example_01.py](example_01.py)

More formally: zip() returns an iterator of tuples, where the *i*-th
tuple contains the *i*-th element from each of the argument iterables.

Another way to think of zip() is that it turns rows into columns, and
columns into rows.  This is similar to [transposing a matrix](https://en.wikipedia.org/wiki/Transpose).

zip() is lazy: The elements won't be processed until the iterable is
iterated on, e.g. by a `for` loop or by wrapping in a
[list](../list/README.md).

One thing to consider is that the iterables passed to zip() could have
different lengths; sometimes by design, and sometimes because of a bug in
the code that prepared these iterables.  Python offers three different
approaches to dealing with this issue:

- By default, zip() stops when the shortest iterable is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted).
  It will ignore the remaining items in the longer iterables, cutting off
  the result to the length of the shortest iterable:

  ``` python
  >>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
  [(0, 'fee'), (1, 'fi'), (2, 'fo')]
  ```
  > Code: [example_02.py](example_02.py)

- zip() is often used in cases where the iterables are assumed to be
  of equal length.  In such cases, it's recommended to use the `strict=True`
  option. Its output is the same as regular zip():

  ``` python
  >>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
  [('a', 1), ('b', 2), ('c', 3)]
  ```
  > Code: [example_03.py](example_03.py)

  Unlike the default behavior, it raises a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) if one iterable
  is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted) before the others:

  ``` python
  >>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  # doctest: +SKIP
  ...     print(item)
  ...
  (0, 'fee')
  (1, 'fi')
  (2, 'fo')
  Traceback (most recent call last):
    ...
  ValueError: zip() argument 2 is longer than argument 1
  ```

  Without the `strict=True` argument, any bug that results in iterables of
  different lengths will be silenced, possibly manifesting as a hard-to-find
  bug in another part of the program.

- Shorter iterables can be padded with a constant value to make all the
  iterables have the same length.  This is done by
  [itertools.zip_longest()](https://docs.python.org/3.15/library/itertools.html#itertools.zip_longest).

Edge cases: With a single iterable argument, zip() returns an
iterator of 1-tuples.  With no arguments, it returns an empty iterator.

Tips and tricks:

- The left-to-right evaluation order of the iterables is guaranteed. This
  makes possible an idiom for clustering a data series into n-length groups
  using `zip(*[iter(s)]*n, strict=True)`.  This repeats the *same* iterator
  `n` times so that each output tuple has the result of `n` calls to the
  iterator. This has the effect of dividing the input into n-length chunks.

- zip() in conjunction with the `*` operator can be used to unzip a
  list:

  ``` python
  >>> x = [1, 2, 3]
  >>> y = [4, 5, 6]
  >>> list(zip(x, y))
  [(1, 4), (2, 5), (3, 6)]
  >>> x2, y2 = zip(*zip(x, y))
  >>> x == list(x2) and y == list(y2)
  True
  ```
  > Code: [example_04.py](example_04.py)

> *Changed in version 3.10:* Added the `strict` argument.
