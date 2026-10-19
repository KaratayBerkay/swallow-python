## `ExceptionGroup`

```
ExceptionGroup(msg, excs)
BaseExceptionGroup(msg, excs)
```

Both of these exception types wrap the exceptions in the sequence `excs`.
The `msg` parameter must be a string. The difference between the two
classes is that BaseExceptionGroup extends [BaseException](../../base-classes/BaseException/README.md) and
it can wrap any exception, while ExceptionGroup extends [Exception](../../base-classes/Exception/README.md)
and it can only wrap subclasses of [Exception](../../base-classes/Exception/README.md). This design is so that
`except Exception` catches an ExceptionGroup but not
BaseExceptionGroup.

The BaseExceptionGroup constructor returns an ExceptionGroup
rather than a BaseExceptionGroup if all contained exceptions are
[Exception](../../base-classes/Exception/README.md) instances, so it can be used to make the selection
automatic. The ExceptionGroup constructor, on the other hand,
raises a [TypeError](../../concrete-exceptions/TypeError/README.md) if any contained exception is not an
[Exception](../../base-classes/Exception/README.md) subclass.

Exception groups are [generic](https://docs.python.org/3.15/library/typing.html#generics) over the type of their
contained exceptions.

> **CPython implementation detail:** The `excs` parameter may be any sequence, but lists and tuples are
> specifically processed more efficiently here. For optimal performance,
> pass a tuple as `excs`.

### message

The `msg` argument to the constructor. This is a read-only attribute.

### exceptions

A tuple of the exceptions in the `excs` sequence given to the
constructor. This is a read-only attribute.

### subgroup(condition)

Returns an exception group that contains only the exceptions from the
current group that match *condition*, or `None` if the result is empty.

The condition can be an exception type or tuple of exception types, in which
case each exception is checked for a match using the same check that is used
in an `except` clause.  The condition can also be a callable (other than
a type object) that accepts an exception as its single argument and returns
true for the exceptions that should be in the subgroup.

The nesting structure of the current exception is preserved in the result,
as are the values of its `message`,
[__traceback__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__traceback__), [__cause__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__cause__),
[__context__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__context__) and
[__notes__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__notes__) fields.
Empty nested groups are omitted from the result.

The condition is checked for all exceptions in the nested exception group,
including the top-level and any nested exception groups. If the condition is
true for such an exception group, it is included in the result in full.

> *Added in version 3.13:* `condition` can be any callable which is not a type object.

### split(condition)

Like `subgroup()`, but returns the pair `(match, rest)` where `match`
is `subgroup(condition)` and `rest` is the remaining non-matching
part.

### derive(excs)

Returns an exception group with the same `message`, but which
wraps the exceptions in `excs`.

This method is used by `subgroup()` and `split()`, which
are used in various contexts to break up an exception group. A
subclass needs to override it in order to make `subgroup()`
and `split()` return instances of the subclass rather
than ExceptionGroup.

`subgroup()` and `split()` copy the
[__traceback__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__traceback__),
[__cause__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__cause__), [__context__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__context__) and
[__notes__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__notes__) fields from
the original exception group to the one returned by `derive()`, so
these fields do not need to be updated by `derive()`.

``` python
>>> class MyGroup(ExceptionGroup):
...     def derive(self, excs):
...         return MyGroup(self.message, excs)
...
>>> e = MyGroup("eg", [ValueError(1), TypeError(2)])
>>> e.add_note("a note")
>>> e.__context__ = Exception("context")
>>> e.__cause__ = Exception("cause")
>>> try:
...    raise e
... except Exception as e:
...    exc = e
...
>>> match, rest = exc.split(ValueError)
>>> exc, exc.__context__, exc.__cause__, exc.__notes__
(MyGroup('eg', [ValueError(1), TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
>>> match, match.__context__, match.__cause__, match.__notes__
(MyGroup('eg', [ValueError(1)]), Exception('context'), Exception('cause'), ['a note'])
>>> rest, rest.__context__, rest.__cause__, rest.__notes__
(MyGroup('eg', [TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
>>> exc.__traceback__ is match.__traceback__ is rest.__traceback__
True
```
> Code: [example_01.py](example_01.py)

Note that BaseExceptionGroup defines [__new__()](https://docs.python.org/3.15/reference/datamodel.html#object.__new__), so
subclasses that need a different constructor signature need to
override that rather than [__init__()](https://docs.python.org/3.15/reference/datamodel.html#object.__init__). For example, the following
defines an exception group subclass which accepts an exit_code and
constructs the group's message from it.

``` python
class Errors(ExceptionGroup):
   def __new__(cls, errors, exit_code):
      self = super().__new__(Errors, f"exit code: {exit_code}", errors)
      self.exit_code = exit_code
      return self

   def derive(self, excs):
      return Errors(excs, self.exit_code)
```

Like ExceptionGroup, any subclass of BaseExceptionGroup which
is also a subclass of [Exception](../../base-classes/Exception/README.md) can only wrap instances of
[Exception](../../base-classes/Exception/README.md).

> *Added in version 3.11.*
