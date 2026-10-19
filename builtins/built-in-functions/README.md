# Built-in Functions

The Python interpreter has a number of functions and types built into it that
are always available.  They are listed here in alphabetical order.

Every folder holds a `README.md` with the explanation from the
official documentation plus the examples as runnable `example_*.py`
files. Run one with:

``` console
$ python3 abs/example_01.py
```

## Contents

- [`abs()`](abs/README.md) — Return the absolute value of a number.
- [`aiter()`](aiter/README.md) — Return an asynchronous iterator for an asynchronous iterable.
- [`all()`](all/README.md) — Return True if all elements of the *iterable* are true (or if the iterable is empty).
- [`anext()`](anext/README.md) — When awaited, return the next item from the given asynchronous iterator, or *default* if given and the iterator is exhausted.
- [`any()`](any/README.md) — Return True if any element of the *iterable* is true.
- [`ascii()`](ascii/README.md) — As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by…
- [`bin()`](bin/README.md) — Convert an integer number to a binary string prefixed with "0b".
- [`bool()`](bool/README.md) — Return a Boolean value, i.e. one of True or False.  The argument is converted using the standard truth testing procedure. If the argument is false…
- [`breakpoint()`](breakpoint/README.md) — This function drops you into the debugger at the call site.
- [`bytearray()`](bytearray/README.md) — Return a new array of bytes.
- [`bytes()`](bytes/README.md) — Return a new "bytes" object which is an immutable sequence of integers in the range 0 <= x < 256.
- [`callable()`](callable/README.md) — Return True if the *object* argument appears callable, False if not.
- [`chr()`](chr/README.md) — Return the string representing a character with the specified Unicode code point.
- [`@classmethod`](classmethod/README.md) — Transform a method into a class method.
- [`compile()`](compile/README.md) — Compile the *source* into a code or AST object.
- [`complex()`](complex/README.md) — Convert a single string or number to a complex number, or create a complex number from real and imaginary parts.
- [`delattr()`](delattr/README.md) — This is a relative of setattr().
- [`dict()`](dict/README.md) — Create a new dictionary.
- [`dir()`](dir/README.md) — Without arguments, return the list of names in the current local scope.
- [`divmod()`](divmod/README.md) — Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
- [`enumerate()`](enumerate/README.md) — Return an enumerate object.
- [`eval()`](eval/README.md) — The *source* argument is parsed and evaluated as a Python expression (technically speaking, an expression list) using the *globals* and *locals*…
- [`exec()`](exec/README.md) — This function supports dynamic execution of Python code.
- [`filter()`](filter/README.md) — Construct an iterator from those elements of *iterable* for which *function* is true.
- [`float()`](float/README.md) — Return a floating-point number constructed from a number or a string.
- [`format()`](format/README.md) — Convert a *value* to a "formatted" representation, as controlled by *format_spec*.
- [`frozendict()`](frozendict/README.md) — Create a new frozen dictionary.
- [`frozenset()`](frozenset/README.md) — Return a new frozenset object, optionally with elements taken from *iterable*.
- [`getattr()`](getattr/README.md) — Return the value of the named attribute of *object*.
- [`globals()`](globals/README.md) — Return the dictionary implementing the current module namespace.
- [`hasattr()`](hasattr/README.md) — The arguments are an object and a string.
- [`hash()`](hash/README.md) — Return the hash value of the object (if it has one).
- [`help()`](help/README.md) — Invoke the built-in help system.
- [`hex()`](hex/README.md) — Convert an integer number to a lowercase hexadecimal string prefixed with "0x".
- [`id()`](id/README.md) — Return the "identity" of an object.
- [`input()`](input/README.md) — If the *prompt* argument is present, it is written to standard output without a trailing newline.
- [`int()`](int/README.md) — Return an integer object constructed from a number or a string, or return 0 if no arguments are given.
- [`isinstance()`](isinstance/README.md) — Return True if the *object* argument is an instance of the *classinfo* argument, or of a (direct, indirect, or virtual) subclass thereof.
- [`issubclass()`](issubclass/README.md) — Return True if *cls* is a subclass (direct, indirect, or virtual) of *classinfo*.
- [`iter()`](iter/README.md) — Return an iterator object.
- [`len()`](len/README.md) — Return the length (the number of items) of an object.
- [`list()`](list/README.md) — Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.
- [`locals()`](locals/README.md) — Return a mapping object representing the current local symbol table, with variable names as the keys, and their currently bound references as the…
- [`map()`](map/README.md) — Return an iterator that applies *function* to every item of *iterable*, yielding the results.
- [`max()`](max/README.md) — Return the largest item in an iterable or the largest of two or more arguments.
- [`memoryview()`](memoryview/README.md) — Return a "memory view" object created from the given argument.
- [`min()`](min/README.md) — Return the smallest item in an iterable or the smallest of two or more arguments.
- [`next()`](next/README.md) — Retrieve the next item from the iterator by calling its __next__() method.
- [`object()`](object/README.md) — This is the ultimate base class of all other classes.
- [`oct()`](oct/README.md) — Convert an integer number to an octal string prefixed with "0o".
- [`open()`](open/README.md) — Open *file* and return a corresponding file object.
- [`ord()`](ord/README.md) — Return the ordinal value of a character.
- [`pow()`](pow/README.md) — Return *base* to the power *exp*; if *mod* is present, return *base* to the power *exp*, modulo *mod* (computed more efficiently than pow(base,…
- [`print()`](print/README.md) — Print *objects* to the text stream *file*, separated by *sep* and followed by *end*.
- [`property()`](property/README.md) — Return a property attribute.
- [`range()`](range/README.md) — Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.
- [`repr()`](repr/README.md) — Return a string containing a printable representation of an object.
- [`reversed()`](reversed/README.md) — Return a reverse iterator.
- [`round()`](round/README.md) — Return *number* rounded to *ndigits* precision after the decimal point.
- [`set()`](set/README.md) — Return a new set object, optionally with elements taken from *iterable*.
- [`setattr()`](setattr/README.md) — This is the counterpart of getattr().
- [`sentinel()`](sentinel/README.md) — Return a new unique sentinel object.
- [`slice()`](slice/README.md) — Return a slice object representing the set of indices specified by range(start, stop, step).
- [`sorted()`](sorted/README.md) — Return a new sorted list from the items in *iterable*.
- [`@staticmethod`](staticmethod/README.md) — Transform a method into a static method.
- [`str()`](str/README.md) — Return a str version of *object*.
- [`sum()`](sum/README.md) — Sums *start* and the items of an *iterable* from left to right and returns the total.
- [`super()`](super/README.md) — Return a proxy object that delegates method calls to a parent or sibling class of *type*.
- [`tuple()`](tuple/README.md) — Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.
- [`type()`](type/README.md) — With one argument, return the type of an *object*.
- [`vars()`](vars/README.md) — Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
- [`zip()`](zip/README.md) — Iterate over several iterables in parallel, producing tuples with an item from each one.
- [`__import__()`](__import__/README.md) — This function is invoked by the import statement.
