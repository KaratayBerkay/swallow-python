Creating a dictionary with the [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md) constructor is atomic when the
argument to it is a [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md) or a [tuple](../../built-in-types/sequence-types-list-tuple-range/tuple/README.md). When using the
[dict.fromkeys()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.fromkeys) method, dictionary creation is atomic when the
argument is a [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md), [tuple](../../built-in-types/sequence-types-list-tuple-range/tuple/README.md), [set](../../built-in-types/set-types-set-frozenset/set/README.md) or
[frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md).

The following operations and functions are [lock-free](https://docs.python.org/3.15/glossary.html#term-lock-free) and
[atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation).

``` python
d[key]       # dict.__getitem__
d.get(key)   # dict.get
key in d     # dict.__contains__
len(d)       # dict.__len__
```

All other operations from here on hold the [per-object lock](https://docs.python.org/3.15/glossary.html#term-per-object-lock).

Writing or removing a single item is safe to call from multiple threads
and will not corrupt the dictionary:

``` python
d[key] = value        # write
del d[key]            # delete
d.pop(key)            # remove and return
d.popitem()           # remove and return last item
d.setdefault(key, v)  # insert if missing
```

These operations may compare keys using [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__), which can
execute arbitrary Python code. During such comparisons, the dictionary may
be modified by another thread. For built-in types like [str](../../built-in-types/text-sequence-type-str/str/README.md),
[int](https://docs.python.org/3.15/builtins/functions.html#int), and [float](https://docs.python.org/3.15/builtins/functions.html#float), that implement [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__) in C,
the underlying lock is not released during comparisons and this is not a
concern.

The following operations return new objects and hold the [per-object lock](https://docs.python.org/3.15/glossary.html#term-per-object-lock)
for the duration of the operation:

``` python
d.copy()      # returns a shallow copy of the dictionary
d | other     # merges two dicts into a new dict
d.keys()      # returns a new dict_keys view object
d.values()    # returns a new dict_values view object
d.items()     # returns a new dict_items view object
```

The [clear()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.clear) method holds the lock for its duration. Other
threads cannot observe elements being removed.

The following operations lock both dictionaries. For [update()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.update)
and `|=`, this applies only when the other operand is a [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md)
that uses the standard dict iterator (but not subclasses that override
iteration). For equality comparison, this applies to [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md) and
its subclasses:

``` python
d.update(other_dict)  # both locked when other_dict is a dict
d |= other_dict       # both locked when other_dict is a dict
d == other_dict       # both locked for dict and subclasses
```

All comparison operations also compare values using [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__),
so for non-built-in types the lock may be released during comparison.

[fromkeys()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.fromkeys) locks both the new dictionary and the iterable
when the iterable is exactly a [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md), [set](../../built-in-types/set-types-set-frozenset/set/README.md), or
[frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md) (not subclasses):

``` python
dict.fromkeys(a_dict)      # locks both
dict.fromkeys(a_set)       # locks both
dict.fromkeys(a_frozenset) # locks both
```

When updating from a non-dict iterable, only the target dictionary is
locked. The iterable may be concurrently modified by another thread:

``` python
d.update(iterable)        # iterable is not a dict: only d locked
d |= iterable             # iterable is not a dict: only d locked
dict.fromkeys(iterable)   # iterable is not a dict/set/frozenset: only result locked
```

Operations that involve multiple accesses, as well as iteration, are never
atomic:

``` python
# NOT atomic: read-modify-write
d[key] = d[key] + 1

# NOT atomic: check-then-act (TOCTOU)
if key in d:
    del d[key]

# NOT thread-safe: iteration while modifying
for key, value in d.items():
    process(key)  # another thread may modify d
```

To avoid time-of-check to time-of-use (TOCTOU) issues, use atomic
operations or handle exceptions:

``` python
# Use pop() with default instead of check-then-delete
d.pop(key, None)

# Or handle the exception
try:
    del d[key]
except KeyError:
    pass
```

To safely iterate over a dictionary that may be modified by another
thread, iterate over a copy:

``` python
# Make a copy to iterate safely
for key, value in d.copy().items():
    process(key)
```

Consider external synchronization when sharing [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md) instances
across threads.
