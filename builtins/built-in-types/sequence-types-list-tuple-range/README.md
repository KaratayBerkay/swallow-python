There are three basic sequence types: lists, tuples, and range objects.
Additional sequence types tailored for processing of
[binary data](https://docs.python.org/3.15/builtins/stdtypes.html#binaryseq) and [text strings](https://docs.python.org/3.15/builtins/stdtypes.html#textseq) are
described in dedicated sections.

## Common Sequence Operations

The operations in the following table are supported by most sequence types,
both mutable and immutable. The [collections.abc.Sequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Sequence) ABC is
provided to make it easier to correctly implement these operations on
custom sequence types.

This table lists the sequence operations sorted in ascending priority.  In the
table, *s* and *t* are sequences of the same type, *n*, *i*, *j* and *k* are
integers and *x* is an arbitrary object that meets any type and value
restrictions imposed by *s*.

The `in` and `not in` operations have the same priorities as the
comparison operations. The `+` (concatenation) and `*` (repetition)
operations have the same priority as the corresponding numeric operations. [^1]

See [Time complexity of operations on built-in types](https://docs.python.org/3.15/builtins/time-complexity.html#time-complexity) for the costs of the various sequence
operations.

| Operation | Result | Notes |
| --- | --- | --- |
| `x in s` | `True` if an item of *s* is equal to *x*, else `False` | (1) |
| `x not in s` | `False` if an item of *s* is equal to *x*, else `True` | (1) |
| `s + t` | the concatenation of *s* and *t* | (6)(7) |
| `s * n` or `n * s` | equivalent to adding *s* to itself *n* times | (2)(7) |
| `s[i]` | *i*th item of *s*, origin 0 | (3)(8) |
| `s[i:j]` | slice of *s* from *i* to *j* | (3)(4) |
| `s[i:j:k]` | slice of *s* from *i* to *j* with step *k* | (3)(5) |
| `len(s)` | length of *s* |  |
| `min(s)` | smallest item of *s* |  |
| `max(s)` | largest item of *s* |  |

Sequences of the same type also support comparisons.  In particular, tuples
and lists are compared lexicographically by comparing corresponding elements.
This means that to compare equal, every element must compare equal and the
two sequences must be of the same type and have the same length.  (For full
details see [Comparisons](https://docs.python.org/3.15/reference/expressions.html#comparisons) in the language reference.)

Forward and reversed iterators over mutable sequences access values using an
index.  That index will continue to march forward (or backward) even if the
underlying sequence is mutated.  The iterator terminates only when an
[IndexError](https://docs.python.org/3.15/builtins/exceptions.html#IndexError) or a [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) is encountered (or when the index
drops below zero).

Notes:

1. While the `in` and `not in` operations are used only for simple
   containment testing in the general case, some specialised sequences
   (such as [str](../text-sequence-type-str/str/README.md), [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) and [bytearray](../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md)) also use
   them for subsequence testing:

   ``` python
   >>> "gg" in "eggs"
   True
   ```
   > Code: [example_01.py](example_01.py)

2. Values of *n* less than `0` are treated as `0` (which yields an empty
   sequence of the same type as *s*).  Note that items in the sequence *s*
   are not copied; they are referenced multiple times.  This often haunts
   new Python programmers; consider:

   ``` python
   >>> lists = [[]] * 3
   >>> lists
   [[], [], []]
   >>> lists[0].append(3)
   >>> lists
   [[3], [3], [3]]
   ```
   > Code: [example_02.py](example_02.py)

   What has happened is that `[[]]` is a one-element list containing an empty
   list, so all three elements of `[[]] * 3` are references to this single empty
   list.  Modifying any of the elements of `lists` modifies this single list.
   You can create a list of different lists this way:

   ``` python
   >>> lists = [[] for i in range(3)]
   >>> lists[0].append(3)
   >>> lists[1].append(5)
   >>> lists[2].append(7)
   >>> lists
   [[3], [5], [7]]
   ```
   > Code: [example_03.py](example_03.py)

   Further explanation is available in the FAQ entry
   [How do I create a multidimensional list?](https://docs.python.org/3.15/faq/programming.html#faq-multidimensional-list).

3. If *i* or *j* is negative, the index is relative to the end of sequence *s*:
   `len(s) + i` or `len(s) + j` is substituted.  But note that `-0` is
   still `0`.

4. The slice of *s* from *i* to *j* is defined as the sequence of items with
   index *k* such that `i <= k < j`.

   - If *i* is omitted or `None`, use `0`.

   - If *j* is omitted or `None`, use `len(s)`.

   - If *i* or *j* is less than `-len(s)`, use `0`.

   - If *i* or *j* is greater than `len(s)`, use `len(s)`.

   - If *i* is greater than or equal to *j*, the slice is empty.

5. The slice of *s* from *i* to *j* with step *k* is defined as the sequence of
   items with index  `x = i + n*k` such that `0 <= n < (j-i)/k`.  In other words,
   the indices are `i`, `i+k`, `i+2*k`, `i+3*k` and so on, stopping when
   *j* is reached (but never including *j*).  When *k* is positive,
   *i* and *j* are reduced to `len(s)` if they are greater.
   When *k* is negative, *i* and *j* are reduced to `len(s) - 1` if
   they are greater.  If *i* or *j* are omitted or `None`, they become
   "end" values (which end depends on the sign of *k*).  Note, *k* cannot be zero.
   If *k* is `None`, it is treated like `1`.

1. Concatenating immutable sequences always results in a new object.  This
   means that building up a sequence by repeated concatenation will have a
   quadratic runtime cost in the total sequence length.  To get a linear
   runtime cost, you must switch to one of the alternatives below:

   - if concatenating [str](../text-sequence-type-str/str/README.md) objects, you can build a list and use
     [str.join()](../text-sequence-type-str/str.join/README.md) at the end or else write to an [io.StringIO](https://docs.python.org/3.15/library/io.html#io.StringIO)
     instance and retrieve its value when complete

   - if concatenating [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) objects, you can similarly use
     [bytes.join()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.join/README.md) or [io.BytesIO](https://docs.python.org/3.15/library/io.html#io.BytesIO), or you can do in-place
     concatenation with a [bytearray](../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md) object.  [bytearray](../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md)
     objects are mutable and have an efficient overallocation mechanism

   - if concatenating [tuple](tuple/README.md) objects, extend a [list](list/README.md) instead

   - for other types, investigate the relevant class documentation

2. Some sequence types (such as [range](range/README.md)) only support item sequences
   that follow specific patterns, and hence don't support sequence
   concatenation or repetition.

3. An [IndexError](https://docs.python.org/3.15/builtins/exceptions.html#IndexError) is raised if *i* is outside the sequence range.

### Sequence, Methods

Sequence types also support the following methods:

- [`list.count`](list.count/README.md)
- [`range.count`](range.count/README.md) — Documented together with list.count.
- [`tuple.count`](tuple.count/README.md) — Documented together with list.count.
- [`sequence.count`](sequence.count/README.md) — Return the total number of occurrences of *value* in *sequence*.
- [`list.index`](list.index/README.md)
- [`range.index`](range.index/README.md) — Documented together with list.index.
- [`tuple.index`](tuple.index/README.md) — Documented together with list.index.
- [`sequence.index`](sequence.index/README.md) — Return the index of the first occurrence of *value* in *sequence*.

## Immutable Sequence Types

The only operation that immutable sequence types generally implement that is
not also implemented by mutable sequence types is support for the [hash()](../../built-in-functions/hash/README.md)
built-in.

This support allows immutable sequences, such as [tuple](tuple/README.md) instances, to
be used as [dict](../mapping-types-dict-frozendict/dict/README.md) keys and stored in [set](../set-types-set-frozenset/set/README.md) and [frozenset](../set-types-set-frozenset/set/README.md)
instances.

Attempting to hash an immutable sequence that contains unhashable values will
result in [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError).

## Mutable Sequence Types

The operations in the following table are defined on mutable sequence types.
The [collections.abc.MutableSequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.MutableSequence) ABC is provided to make it
easier to correctly implement these operations on custom sequence types.

In the table *s* is an instance of a mutable sequence type, *t* is any
iterable object and *x* is an arbitrary object that meets any type
and value restrictions imposed by *s* (for example, [bytearray](../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md) only
accepts integers that meet the value restriction `0 <= x <= 255`).

| Operation | Result | Notes |
| --- | --- | --- |
| `s[i] = x` | item *i* of *s* is replaced by *x* |  |
| `del s[i]` | removes item *i* of *s* |  |
| `s[i:j] = t` | slice of *s* from *i* to *j* is replaced by the contents of the iterable *t* |  |
| `del s[i:j]` | removes the elements of `s[i:j]` from the list (same as `s[i:j] = []`) |  |
| `s[i:j:k] = t` | the elements of `s[i:j:k]` are replaced by those of *t* | (1) |
| `del s[i:j:k]` | removes the elements of `s[i:j:k]` from the list |  |
| `s += t` | extends *s* with the contents of *t* (for the most part the same as `s[len(s):len(s)] = t`) |  |
| `s *= n` | updates *s* with its contents repeated *n* times | (2) |

Notes:

1. If *k* is not equal to `1`, *t* must have the same length as the slice it is replacing.

2. The value *n* is an integer, or an object implementing
   [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).  Zero and negative values of *n* clear
   the sequence.  Items in the sequence are not copied; they are referenced
   multiple times, as explained for `s * n` under [Common Sequence Operations](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-common).

### Mutable, Sequence, Methods

Mutable sequence types also support the following methods:

- [`bytearray.append`](bytearray.append/README.md)
- [`list.append`](list.append/README.md) — Documented together with bytearray.append.
- [`sequence.append`](sequence.append/README.md) — Append *value* to the end of the sequence.
- [`bytearray.clear`](bytearray.clear/README.md)
- [`list.clear`](list.clear/README.md) — Documented together with bytearray.clear.
- [`sequence.clear`](sequence.clear/README.md) — Remove all items from *sequence*.
- [`bytearray.copy`](bytearray.copy/README.md)
- [`list.copy`](list.copy/README.md) — Documented together with bytearray.copy.
- [`sequence.copy`](sequence.copy/README.md) — Create a shallow copy of *sequence*.
- [`bytearray.extend`](bytearray.extend/README.md)
- [`list.extend`](list.extend/README.md) — Documented together with bytearray.extend.
- [`sequence.extend`](sequence.extend/README.md) — Extend *sequence* with the contents of *iterable*.
- [`bytearray.insert`](bytearray.insert/README.md)
- [`list.insert`](list.insert/README.md) — Documented together with bytearray.insert.
- [`sequence.insert`](sequence.insert/README.md) — Insert *value* into *sequence* at the given *index*.
- [`bytearray.pop`](bytearray.pop/README.md)
- [`list.pop`](list.pop/README.md) — Documented together with bytearray.pop.
- [`sequence.pop`](sequence.pop/README.md) — Retrieve the item at *index* and also remove it from *sequence*.
- [`bytearray.remove`](bytearray.remove/README.md)
- [`list.remove`](list.remove/README.md) — Documented together with bytearray.remove.
- [`sequence.remove`](sequence.remove/README.md) — Remove the first item from *sequence* where sequence[i] == value.
- [`bytearray.reverse`](bytearray.reverse/README.md)
- [`list.reverse`](list.reverse/README.md) — Documented together with bytearray.reverse.
- [`sequence.reverse`](sequence.reverse/README.md) — Reverse the items of *sequence* in place.

## Lists

Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).

- [`list`](list/README.md) — Lists may be constructed in several ways:

> **See also**
>
> For detailed information on thread-safety guarantees for [list](list/README.md)
> objects, see [Thread safety for list objects](https://docs.python.org/3.15/builtins/threadsafety.html#thread-safety-list).

## Tuples

Tuples are immutable sequences, typically used to store collections of
heterogeneous data (such as the 2-tuples produced by the [enumerate()](../../built-in-functions/enumerate/README.md)
built-in). Tuples are also used for cases where an immutable sequence of
homogeneous data is needed (such as allowing storage in a [set](../set-types-set-frozenset/set/README.md) or
[dict](../mapping-types-dict-frozendict/dict/README.md) instance).

- [`tuple`](tuple/README.md) — Tuples may be constructed in a number of ways:

For heterogeneous collections of data where access by name is clearer than
access by index, [collections.namedtuple()](https://docs.python.org/3.15/library/collections.html#collections.namedtuple) may be a more appropriate
choice than a simple tuple object.

## Ranges

The [range](range/README.md) type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in `for`
loops.

- [`range`](range/README.md) — The arguments to the range constructor must be integers (either built-in int or any object that implements the __index__() special method).

The advantage of the [range](range/README.md) type over a regular [list](list/README.md) or
[tuple](tuple/README.md) is that a [range](range/README.md) object will always take the same
(small) amount of memory, no matter the size of the range it represents (as it
only stores the `start`, `stop` and `step` values, calculating individual
items and subranges as needed).

Range objects implement the [collections.abc.Sequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Sequence) ABC, and provide
features such as containment tests, element index lookup, slicing and
support for negative indices (see [Sequence Types — list, tuple, range](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq)):

``` python
>>> r = range(0, 20, 2)
>>> r
range(0, 20, 2)
>>> 11 in r
False
>>> 10 in r
True
>>> r.index(10)
5
>>> r[5]
10
>>> r[:5]
range(0, 10, 2)
>>> r[-1]
18
```
> Code: [example_04.py](example_04.py)

Testing range objects for equality with `==` and `!=` compares
them as sequences.  That is, two range objects are considered equal if
they represent the same sequence of values.  (Note that two range
objects that compare equal might have different [start](https://docs.python.org/3.15/builtins/stdtypes.html#range.start),
[stop](https://docs.python.org/3.15/builtins/stdtypes.html#range.stop) and [step](https://docs.python.org/3.15/builtins/stdtypes.html#range.step) attributes, for example
`range(0) == range(2, 1, 3)` or `range(0, 3, 2) == range(0, 4, 2)`.)

> *Changed in version 3.2:* Implement the Sequence ABC.
> Support slicing and negative indices.
> Test [int](../../built-in-functions/int/README.md) objects for membership in constant time instead of
> iterating through all items.

> *Changed in version 3.3:* Define '==' and '!=' to compare range objects based on the
> sequence of values they define (instead of comparing based on
> object identity).
>
> Added the [start](https://docs.python.org/3.15/builtins/stdtypes.html#range.start), [stop](https://docs.python.org/3.15/builtins/stdtypes.html#range.stop) and [step](https://docs.python.org/3.15/builtins/stdtypes.html#range.step)
> attributes.

> **See also**
>
> - The [linspace recipe](https://code.activestate.com/recipes/579000-equally-spaced-numbers-linspace/)
>   shows how to implement a lazy version of range suitable for floating-point
>   applications.

[^1]: They must have since the parser can't tell the type of the operands.
