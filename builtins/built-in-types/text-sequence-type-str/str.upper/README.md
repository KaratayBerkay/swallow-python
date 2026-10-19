## `str.upper`

```
str.upper()
```

Return a copy of the string with all the cased characters [^1] converted to
uppercase.  Note that `s.upper().isupper()` might be `False` if `s`
contains uncased characters or if the Unicode category of the resulting
character(s) is not "Lu" (Letter, uppercase), but e.g. "Lt" (Letter,
titlecase).

The uppercasing algorithm used is [described in section 3.13.2 'Default Case
Conversion' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G34078).

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).
