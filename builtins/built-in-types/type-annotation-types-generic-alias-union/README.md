The core built-in types for [type annotations](https://docs.python.org/3.15/glossary.html#term-annotation) are
[Generic Alias](https://docs.python.org/3.15/builtins/stdtypes.html#types-genericalias) and [Union](https://docs.python.org/3.15/builtins/stdtypes.html#types-union).

## Generic Alias Type

`GenericAlias` objects are generally created by
[subscripting](https://docs.python.org/3.15/reference/expressions.html#subscriptions) a class. They are most often used with
[container classes](https://docs.python.org/3.15/reference/datamodel.html#sequence-types), such as [list](../sequence-types-list-tuple-range/list/README.md) or
[dict](../mapping-types-dict-frozendict/dict/README.md). For example, `list[int]` is a `GenericAlias` object created
by subscripting the `list` class with the argument [int](../../built-in-functions/int/README.md).
`GenericAlias` objects are intended primarily for use with
[type annotations](https://docs.python.org/3.15/glossary.html#term-annotation).

> **Note**
>
> It is generally only possible to subscript a class if the class implements
> the special method [__class_getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__class_getitem__).

A `GenericAlias` object acts as a proxy for a [generic type](https://docs.python.org/3.15/glossary.html#term-generic-type),
implementing *parameterized generics*.

For a container class, the
argument(s) supplied to a [subscription](https://docs.python.org/3.15/reference/expressions.html#subscriptions) of the class may
indicate the type(s) of the elements an object contains. For example,
`set[bytes]` can be used in type annotations to signify a [set](../set-types-set-frozenset/set/README.md) in
which all the elements are of type [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md).

For a class which defines [__class_getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__class_getitem__) but is not a
container, the argument(s) supplied to a subscription of the class will often
indicate the return type(s) of one or more methods defined on an object. For
example, [regular expressions](https://docs.python.org/3.15/library/re.html#module-re) can be used on both the [str](../text-sequence-type-str/str/README.md) data
type and the [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) data type:

- If `x = re.search('foo', 'foo')`, `x` will be a
  [re.Match](https://docs.python.org/3.15/library/re.html#match-objects) object where the return values of
  `x.group(0)` and `x[0]` will both be of type [str](../text-sequence-type-str/str/README.md). We can
  represent this kind of object in type annotations with the `GenericAlias`
  `re.Match[str]`.

- If `y = re.search(b'bar', b'bar')`, (note the `b` for [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md)),
  `y` will also be an instance of `re.Match`, but the return
  values of `y.group(0)` and `y[0]` will both be of type
  [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md). In type annotations, we would represent this
  variety of [re.Match](https://docs.python.org/3.15/library/re.html#match-objects) objects with `re.Match[bytes]`.

`GenericAlias` objects are instances of the class
[types.GenericAlias](https://docs.python.org/3.15/library/types.html#types.GenericAlias), which can also be used to create `GenericAlias`
objects directly. Specializations of user-defined [generic classes](https://docs.python.org/3.15/reference/compound_stmts.html#generic-classes)
may not be instances of [types.GenericAlias](https://docs.python.org/3.15/library/types.html#types.GenericAlias), but they provide similar functionality.

### T[X,, Y,, ...]

Creates a `GenericAlias` representing a type `T` parameterized by types
*X*, *Y*, and more depending on the `T` used.
For example, a function expecting a [list](../sequence-types-list-tuple-range/list/README.md) containing
[float](../../built-in-functions/float/README.md) elements:

``` python
def average(values: list[float]) -> float:
    return sum(values) / len(values)
```

Another example for [mapping](https://docs.python.org/3.15/glossary.html#term-mapping) objects, using a [dict](../mapping-types-dict-frozendict/dict/README.md), which
is a generic type expecting two type parameters representing the key type
and the value type.  In this example, the function expects a `dict` with
keys of type [str](../text-sequence-type-str/str/README.md) and values of type [int](../../built-in-functions/int/README.md):

``` python
def send_post_request(url: str, body: dict[str, int]) -> None:
    ...
```

The builtin functions [isinstance()](../../built-in-functions/isinstance/README.md) and [issubclass()](../../built-in-functions/issubclass/README.md) do not accept
`GenericAlias` types for their second argument:

``` python
>>> isinstance([1, 2], list[str])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: isinstance() argument 2 cannot be a parameterized generic
```
> Code: [example_01.py](example_01.py)

The Python runtime does not enforce [type annotations](https://docs.python.org/3.15/glossary.html#term-annotation).
This extends to generic types and their type parameters. When creating
a container object from a `GenericAlias`, the elements in the container are not checked
against their type. For example, the following code is discouraged, but will
run without errors:

``` python
>>> t = list[str]
>>> t([1, 2, 3])
[1, 2, 3]
```
> Code: [example_02.py](example_02.py)

Furthermore, parameterized generics erase type parameters during object
creation:

``` python
>>> t = list[str]
>>> type(t)
<class 'types.GenericAlias'>

>>> l = t()
>>> type(l)
<class 'list'>
```
> Code: [example_03.py](example_03.py)

Instances of `GenericAlias` are not classes at runtime, even though they behave like classes (they can be instantiated and subclassed):

``` python
>>> import inspect
>>> inspect.isclass(list[int])
False
```
> Code: [example_04.py](example_04.py)

This is true for [user-defined generics](https://docs.python.org/3.15/library/typing.html#user-defined-generics) also.

Calling [repr()](../../built-in-functions/repr/README.md) or [str()](../../built-in-functions/str/README.md) on a generic shows the parameterized type:

``` python
>>> repr(list[int])
'list[int]'

>>> str(list[int])
'list[int]'
```
> Code: [example_05.py](example_05.py)

The [__getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getitem__) method of generic containers will raise an
exception to disallow mistakes like `dict[str][str]`:

``` python
>>> dict[str][str]
Traceback (most recent call last):
  ...
TypeError: dict[str] is not a generic class
```
> Code: [example_06.py](example_06.py)

However, such expressions are valid when [type variables](https://docs.python.org/3.15/library/typing.html#generics) are
used.  The index must have as many elements as there are type variable items
in the `GenericAlias` object's [__args__](genericalias.__args__/README.md).

``` python
>>> from typing import TypeVar
>>> Y = TypeVar('Y')
>>> dict[str, Y][int]
dict[str, int]
```
> Code: [example_07.py](example_07.py)

### Standard Generic Classes

The following standard library classes support parameterized generics. This
list is non-exhaustive.

- [tuple](../sequence-types-list-tuple-range/tuple/README.md)

- [list](../sequence-types-list-tuple-range/list/README.md)

- [dict](../mapping-types-dict-frozendict/dict/README.md)

- [set](../set-types-set-frozenset/set/README.md)

- [frozendict](../mapping-types-dict-frozendict/frozendict/README.md)

- [frozenset](../set-types-set-frozenset/set/README.md)

- [type](../../built-in-functions/type/README.md)

- [asyncio.Future](https://docs.python.org/3.15/library/asyncio-future.html#asyncio.Future)

- [asyncio.Task](https://docs.python.org/3.15/library/asyncio-task.html#asyncio.Task)

- [collections.deque](https://docs.python.org/3.15/library/collections.html#collections.deque)

- [collections.defaultdict](https://docs.python.org/3.15/library/collections.html#collections.defaultdict)

- [collections.OrderedDict](https://docs.python.org/3.15/library/collections.html#collections.OrderedDict)

- [collections.Counter](https://docs.python.org/3.15/library/collections.html#collections.Counter)

- [collections.ChainMap](https://docs.python.org/3.15/library/collections.html#collections.ChainMap)

- [collections.abc.Awaitable](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Awaitable)

- [collections.abc.Coroutine](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Coroutine)

- [collections.abc.AsyncIterable](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.AsyncIterable)

- [collections.abc.AsyncIterator](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.AsyncIterator)

- [collections.abc.AsyncGenerator](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.AsyncGenerator)

- [collections.abc.Iterable](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Iterable)

- [collections.abc.Iterator](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Iterator)

- [collections.abc.Generator](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Generator)

- [collections.abc.Reversible](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Reversible)

- [collections.abc.Container](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Container)

- [collections.abc.Collection](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Collection)

- [collections.abc.Callable](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Callable)

- [collections.abc.Set](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Set)

- [collections.abc.MutableSet](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.MutableSet)

- [collections.abc.Mapping](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Mapping)

- [collections.abc.MutableMapping](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.MutableMapping)

- [collections.abc.Sequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Sequence)

- [collections.abc.MutableSequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.MutableSequence)

- [collections.abc.ByteString](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.ByteString)

- [collections.abc.MappingView](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.MappingView)

- [collections.abc.KeysView](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.KeysView)

- [collections.abc.ItemsView](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.ItemsView)

- [collections.abc.ValuesView](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.ValuesView)

- [contextlib.AbstractContextManager](https://docs.python.org/3.15/library/contextlib.html#contextlib.AbstractContextManager)

- [contextlib.AbstractAsyncContextManager](https://docs.python.org/3.15/library/contextlib.html#contextlib.AbstractAsyncContextManager)

- [dataclasses.Field](https://docs.python.org/3.15/library/dataclasses.html#dataclasses.Field)

- `functools.cached_property`

- [functools.partialmethod](https://docs.python.org/3.15/library/functools.html#functools.partialmethod)

- [os.PathLike](https://docs.python.org/3.15/library/os.html#os.PathLike)

- [queue.LifoQueue](https://docs.python.org/3.15/library/queue.html#queue.LifoQueue)

- [queue.Queue](https://docs.python.org/3.15/library/queue.html#queue.Queue)

- [queue.PriorityQueue](https://docs.python.org/3.15/library/queue.html#queue.PriorityQueue)

- [queue.SimpleQueue](https://docs.python.org/3.15/library/queue.html#queue.SimpleQueue)

- [re.Pattern](https://docs.python.org/3.15/library/re.html#re-objects)

- [re.Match](https://docs.python.org/3.15/library/re.html#match-objects)

- [shelve.BsdDbShelf](https://docs.python.org/3.15/library/shelve.html#shelve.BsdDbShelf)

- [shelve.DbfilenameShelf](https://docs.python.org/3.15/library/shelve.html#shelve.DbfilenameShelf)

- [shelve.Shelf](https://docs.python.org/3.15/library/shelve.html#shelve.Shelf)

- [types.MappingProxyType](https://docs.python.org/3.15/library/types.html#types.MappingProxyType)

- [weakref.WeakKeyDictionary](https://docs.python.org/3.15/library/weakref.html#weakref.WeakKeyDictionary)

- [weakref.WeakMethod](https://docs.python.org/3.15/library/weakref.html#weakref.WeakMethod)

- [weakref.WeakSet](https://docs.python.org/3.15/library/weakref.html#weakref.WeakSet)

- [weakref.WeakValueDictionary](https://docs.python.org/3.15/library/weakref.html#weakref.WeakValueDictionary)

### Special Attributes of ``GenericAlias`` objects

All parameterized generics implement special read-only attributes.

- [`genericalias.__origin__`](genericalias.__origin__/README.md) — This attribute points at the non-parameterized generic class:
- [`genericalias.__args__`](genericalias.__args__/README.md) — This attribute is a tuple (possibly of length 1) of generic types passed to the original __class_getitem__() of the generic class:
- [`genericalias.__parameters__`](genericalias.__parameters__/README.md) — This attribute is a lazily computed tuple (possibly empty) of unique type variables found in __args__:
- [`genericalias.__unpacked__`](genericalias.__unpacked__/README.md) — A boolean that is true if the alias has been unpacked using the * operator (see TypeVarTuple).

> **See also**
>
> PEP 484
>
>  - Type Hints
>
> Introducing Python's framework for type annotations.
>
> PEP 585
>
>  - Type Hinting Generics In Standard Collections
>
> Introducing the ability to natively parameterize standard-library
> classes, provided they implement the special class method
> [__class_getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__class_getitem__).
>
> Generics
>
> ,
>
> user-defined generics
>
>  and
>
> typing.Generic
>
> Documentation on how to implement generic classes that can be
> parameterized at runtime and understood by static type-checkers.

> *Added in version 3.9.*

## Union Type

A union object holds the value of the `|` (bitwise or) operation on
multiple [type objects](https://docs.python.org/3.15/builtins/stdtypes.html#bltin-type-objects).  These types are intended
primarily for [type annotations](https://docs.python.org/3.15/glossary.html#term-annotation). The union type expression
enables cleaner type hinting syntax compared to subscripting [typing.Union](https://docs.python.org/3.15/library/typing.html#typing.Union).

### X, |, Y, |, ...

Defines a union object which holds types *X*, *Y*, and so forth. `X | Y`
means either X or Y.  It is equivalent to `typing.Union[X, Y]`.
For example, the following function expects an argument of type
[int](../../built-in-functions/int/README.md) or [float](../../built-in-functions/float/README.md):

``` python
def square(number: int | float) -> int | float:
    return number ** 2
```

> **Note**
>
> The `|` operator cannot be used at runtime to define unions where one or
> more members is a forward reference. For example, `int | "Foo"`, where
> `"Foo"` is a reference to a class not yet defined, will fail at
> runtime. For unions which include forward references, present the
> whole expression as a string, e.g. `"int | Foo"`.

### union_object, ==, other

Union objects can be tested for equality with other union objects.  Details:

- Unions of unions are flattened:

  ``` python
  (int | str) | float == int | str | float
  ```

- Redundant types are removed:

  ``` python
  int | str | int == int | str
  ```

- When comparing unions, the order is ignored:

  ``` python
  int | str == str | int
  ```

- It creates instances of [typing.Union](https://docs.python.org/3.15/library/typing.html#typing.Union):

  ``` python
  int | str == typing.Union[int, str]
  type(int | str) is typing.Union
  ```

- Optional types can be spelled as a union with `None`:

  ``` python
  str | None == typing.Optional[str]
  ```

### isinstance(obj,, union_object)

### issubclass(obj,, union_object)

Calls to [isinstance()](../../built-in-functions/isinstance/README.md) and [issubclass()](../../built-in-functions/issubclass/README.md) are also supported with a
union object:

``` python
>>> isinstance("", int | str)
True
```
> Code: [example_08.py](example_08.py)

However, [parameterized generics](https://docs.python.org/3.15/builtins/stdtypes.html#types-genericalias) in
union objects cannot be checked:

``` python
>>> isinstance(1, int | list[int])  # short-circuit evaluation
True
>>> isinstance([1], int | list[int])
Traceback (most recent call last):
  ...
TypeError: isinstance() argument 2 cannot be a parameterized generic
```
> Code: [example_09.py](example_09.py)

The user-exposed type for the union object can be accessed from
[typing.Union](https://docs.python.org/3.15/library/typing.html#typing.Union) and used for [isinstance()](../../built-in-functions/isinstance/README.md) checks:

``` python
>>> import typing
>>> isinstance(int | str, typing.Union)
True
>>> typing.Union()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create 'typing.Union' instances
```
> Code: [example_10.py](example_10.py)

> **Note**
>
> The `__or__()` method for type objects was added to support the syntax
> `X | Y`.  If a metaclass implements `__or__()`, the Union may
> override it:
>
> ``` python
> >>> class M(type):
> ...     def __or__(self, other):
> ...         return "Hello"
> ...
> >>> class C(metaclass=M):
> ...     pass
> ...
> >>> C | int
> 'Hello'
> >>> int | C
> int | C
> ```
> > Code: [example_11.py](example_11.py)

> **See also**
>
> [PEP 604](https://peps.python.org/pep-604/) -- PEP proposing the `X | Y` syntax and the Union type.

> *Added in version 3.10.*

> *Changed in version 3.14:* Union objects are now instances of [typing.Union](https://docs.python.org/3.15/library/typing.html#typing.Union). Previously, they were instances
> of [types.UnionType](https://docs.python.org/3.15/library/types.html#types.UnionType), which remains an alias for [typing.Union](https://docs.python.org/3.15/library/typing.html#typing.Union).
