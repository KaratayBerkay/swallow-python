# Built-in Constants

A small number of constants live in the built-in namespace.  They are:

> **Note**
>
> The names [None](None/README.md), [False](False/README.md), [True](True/README.md) and [__debug__](__debug__/README.md)
> cannot be reassigned (assignments to them, even as an attribute name, raise
> [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError)), so they can be considered "true" constants.

## Contents

- [`False`](False/README.md) — The false value of the bool type.
- [`True`](True/README.md) — The true value of the bool type.
- [`None`](None/README.md) — An object frequently used to represent the absence of a value, as when default arguments are not passed to a function.
- [`NotImplemented`](NotImplemented/README.md) — A special value which should be returned by the binary special methods (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the…
- [`Ellipsis`](Ellipsis/README.md) — The same as the ellipsis literal "...", an object frequently used to indicate that something is omitted.
- [`__debug__`](__debug__/README.md) — This constant is true if Python was not started with an -O option.

## Constants added by the `site` module

The [site](https://docs.python.org/3.15/library/site.html#module-site) module (which is imported automatically during startup, except
if the [-S](https://docs.python.org/3.15/using/cmdline.html#cmdoption-S) command-line option is given) adds several constants to the
built-in namespace.  They are useful for the interactive interpreter shell and
should not be used in programs.

- [`quit()`](constants-added-by-the-site-module/quit/README.md) — Objects that when printed, print a message like "Use quit() or Ctrl-D (i.e. EOF) to exit", and when accessed directly in the interactive…
- [`help`](constants-added-by-the-site-module/help/README.md) — Object that when printed, prints the message "Type help() for interactive help, or help(object) for help about object.", and when accessed…
- [`copyright`](constants-added-by-the-site-module/copyright/README.md) — Objects that when printed or called, print the text of copyright or credits, respectively.
- [`license`](constants-added-by-the-site-module/license/README.md) — Object that when printed, prints the message "Type license() to see the full license text", and when called, displays the full license text in a…
- [`exit()`](constants-added-by-the-site-module/exit/README.md) — Documented together with quit().
- [`credits`](constants-added-by-the-site-module/credits/README.md) — Documented together with copyright.
