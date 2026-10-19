## `breakpoint()`

```
breakpoint(*args, **kws)
```

This function drops you into the debugger at the call site.  Specifically,
it calls [sys.breakpointhook()](https://docs.python.org/3.15/library/sys.html#sys.breakpointhook), passing `args` and `kws` straight
through.  By default, `sys.breakpointhook()` calls
[pdb.set_trace()](https://docs.python.org/3.15/library/pdb.html#pdb.set_trace) expecting no arguments.  In this case, it is
purely a convenience function so you don't have to explicitly import
[pdb](https://docs.python.org/3.15/library/pdb.html#module-pdb) or type as much code to enter the debugger.  However,
[sys.breakpointhook()](https://docs.python.org/3.15/library/sys.html#sys.breakpointhook) can be set to some other function and
breakpoint() will automatically call that, allowing you to drop into
the debugger of choice.
If [sys.breakpointhook()](https://docs.python.org/3.15/library/sys.html#sys.breakpointhook) is not accessible, this function will
raise [RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError).

By default, the behavior of breakpoint() can be changed with
the [PYTHONBREAKPOINT](https://docs.python.org/3.15/using/cmdline.html#envvar-PYTHONBREAKPOINT) environment variable.
See [sys.breakpointhook()](https://docs.python.org/3.15/library/sys.html#sys.breakpointhook) for usage details.

Note that this is not guaranteed if [sys.breakpointhook()](https://docs.python.org/3.15/library/sys.html#sys.breakpointhook)
has been replaced.

Raises an auditing event `builtins.breakpoint` with argument `breakpointhook`.

> *Added in version 3.7.*
