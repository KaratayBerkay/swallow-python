The interpreter supports several other kinds of objects. Most of these support
only one or two operations.

## Modules

The only special operation on a module is attribute access: `m.name`, where
*m* is a module and *name* accesses a name defined in *m*'s symbol table.
Module attributes can be assigned to.  (Note that the `import`
statement is not, strictly speaking, an operation on a module object; `import
foo` does not require a module object named *foo* to exist, rather it requires
an (external) *definition* for a module named *foo* somewhere.)

A special attribute of every module is [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__). This is the
dictionary containing the module's symbol table. Modifying this dictionary will
actually change the module's symbol table, but direct assignment to the
[__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) attribute is not possible (you can write
`m.__dict__['a'] = 1`, which defines `m.a` to be `1`, but you can't write
`m.__dict__ = {}`).  Modifying [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) directly is
not recommended.

Modules built into the interpreter are written like this: `<module 'sys'
(built-in)>`.  If loaded from a file, they are written as `<module 'os' from
'/usr/local/lib/pythonX.Y/os.pyc'>`.

## Classes and Class Instances

See [Objects, values and types](https://docs.python.org/3.15/reference/datamodel.html#objects) and [Class definitions](https://docs.python.org/3.15/reference/compound_stmts.html#class) for these.

## Functions

Function objects are created by function definitions.  The only operation on a
function object is to call it: `func(argument-list)`.

There are really two flavors of function objects: built-in functions and
user-defined functions.  Both support the same operation (to call the function),
but the implementation is different, hence the different object types.

See [Function definitions](https://docs.python.org/3.15/reference/compound_stmts.html#function) for more information.

## Methods

Methods are functions that are called using the attribute notation.
There are two flavors: [built-in methods](https://docs.python.org/3.15/reference/datamodel.html#builtin-methods)
(such as [append()](../sequence-types-list-tuple-range/bytearray.append/README.md) on lists)
and [class instance methods](https://docs.python.org/3.15/reference/datamodel.html#instance-methods).
Built-in methods are described with the types that support them.

If you access a method (a function defined in a class namespace) through an
instance, you get a special object: a bound method (also called
[instance method](https://docs.python.org/3.15/reference/datamodel.html#instance-methods)) object. When called, it will add
the `self` argument
to the argument list.  Bound methods have two special read-only attributes:
[m.__self__](https://docs.python.org/3.15/reference/datamodel.html#method.__self__) is the object on which the method
operates, and [m.__func__](https://docs.python.org/3.15/reference/datamodel.html#method.__func__) is
the function implementing the method.  Calling `m(arg-1, arg-2, ..., arg-n)`
is completely equivalent to calling `m.__func__(m.__self__, arg-1, arg-2, ...,
arg-n)`.

Like [function objects](https://docs.python.org/3.15/reference/datamodel.html#user-defined-funcs), bound method objects support
getting arbitrary
attributes.  However, since method attributes are actually stored on the
underlying function object ([method.__func__](https://docs.python.org/3.15/reference/datamodel.html#method.__func__)), setting method attributes on
bound methods is disallowed.  Attempting to set an attribute on a method
results in an [AttributeError](https://docs.python.org/3.15/builtins/exceptions.html#AttributeError) being raised.  In order to set a method
attribute, you need to explicitly set it on the underlying function object:

``` python
>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'my name is method'  # can't set on the method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'method' object has no attribute 'whoami'
>>> c.method.__func__.whoami = 'my name is method'
>>> c.method.whoami
'my name is method'
```
> Code: [example_01.py](example_01.py)

See [Instance methods](https://docs.python.org/3.15/reference/datamodel.html#instance-methods) for more information.

## Code Objects

Code objects are used by the implementation to represent "pseudo-compiled"
executable Python code such as a function body. They differ from function
objects because they don't contain a reference to their global execution
environment.  Code objects are returned by the built-in [compile()](../../built-in-functions/compile/README.md) function
and can be extracted from function objects through their
[__code__](https://docs.python.org/3.15/reference/datamodel.html#function.__code__) attribute. See also the [code](https://docs.python.org/3.15/library/code.html#module-code) module.

Accessing [__code__](https://docs.python.org/3.15/reference/datamodel.html#function.__code__) raises an [auditing event](https://docs.python.org/3.15/library/sys.html#auditing)
`object.__getattr__` with arguments `obj` and `"__code__"`.

A code object can be executed or evaluated by passing it (instead of a source
string) to the [exec()](../../built-in-functions/exec/README.md) or [eval()](../../built-in-functions/eval/README.md)  built-in functions.

See [The standard type hierarchy](https://docs.python.org/3.15/reference/datamodel.html#types) for more information.

## Type Objects

Type objects represent the various object types.  An object's type is accessed
by the built-in function [type()](../../built-in-functions/type/README.md).  There are no special operations on
types.  The standard module [types](https://docs.python.org/3.15/library/types.html#module-types) defines names for all standard built-in
types.

Types are written like this: `<class 'int'>`.

## The Null Object

This object is returned by functions that don't explicitly return a value.  It
supports no special operations.  There is exactly one null object, named
`None` (a built-in name).  `type(None)()` produces the same singleton.

It is written as `None`.

## The Ellipsis Object

This object is commonly used to indicate that something is omitted.
It supports no special operations.  There is exactly one ellipsis object, named
[Ellipsis](https://docs.python.org/3.15/builtins/constants.html#Ellipsis) (a built-in name).  `type(Ellipsis)()` produces the
[Ellipsis](https://docs.python.org/3.15/builtins/constants.html#Ellipsis) singleton.

It is written as `Ellipsis` or `...`.

In typical use, `...` as the `Ellipsis` object appears in a few different
places, for instance:

- In type annotations, such as [callable arguments](https://docs.python.org/3.15/library/typing.html#annotating-callables)
  or [tuple elements](https://docs.python.org/3.15/library/typing.html#annotating-tuples).

- As the body of a function instead of a [pass statement](https://docs.python.org/3.15/tutorial/controlflow.html#tut-pass).

- In third-party libraries, such as [Numpy's slicing and striding](https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding).

Python also uses three dots in ways that are not `Ellipsis` objects, for instance:

- Doctest's [ELLIPSIS](https://docs.python.org/3.15/library/doctest.html#doctest.ELLIPSIS), as a pattern for missing content.

- The default Python prompt of the [interactive](https://docs.python.org/3.15/glossary.html#term-interactive) shell when partial input is incomplete.

Lastly, the Python documentation often uses three dots in conventional English
usage to mean omitted content, even in code examples that also use them as the
`Ellipsis`.

## The NotImplemented Object

This object is returned from comparisons and binary operations when they are
asked to operate on types they don't support. See [Comparisons](https://docs.python.org/3.15/reference/expressions.html#comparisons) for more
information.  There is exactly one [NotImplemented](https://docs.python.org/3.15/builtins/constants.html#NotImplemented) object.
`type(NotImplemented)()` produces the singleton instance.

It is written as `NotImplemented`.

## Internal Objects

See [The standard type hierarchy](https://docs.python.org/3.15/reference/datamodel.html#types) for this information.  It describes
[stack frame objects](https://docs.python.org/3.15/reference/datamodel.html#frame-objects),
[traceback objects](https://docs.python.org/3.15/reference/datamodel.html#traceback-objects), and slice objects.
