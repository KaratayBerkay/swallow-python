# Time complexity of operations on built-in types

This page documents the time complexity of various operations on built-in types
in CPython. Other Python implementations may have different performance
characteristics. Additionally, the listed costs assume exact built-in types, as
instances of subclasses may have different costs.

We use [Big *O* notation](https://en.wikipedia.org/wiki/Big_O_notation) to describe how the running time of an operation grows
with the size of its inputs. Unless stated otherwise, *n* denotes the number of
elements currently in the container, and *k* is the value of a numeric
parameter, such as an index or a repeat count.

## Contents

- [list](list/README.md) — Lists are mutable sequences; for more detail on the implementation see How are lists implemented in CPython?.
- [tuple](tuple/README.md) — A tuple is an immutable sequence.
- [dict, frozendict](dict-frozendict/README.md) — The times listed for dict objects are average-case times, as they assume the hash function for the objects is sufficiently robust to make…
- [set, frozenset](set-frozenset/README.md) — See dict as the set and frozenset implementations are similar, and the same caveats apply.
- [str, bytes, bytearray](str-bytes-bytearray/README.md) — str and bytes objects are immutable sequences of characters and bytes, respectively.
- [memoryview](memoryview/README.md) — memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying.
- [range](range/README.md) — A range object computes its items on demand from its *start*, *stop* and *step* values, so most operations do not depend on the length of the range.
- [Notes](notes/README.md)
