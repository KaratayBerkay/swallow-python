#### 4.9.3.4. Function Examples

Consider the following example function definitions paying close attention to the markers `/` and `*`:

``` python
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```
> Code: [standard_arg.py](standard_arg.py)

The first function definition, `standard_arg`, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:

``` python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2
```
> Code: [example_01.py](example_01.py)

The second function `pos_only_arg` is restricted to only use positional parameters as there is a `/` in the function definition:

``` python
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
```
> Code: [example_02.py](example_02.py)

The third function `kwd_only_arg` only allows keyword arguments as indicated by a `*` in the function definition:

``` python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3
```
> Code: [example_03.py](example_03.py)

And the last uses all three calling conventions in the same function definition:

``` python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
```
> Code: [example_04.py](example_04.py)

Finally, consider this function definition which has a potential collision between the positional argument `name` and `**kwds` which has `name` as a key:

``` python
def foo(name, **kwds):
    return 'name' in kwds
```
> Code: [foo.py](foo.py)

There is no possible call that will make it return `True` as the keyword `'name'` will always bind to the first parameter. For example:

``` python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>
```
> Code: [example_05.py](example_05.py)

But using `/` (positional only arguments), it is possible since it allows `name` as a positional argument and `'name'` as a key in the keyword arguments:

``` python
>>> def foo(name, /, **kwds):
...     return 'name' in kwds
...
>>> foo(1, **{'name': 2})
True
```
> Code: [foo_2.py](foo_2.py)

In other words, the names of positional-only parameters can be used in `**kwds` without ambiguity.
