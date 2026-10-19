## `str.istitle`

```
str.istitle()
```

Return `True` if the string is a titlecased string and there is at least one
character, for example uppercase characters may only follow uncased characters
and lowercase characters only cased ones.  Return `False` otherwise.

For example:

``` python
>>> 'Spam, Spam, Spam'.istitle()
True
>>> 'spam, spam, spam'.istitle()
False
>>> 'SPAM, SPAM, SPAM'.istitle()
False
```
> Code: [example_01.py](example_01.py)

See also `title()`.
