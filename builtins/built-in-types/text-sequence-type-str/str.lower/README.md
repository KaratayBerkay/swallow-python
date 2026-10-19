## `str.lower`

```
str.lower()
```

Return a copy of the string with all the cased characters [^1] converted to
lowercase. For example:

``` python
>>> 'Lower Method Example'.lower()
'lower method example'
```
> Code: [example_01.py](example_01.py)

The lowercasing algorithm used is [described in section 3.13.2 'Default Case
Conversion' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G34078).

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).
