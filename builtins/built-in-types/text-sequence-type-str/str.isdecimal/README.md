## `str.isdecimal`

```
str.isdecimal()
```

Return `True` if all characters in the string are decimal
characters and there is at least one character, `False`
otherwise. Decimal characters are those that can be used to form
numbers in base 10, such as U+0660, ARABIC-INDIC DIGIT
ZERO.  Formally a decimal character is a character in the Unicode
General Category "Nd". For example:

``` python
>>> '0123456789'.isdecimal()
True
>>> '٠١٢٣٤٥٦٧٨٩'.isdecimal()  # Arabic-Indic digits zero to nine
True
>>> 'alphabetic'.isdecimal()
False
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Decimal rakamla tüm sayısal Unicode karakterlerini ayır

```python
print(repr("12".isdecimal()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.17: str.isdecimal davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; decimal rakamla tüm sayısal Unicode karakterlerini ayır

```python
"١٢".isdecimal()
"²".isdecimal()
"".isdecimal()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Decimal rakamla tüm sayısal Unicode karakterlerini ayır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isdigit/README.md)
<!-- learning-task:end -->
