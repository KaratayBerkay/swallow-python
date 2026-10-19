## `compile()`

```
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, *, module=None)
```

Compile the *source* into a code or AST object.  Code objects can be executed
by [exec()](../exec/README.md) or [eval()](../eval/README.md).  *source* can either be a normal string, a
byte string, or an AST object.  Refer to the [ast](https://docs.python.org/3.15/library/ast.html#module-ast) module documentation
for information on how to work with AST objects.

The *filename* argument should give the file from which the code was read;
pass some recognizable value if it wasn't read from a file (`'<string>'` is
commonly used).

The *mode* argument specifies what kind of code must be compiled; it can be
`'exec'` if *source* consists of a sequence of statements, `'eval'` if it
consists of a single expression, or `'single'` if it consists of a single
interactive statement (in the latter case, expression statements that
evaluate to something other than `None` will be printed).

The optional arguments *flags* and *dont_inherit* control which
[compiler options](https://docs.python.org/3.15/library/ast.html#ast-compiler-flags) should be activated
and which [future features](https://docs.python.org/3.15/reference/simple_stmts.html#future) should be allowed. If neither
is present (or both are zero) the code is compiled with the same flags that
affect the code that is calling compile(). If the *flags*
argument is given and *dont_inherit* is not (or is zero) then the compiler
options and the future statements specified by the *flags* argument are used
in addition to those that would be used anyway. If *dont_inherit* is a
non-zero integer then the *flags* argument is it -- the flags (future
features and compiler options) in the surrounding code are ignored.

Compiler options and future statements are specified by bits which can be
bitwise ORed together to specify multiple options. The bitfield required to
specify a given future feature can be found as the
[compiler_flag](https://docs.python.org/3.15/library/__future__.html#future__._Feature.compiler_flag) attribute on the
[_Feature](https://docs.python.org/3.15/library/__future__.html#future__._Feature) instance in the [__future__](https://docs.python.org/3.15/library/__future__.html#module-__future__) module.
[Compiler flags](https://docs.python.org/3.15/library/ast.html#ast-compiler-flags) can be found in [ast](https://docs.python.org/3.15/library/ast.html#module-ast)
module, with `PyCF_` prefix.

The argument *optimize* specifies the optimization level of the compiler; the
default value of `-1` selects the optimization level of the interpreter as
given by [-O](https://docs.python.org/3.15/using/cmdline.html#cmdoption-O) options.  Explicit levels are `0` (no optimization;
`__debug__` is true), `1` (asserts are removed, `__debug__` is false)
or `2` (docstrings are removed too).

The optional argument *module* specifies the module name.
It is needed to unambiguous [filter](https://docs.python.org/3.15/library/warnings.html#warning-filter) syntax warnings
by module name.

This function raises [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError) if the compiled source is invalid,
including a *source* containing a null character or that cannot be decoded;
[ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) if *mode* or *flags* is invalid,
or if a string *source* contains surrogate characters;
[MemoryError](https://docs.python.org/3.15/builtins/exceptions.html#MemoryError) or [RecursionError](https://docs.python.org/3.15/builtins/exceptions.html#RecursionError) if *source* is too complex
to parse or compile,
for example an expression with many thousands of nested operators;
and [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) if *source* is too large.

If you want to parse Python code into its AST representation, see
[ast.parse()](https://docs.python.org/3.15/library/ast.html#ast.parse).

Raises an [auditing event](https://docs.python.org/3.15/library/sys.html#auditing) `compile` with arguments
`source` and `filename`. This event may also be raised by implicit
compilation.

> **Note**
>
> When compiling a string with multi-line code in `'single'` or
> `'eval'` mode, input must be terminated by at least one newline
> character.  This is to facilitate detection of incomplete and complete
> statements in the [code](https://docs.python.org/3.15/library/code.html#module-code) module.

> **Warning**
>
> It is possible to crash the Python interpreter with a
> sufficiently large/complex string when compiling to an AST
> object due to stack depth limitations in Python's AST compiler.

> *Changed in version 3.2:* Allowed use of Windows and Mac newlines.  Also, input in `'exec'` mode
> does not have to end in a newline anymore.  Added the *optimize* parameter.

> *Changed in version 3.5:* Previously, [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) was raised when null bytes were encountered
> in *source*.

> *Changed in version 3.8:* `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` can now be passed in flags to enable
> support for top-level `await`, `async for`, and `async with`.

> *Changed in version 3.12:* [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError) is raised instead of [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when null bytes
> are encountered in *source*.

> *Changed in version 3.15:* Added the *module* parameter.
