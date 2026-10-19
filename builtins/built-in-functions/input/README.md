## `input()`

```
input()
input(prompt, /)
```

If the *prompt* argument is present, it is written to standard output without
a trailing newline.  The function then reads a line from input, converts it
to a string (stripping a trailing newline), and returns that.  When EOF is
read, [EOFError](https://docs.python.org/3.15/builtins/exceptions.html#EOFError) is raised.  Example:

``` python
>>> s = input('--> ')  # doctest: +SKIP
--> Monty Python's Flying Circus
>>> s  # doctest: +SKIP
"Monty Python's Flying Circus"
```

If the [readline](https://docs.python.org/3.15/library/readline.html#module-readline) module was loaded, then input() will use it
to provide elaborate line editing and history features.

Raises an [auditing event](https://docs.python.org/3.15/library/sys.html#auditing) `builtins.input` with
argument `prompt` before reading input

Raises an [auditing event](https://docs.python.org/3.15/library/sys.html#auditing) `builtins.input/result`
with the result after successfully reading input.
