1. Amortized. An individual operation may occasionally be *O*(*n*)
   when the underlying storage is resized, but this cost is spread over
   many operations, depending on the history of the container.

2. Popping or deleting the element at index *k* of a list of size *n*
   shifts all elements after *k* one slot to the left, moving *n* - *k* - 1
   elements; inserting at index *k* shifts the elements from *k* onwards one
   slot to the right, moving *n* - *k* elements. The worst case is index 0,
   where the whole rest of the list has to be moved; the average case, an
   index in the middle of the list, takes *O*(*n*/2) = *O*(*n*)
   operations; and operating at the end of the list moves nothing and is
   *O*(1).

3. Plus the cost of iterating over *t*, which may be expensive for an
   arbitrary iterable.

4. This is the worst case scenario. Sorting is adaptive and input that is
   already sorted or reverse-sorted takes only *O*(*n*) comparisons.
   See [Objects/listsort.txt](https://github.com/python/cpython/tree/3.15/Objects/listsort.txt) for more information.

5. The number of elements is stored in the object, so `len()` does
   not need to count them.

6. Copying a [frozendict](../../built-in-types/mapping-types-dict-frozendict/frozendict/README.md) or a [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md) is *O*(1) as it
   returns the original object.

7. These operations scan the container's internal hash table, which is
   not shrunk when elements are removed. After removing most elements, they
   still take time proportional to the container's former size, until a
   later insertion triggers a resize.

8. *O*(len(*t*)) if *t* is not a set.

9. *O*(len(*s*) + len(*t*)) if *t* is not a set.

10. Each concatenation builds a new object, so building a string by
    concatenating many pieces in a loop is quadratic in the total length.
    See the [note on concatenating immutable sequences](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-repeated-concatenation) for alternatives.

11. With *start* and *end* arguments, *n* is the length of the region
    searched rather than of *s*, and unlike slicing nothing is copied.

12. This is the worst case. Reverse searches are *O*(*n*) on typical
    input. Forward searches instead use a more elaborate algorithm with a
    linear worst case, described in
    [Objects/stringlib/stringlib_find_two_way_notes.txt](https://github.com/python/cpython/tree/3.15/Objects/stringlib/stringlib_find_two_way_notes.txt).

13. This assumes a codec that does a constant amount of work per character.

14. These unpack and compare each element individually, so they are much
    slower than the equivalent [bytes](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) methods.

15. Assuming [int](https://docs.python.org/3.15/builtins/functions.html#int) or [bool](https://docs.python.org/3.15/builtins/functions.html#bool) arguments. For other types,
    the range is searched like any other sequence in *O*(*n*) time.
