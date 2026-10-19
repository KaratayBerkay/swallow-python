## `BaseException`

```
BaseException
```

The base class for all built-in exceptions.  It is not meant to be directly
inherited by user-defined classes (for that, use [Exception](../Exception/README.md)).  If
[str()](../../../built-in-functions/str/README.md) is called on an instance of this class, the representation of
the argument(s) to the instance are returned, or the empty string when
there were no arguments.

### args

The tuple of arguments given to the exception constructor.  Some built-in
exceptions (like [OSError](../../concrete-exceptions/OSError/README.md)) expect a certain number of arguments and
assign a special meaning to the elements of this tuple, while others are
usually called only with a single string giving an error message.

### with_traceback(tb)

This method sets *tb* as the new traceback for the exception and returns
the exception object.  It was more commonly used before the exception
chaining features of [PEP 3134](https://peps.python.org/pep-3134/) became available.  The following example
shows how we can convert an instance of `SomeException` into an
instance of `OtherException` while preserving the traceback.  Once
raised, the current frame is pushed onto the traceback of the
`OtherException`, as would have happened to the traceback of the
original `SomeException` had we allowed it to propagate to the caller.

``` python
try:
    ...
except SomeException:
    tb = sys.exception().__traceback__
    raise OtherException(...).with_traceback(tb)
```

### __traceback__

A writable field that holds the
[traceback object](https://docs.python.org/3.15/reference/datamodel.html#traceback-objects) associated with this
exception. See also: [The raise statement](https://docs.python.org/3.15/reference/simple_stmts.html#raise).

### add_note(note)

Add the string `note` to the exception's notes which appear in the standard
traceback after the exception string. A [TypeError](../../concrete-exceptions/TypeError/README.md) is raised if `note`
is not a string.

> *Added in version 3.11.*

### __notes__

A list of the notes of this exception, which were added with `add_note()`.
This attribute is created when `add_note()` is called.

> *Added in version 3.11.*
