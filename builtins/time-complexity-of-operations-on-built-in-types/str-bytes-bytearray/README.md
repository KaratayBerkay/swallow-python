[str](../../built-in-types/text-sequence-type-str/str/README.md) and [bytes](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) objects are immutable sequences of characters and
bytes, respectively. As with tuples, copying one returns the original object.
A [bytearray](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md) is mutable, and additionally supports the mutating operations
of [list](../../built-in-types/sequence-types-list-tuple-range/list/README.md) (except `sort()`), at the same costs. However, deleting at
the front with `del` (`del b[0]`, `del b[:k]`) only advances the start of
the buffer instead of moving the remaining bytes, and is amortized *O*(1).

| Operation | Complexity |
| --- | --- |
| Get item (`s[k]`) | *O*(1) |
| Get slice (`s[i:j]`) | *O*(*j* - *i*) |
| Concatenate (`s + t`) [^1] | *O*(len(*s*) + len(*t*)) |
| Multiply (`s * k`) | *O*(*nk*) |
| Substring search (`x in s`, `s.find(x)`, `s.index(x)`) [^2] | *O*(*n*) |
| Reverse substring search (`s.rfind(x)`, `s.rindex(x)`) [^2] [^3] | *O*(*n* × len(*x*)) |
| Encode or decode [^4] | *O*(*n*) |
| Iteration | *O*(*n*) |
| Get length (`len(s)`) [^5] | *O*(1) |

[^1]: Each concatenation builds a new object, so building a string by concatenating many pieces in a loop is quadratic in the total length. See the [note on concatenating immutable sequences](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-repeated-concatenation) for alternatives.
[^2]: With *start* and *end* arguments, *n* is the length of the region searched rather than of *s*, and unlike slicing nothing is copied.
[^3]: This is the worst case. Reverse searches are *O*(*n*) on typical input. Forward searches instead use a more elaborate algorithm with a linear worst case, described in [Objects/stringlib/stringlib_find_two_way_notes.txt](https://github.com/python/cpython/tree/3.15/Objects/stringlib/stringlib_find_two_way_notes.txt).
[^4]: This assumes a codec that does a constant amount of work per character.
[^5]: The number of elements is stored in the object, so `len()` does not need to count them.
