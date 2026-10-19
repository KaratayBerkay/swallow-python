## `str.strip`

```
str.strip(chars=None, /)
```

Return a copy of the string with the leading and trailing characters removed.
The *chars* argument is a string specifying the set of characters to be removed.
If omitted or `None`, the *chars* argument defaults to removing whitespace.
The *chars* argument is not a prefix or suffix; rather, all combinations of its
values are stripped.

Whitespace characters are defined by [str.isspace()](../str.isspace/README.md).

For example:

``` python
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
```
> Code: [example_01.py](example_01.py)

The outermost leading and trailing *chars* argument values are stripped
from the string. Characters are removed from the leading end until
reaching a string character that is not contained in the set of
characters in *chars*. A similar action takes place on the trailing end.

For example:

``` python
>>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
>>> comment_string.strip('.#! ')
'Section 3.2.1 Issue #32'
```
> Code: [example_02.py](example_02.py)

See also `rstrip()`.

## Çözümlü kısa örnek

Chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur

```python
print(repr(" a ".strip()))
# Sonuç: 'a'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.43: str.strip davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur

```python
"abbaXba".strip("ab")
"abXabYab".strip("ab")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'X'`; `'XabY'`.
- [ ] Chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.swapcase/README.md)
<!-- learning-task:end -->
