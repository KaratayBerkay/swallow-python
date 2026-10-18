### 5.1.5. Unpacking in Lists and List Comprehensions

The section on Unpacking Argument Lists describes the use of `*` to "unpack" the elements of an iterable object, providing each one separately as an argument to a function. Unpacking can also be used in other contexts, for example, when creating lists. When specifying elements of a list, prefixing an expression by a `*` will unpack the result of that expression, adding each of its elements to the list we're creating:

``` python
>>> x = [1, 2, 3]
>>> [0, *x, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
```
> Code: [x.py](x.py)

This only works if the expression following the `*` evaluates to an iterable object; trying to unpack a non-iterable object will raise an exception:

``` python
>>> x = 1
>>> [0, *x, 2, 3, 4]
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    [0, *x, 2, 3, 4]
TypeError: Value after * must be an iterable, not int
```
> Code: [x_2.py](x_2.py)

Unpacking can also be used in list comprehensions, as a way to build a new list representing the concatenation of an arbitrary number of iterables:

``` python
>>> x = [[1, 2, 3], [4, 5, 6], [], [7], [8, 9]]
>>> [*element for element in x]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
> Code: [x_3.py](x_3.py)

Note that the effect is that each element from `x` is unpacked. This works for arbitrary iterable objects, not just lists:

``` python
>>> x = [[1, 2, 3], 'cat', {'spam': 'eggs'}]
>>> [*element for element in x]
[1, 2, 3, 'c', 'a', 't', 'spam']
```
> Code: [x_4.py](x_4.py)

But if the objects in `x` are not iterable, this expression would again raise an exception.
