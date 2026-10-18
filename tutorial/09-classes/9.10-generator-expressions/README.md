## 9.10. Generator Expressions

Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

Examples:

``` python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

>>> x = [[1,2,3], [], [4, 5]]
>>> g = (*i for i in x)
>>> list(g)
[1, 2, 3, 4, 5]
```
> Code: [xvec.py](xvec.py)

In most cases, generator expressions must be wrapped in parentheses. As a special case, however, when provided as the sole argument to a function (as in the examples involving `sum`, `set`, `max`, and `list` above), the generator expression does not need to be wrapped in an additional set of parentheses. That is to say, the following two pieces of code are semantically equivalent:

``` python
>>> f(x for x in y)
>>> f((x for x in y))
```
> Code: [example_01.py](example_01.py)

as are the following:

``` python
>>> f(*x for x in y)
>>> f((*x for x in y))
```
> Code: [example_02.py](example_02.py)
