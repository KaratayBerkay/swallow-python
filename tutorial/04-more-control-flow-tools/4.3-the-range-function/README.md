## 4.3. The `range()` Function

If you do need to iterate over a sequence of numbers, the built-in function `range()` comes in handy. It generates arithmetic progressions:

``` python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```
> Code: [example_01.py](example_01.py)

The given end point is never part of the generated sequence; `range(10)` generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the 'step'):

``` python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```
> Code: [example_02.py](example_02.py)

To iterate over the indices of a sequence, you can combine `range()` and `len()` as follows:

``` python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```
> Code: [a.py](a.py)

In most such cases, however, it is convenient to use the `enumerate()` function, see Looping Techniques.

A strange thing happens if you just print a range:

``` python
>>> range(10)
range(0, 10)
```
> Code: [example_03.py](example_03.py)

In many ways the object returned by `range()` behaves as if it is a list, but in fact it isn't. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn't really make the list, thus saving space.

We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the `for` statement is such a construct, while an example of a function that takes an iterable is `sum()`:

``` python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```
> Code: [example_04.py](example_04.py)

Later we will see more functions that return iterables and take iterables as arguments. In chapter Data Structures, we will discuss `list()` in more detail.
