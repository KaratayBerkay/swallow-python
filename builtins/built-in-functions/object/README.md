## `object()`

```
object()
```

This is the ultimate base class of all other classes. It has methods
that are common to all instances of Python classes. When the constructor
is called, it returns a new featureless object. The constructor does not
accept any arguments.

> **Note**
>
> object instances do *not* have [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__)
> attributes, so you can't assign arbitrary attributes to an instance of
> object.
