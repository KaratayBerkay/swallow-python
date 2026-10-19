## `str.isdigit`

```
str.isdigit()
```

Return `True` if all characters in the string are digits and there is at least one
character, `False` otherwise.  Digits include decimal characters and digits that need
special handling, such as the compatibility superscript digits.
This covers digits which cannot be used to form numbers in base 10,
like the [Kharosthi numbers](https://en.wikipedia.org/wiki/Kharosthi#Numerals).
Formally, a digit is a character that has the
property value Numeric_Type=Digit or Numeric_Type=Decimal.

For example:

``` python
>>> '0123456789'.isdigit()
True
>>> '٠١٢٣٤٥٦٧٨٩'.isdigit()  # Arabic-Indic digits zero to nine
True
>>> '⅕'.isdigit()  # Vulgar fraction one fifth
False
>>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
(False, True, True)
```
> Code: [example_01.py](example_01.py)

See also `isdecimal()` and `isnumeric()`.

## Çözümlü kısa örnek

Üst simge rakam kabul edilir; kesir her zaman digit değildir

```python
print(repr("12".isdigit()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.18: str.isdigit davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; üst simge rakam kabul edilir; kesir her zaman digit değildir

```python
"²".isdigit()
"⅕".isdigit()
"".isdigit()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Üst simge rakam kabul edilir; kesir her zaman digit değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isidentifier/README.md)
<!-- learning-task:end -->
