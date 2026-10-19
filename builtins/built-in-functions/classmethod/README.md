## `@classmethod`

```
classmethod
```

Transform a method into a class method.

A class method receives the class as an implicit first argument, just like an
instance method receives the instance. To declare a class method, use this
idiom:

``` python
class C:
    @classmethod
    def f(cls, arg1, arg2): ...
```

The `@classmethod` form is a function [decorator](https://docs.python.org/3.15/glossary.html#term-decorator) -- see
[Function definitions](https://docs.python.org/3.15/reference/compound_stmts.html#function) for details.

A class method can be called either on the class (such as `C.f()`) or on an instance (such
as `C().f()`).  The instance is ignored except for its class. If a class
method is called for a derived class, the derived class object is passed as the
implied first argument.

Class methods are different than C++ or Java static methods. If you want those,
see [staticmethod()](../staticmethod/README.md) in this section.
For more information on class methods, see [The standard type hierarchy](https://docs.python.org/3.15/reference/datamodel.html#types).

> *Changed in version 3.9:* Class methods can now wrap other [descriptors](https://docs.python.org/3.15/glossary.html#term-descriptor) such as
> `property()`.

> *Changed in version 3.10:* Class methods now inherit the method attributes
> ([__module__](https://docs.python.org/3.15/reference/datamodel.html#function.__module__), [__name__](https://docs.python.org/3.15/reference/datamodel.html#function.__name__),
> [__qualname__](https://docs.python.org/3.15/reference/datamodel.html#function.__qualname__), [__doc__](https://docs.python.org/3.15/reference/datamodel.html#function.__doc__) and
> [__annotations__](https://docs.python.org/3.15/reference/datamodel.html#function.__annotations__)) and have a new `__wrapped__`
> attribute.

> *Deprecated since version 3.11, removed in version 3.13:* Class methods can no longer wrap other [descriptors](https://docs.python.org/3.15/glossary.html#term-descriptor) such as
> `property()`.
