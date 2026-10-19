## `help()`

```
help()
help(request)
```

Invoke the built-in help system.  (This function is intended for interactive
use.)  If no argument is given, the interactive help system starts on the
interpreter console.  If the argument is a string, then the string is looked up
as the name of a module, function, class, method, keyword, or documentation
topic, and a help page is printed on the console.  If the argument is any other
kind of object, a help page on the object is generated.

Note that if a slash(/) appears in the parameter list of a function when
invoking help(), it means that the parameters prior to the slash are
positional-only. For more info, see
[the FAQ entry on positional-only parameters](https://docs.python.org/3.15/faq/programming.html#faq-positional-only-arguments).

This function is added to the built-in namespace by the [site](https://docs.python.org/3.15/library/site.html#module-site) module.

> *Changed in version 3.4:* Changes to [pydoc](https://docs.python.org/3.15/library/pydoc.html#module-pydoc) and [inspect](https://docs.python.org/3.15/library/inspect.html#module-inspect) mean that the reported
> signatures for callables are now more comprehensive and consistent.
