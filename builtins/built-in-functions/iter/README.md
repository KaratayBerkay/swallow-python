## `iter()`

```
iter(iterable, /)
iter(callable, sentinel, /)
```

Return an [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) object.  The first argument is interpreted very
differently depending on the presence of the second argument. Without a
second argument, the single argument must be a collection object which supports the
[iterable](https://docs.python.org/3.15/glossary.html#term-iterable) protocol (the [__iter__()](https://docs.python.org/3.15/reference/datamodel.html#object.__iter__) method),
or it must support
the sequence protocol (the [__getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getitem__) method with integer arguments
starting at `0`).  If it does not support either of those protocols,
[TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) is raised. If the second argument, *sentinel*, is given,
then the first argument must be a callable object.  The iterator created in this case
will call *callable* with no arguments for each call to its
[__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method; if the value returned is equal to
*sentinel*, [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) will be raised, otherwise the value will
be returned.

See also [Iteration-related types](https://docs.python.org/3.15/builtins/stdtypes.html#typeiter).

One useful application of the second form of iter() is to build a
block-reader. For example, reading fixed-width blocks from a binary
database file until the end of file is reached:

``` python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```
