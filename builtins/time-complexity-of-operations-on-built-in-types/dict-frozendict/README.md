The times listed for dict objects are average-case times, as they assume the
hash function for the objects is sufficiently robust to make collisions
uncommon. They also assume the keys are well-distributed among the set of
possible keys. In the worst case, when every key hashes to the same value,
each of the *O*(1) operations below instead takes *O*(*n*) time. They also
assume that hashing and comparing a key is *O*(1). For more detail on the
implementation, see [How are dictionaries implemented in CPython?](https://docs.python.org/3.15/faq/design.html#how-are-dictionaries-implemented).

A [frozendict](../../built-in-types/mapping-types-dict-frozendict/frozendict/README.md) is immutable, so it does not support setting, deleting,
or updating items. The other operations below apply to it at the same costs.

| Operation | Complexity |
| --- | --- |
| `key in d` | *O*(1) |
| Copy (`d.copy()`) [^1] [^2] | *O*(*n*) |
| Get item (`d[key]`, `d.get(key)`) | *O*(1) |
| Set item (`d[key] = value`) [^3] | *O*(1) |
| Delete item (`del d[key]`, `d.pop(key)`) | *O*(1) |
| Update (`d.update(t)`, `d \|= t`) [^3] [^4] [^2] | *O*(len(*t*)) |
| Iteration [^2] | *O*(*n*) |
| Get length (`len(d)`) [^5] | *O*(1) |

[^1]: Copying a [frozendict](../../built-in-types/mapping-types-dict-frozendict/frozendict/README.md) or a [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md) is *O*(1) as it returns the original object.
[^2]: These operations scan the container's internal hash table, which is not shrunk when elements are removed. After removing most elements, they still take time proportional to the container's former size, until a later insertion triggers a resize.
[^3]: Amortized. An individual operation may occasionally be *O*(*n*) when the underlying storage is resized, but this cost is spread over many operations, depending on the history of the container.
[^4]: Plus the cost of iterating over *t*, which may be expensive for an arbitrary iterable.
[^5]: The number of elements is stored in the object, so `len()` does not need to count them.
