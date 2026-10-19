## `str.casefold`

```
str.casefold()
```

Return a casefolded copy of the string. Casefolded strings may be used for
caseless matching.

Casefolding is similar to lowercasing but more aggressive because it is
intended to remove all case distinctions in a string. For example, the German
lowercase letter `'ß'` is equivalent to `"ss"`. Since it is already
lowercase, `lower()` would do nothing to `'ß'`; `casefold()`
converts it to `"ss"`.
For example:

``` python
>>> 'straße'.lower()
'straße'
>>> 'straße'.casefold()
'strasse'
```
> Code: [example_01.py](example_01.py)

The casefolding algorithm is [described in section 3.13.3 'Default Case
Folding' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G53253).

> *Added in version 3.3.*
