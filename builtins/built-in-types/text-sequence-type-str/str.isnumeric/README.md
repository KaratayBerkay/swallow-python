## `str.isnumeric`

```
str.isnumeric()
```

Return `True` if all characters in the string are numeric
characters, and there is at least one character, `False`
otherwise. Numeric characters include digit characters, and all characters
that have the Unicode numeric value property, e.g. U+2155,
VULGAR FRACTION ONE FIFTH.  Formally, numeric characters are those with the property
value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.
For example:

``` python
>>> '0123456789'.isnumeric()
True
>>> '٠١٢٣٤٥٦٧٨٩'.isnumeric()  # Arabic-Indic digits zero to nine
True
>>> '⅕'.isnumeric()  # Vulgar fraction one fifth
True
>>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
(False, True, True)
```
> Code: [example_01.py](example_01.py)

See also `isdecimal()` and `isdigit()`.

## Çözümlü kısa örnek

Numeric karakter, int ile okunabilen decimal metin demek değildir

```python
print(repr("12".isnumeric()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.21: str.isnumeric davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; numeric karakter, int ile okunabilen decimal metin demek değildir

```python
"⅕".isnumeric()
"-2".isnumeric()
"".isnumeric()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Numeric karakter, int ile okunabilen decimal metin demek değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isprintable/README.md)
<!-- learning-task:end -->
