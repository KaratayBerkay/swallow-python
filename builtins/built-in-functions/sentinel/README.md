## `sentinel()`

```
sentinel(name, /, *, repr=None)
```

Return a new unique sentinel object.  *name* must be a [str](../str/README.md), and is
used by default as the returned object's representation:

``` python
>>> MISSING = sentinel("MISSING")
>>> MISSING
MISSING
```
> Code: [example_01.py](example_01.py)

The optional *repr* argument can be used to specify a different representation:

``` python
>>> MISSING = sentinel("MISSING", repr="<MISSING>")
>>> MISSING
<MISSING>
```
> Code: [example_02.py](example_02.py)

Sentinel objects are truthy and compare equal only to themselves.  They are
intended to be compared with the `is` operator.

`sentinel` does not support subclassing.

Shallow and deep copies of a sentinel object return the object itself.

Sentinels are conventionally assigned to a variable with a matching name.
Sentinels defined in this way can be used in [type hints](https://docs.python.org/3.15/glossary.html#term-type-hint):

``` python
MISSING = sentinel("MISSING")

def next_value(default: int | MISSING = MISSING):
    ...
```

Sentinel objects support the [|](https://docs.python.org/3.15/reference/expressions.html#bitwise) operator for use in type expressions.

[Pickling](https://docs.python.org/3.15/library/pickle.html#module-pickle) is supported for sentinel objects that are
placed in the global scope of a module under a name matching the sentinel's
name, and for sentinels placed in class scopes with a name matching the
[qualified name](https://docs.python.org/3.15/glossary.html#term-qualified-name) of the sentinel. Other sentinels, such as those
defined in a function scope, are not picklable. The identity of the sentinel is preserved
after pickling:

``` python
import pickle

PICKLABLE = sentinel("PICKLABLE")

assert pickle.loads(pickle.dumps(PICKLABLE)) is PICKLABLE

class Cls:
    PICKLABLE = sentinel("Cls.PICKLABLE")

assert pickle.loads(pickle.dumps(Cls.PICKLABLE)) is Cls.PICKLABLE
```

Sentinel objects have the following attributes:

### __name__

The sentinel's name.

### __module__

The name of the module where the sentinel was created. This attribute is writable.

> *Added in version 3.15.*
