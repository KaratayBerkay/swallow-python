# Thread Safety Guarantees

This page documents thread-safety guarantees for built-in types in Python's
free-threaded build. The guarantees described here apply when using Python with
the [GIL](https://docs.python.org/3.15/glossary.html#term-GIL) disabled (free-threaded mode). When the GIL is enabled, most
operations are implicitly serialized.

For general guidance on writing thread-safe code in free-threaded Python, see
[Python support for free threading](https://docs.python.org/3.15/howto/free-threading-python.html#freethreading-python-howto).

## Contents

- [Thread safety levels](thread-safety-levels/README.md) — The C API documentation uses the following levels to describe the thread safety guarantees of each function.
- [Thread safety for list objects](thread-safety-for-list-objects/README.md) — Reading a single element from a list is atomic:
- [Thread safety for dict objects](thread-safety-for-dict-objects/README.md) — Creating a dictionary with the dict constructor is atomic when the argument to it is a dict or a tuple.
- [Thread safety for set objects](thread-safety-for-set-objects/README.md) — The len() function is lock-free and atomic.
- [Thread safety for bytearray objects](thread-safety-for-bytearray-objects/README.md) — The len() function is lock-free and atomic.
- [Thread safety for memoryview objects](thread-safety-for-memoryview-objects/README.md) — memoryview objects provide access to the internal data of an underlying object without copying.
