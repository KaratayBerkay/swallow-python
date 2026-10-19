## `genericalias.__args__`

```
genericalias.__args__
```

This attribute is a [tuple](../../sequence-types-list-tuple-range/tuple/README.md) (possibly of length 1) of generic
types passed to the original [__class_getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__class_getitem__) of the
generic class:

``` python
>>> dict[str, list[int]].__args__
(<class 'str'>, list[int])
```
> Code: [example_01.py](example_01.py)
