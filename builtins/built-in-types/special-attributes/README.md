The implementation adds a few special read-only attributes to several object
types, where they are relevant.  Some of these are not reported by the
[dir()](../../built-in-functions/dir/README.md) built-in function.

- [`definition.__name__`](definition.__name__/README.md) — The name of the class, function, method, descriptor, or generator instance.
- [`definition.__qualname__`](definition.__qualname__/README.md) — The qualified name of the class, function, method, descriptor, or generator instance.
- [`definition.__module__`](definition.__module__/README.md) — The name of the module in which a class or function was defined.
- [`definition.__doc__`](definition.__doc__/README.md) — The documentation string of a class or function, or None if undefined.
- [`definition.__type_params__`](definition.__type_params__/README.md) — The type parameters of generic classes, functions, and type aliases.
