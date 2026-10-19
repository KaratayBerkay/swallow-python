## `str.title`

```
str.title()
```

Return a titlecased version of the string where words start with an uppercase
character and the remaining characters are lowercase.

For example:

``` python
>>> 'Hello world'.title()
'Hello World'
```
> Code: [example_01.py](example_01.py)

The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result:

``` python
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"
```
> Code: [example_02.py](example_02.py)

The [string.capwords()](https://docs.python.org/3.15/library/string.html#string.capwords) function does not have this problem, as it
splits words on spaces only.

Alternatively, a workaround for apostrophes can be constructed using regular
expressions:

``` python
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0).capitalize(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."
```
> Code: [example_03.py](example_03.py)

See also `istitle()`.
