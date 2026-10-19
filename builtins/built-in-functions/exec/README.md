## `exec()`

```
exec(source, /, globals=None, locals=None, *, closure=None)
```

> **Warning**
>
> This function executes arbitrary code. Calling it with
> untrusted user-supplied input will lead to security vulnerabilities.

This function supports dynamic execution of Python code. *source* must be
either a string or a code object.  If it is a string, the string is parsed as
a suite of Python statements which is then executed (unless a syntax error
occurs). [^1] If it is a code object, it is simply executed.  In all cases,
the code that's executed is expected to be valid as file input (see the
section [File input](https://docs.python.org/3.15/reference/toplevel_components.html#file-input) in the Reference Manual). Be aware that the
`nonlocal`, `yield`,  and `return`
statements may not be used outside of
function definitions even within the context of code passed to the
exec() function. The return value is `None`.

In all cases, if the optional parts are omitted, the code is executed in the
current scope.  If only *globals* is provided, it must be a dictionary
(and not a subclass of dictionary), which
will be used for both the global and the local variables.  If *globals* and
*locals* are given, they are used for the global and local variables,
respectively.  If provided, *locals* can be any mapping object.  Remember
that at the module level, globals and locals are the same dictionary.

> **Note**
>
> When `exec` gets two separate objects as *globals* and *locals*, the
> code will be executed as if it were embedded in a class definition. This
> means functions and classes defined in the executed code will not be able
> to access variables assigned at the top level (as the "top level"
> variables are treated as class variables in a class definition).

If the *globals* dictionary does not contain a value for the key
`__builtins__`, a reference to the dictionary of the built-in module
[builtins](https://docs.python.org/3.15/library/builtins.html#module-builtins) is inserted under that key.
Overriding `__builtins__` can be used to restrict or change the available
names, but this is **not** a security mechanism: the executed code can
still access all builtins.

The *closure* argument specifies a closure--a tuple of cellvars.
It's only valid when the *object* is a code object containing
[free (closure) variables](https://docs.python.org/3.15/glossary.html#term-closure-variable).
The length of the tuple must exactly match the length of the code object's
[co_freevars](https://docs.python.org/3.15/reference/datamodel.html#codeobject.co_freevars) attribute.

Raises an [auditing event](https://docs.python.org/3.15/library/sys.html#auditing) `exec` with the code object
as the argument. Code compilation events may also be raised.

> **Note**
>
> The built-in functions [globals()](../globals/README.md) and [locals()](../locals/README.md) return the current
> global and local namespace, respectively, which may be useful to pass around
> for use as the second and third argument to exec().

> **Note**
>
> The default *locals* act as described for function [locals()](../locals/README.md) below.
> Pass an explicit *locals* dictionary if you need to see effects of the
> code on *locals* after function exec() returns.

> *Changed in version 3.11:* Added the *closure* parameter.

> *Changed in version 3.13:* The *globals* and *locals* arguments can now be passed as keywords.

> *Changed in version 3.13:* The semantics of the default *locals* namespace have been adjusted as
> described for the [locals()](../locals/README.md) builtin.

> *Changed in version 3.15:* *globals* can now be a [frozendict](../frozendict/README.md).

[^1]: Note that the parser only accepts the Unix-style end of line convention. If you are reading the code from a file, make sure to use newline conversion mode to convert Windows or Mac-style newlines.
