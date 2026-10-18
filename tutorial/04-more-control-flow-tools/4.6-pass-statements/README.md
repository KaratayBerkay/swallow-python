## 4.6. `pass` Statements

The `pass` statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

``` python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```
> Code: [example_01.py](example_01.py)

This is commonly used for creating minimal classes:

``` python
>>> class MyEmptyClass:
...     pass
...
```
> Code: [my_empty_class.py](my_empty_class.py)

Another place `pass` can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The `pass` is silently ignored:

``` python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```
> Code: [initlog.py](initlog.py)

For this last case, many people use the ellipsis literal `...` instead of `pass`. This use has no special meaning to Python, and is not part of the language definition (you could use any constant expression here), but `...` is used conventionally as a placeholder body as well. See The Ellipsis Object.
