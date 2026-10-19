## `str.isascii`

```
str.isascii()
```

Return `True` if the string is empty or all characters in the string are ASCII,
`False` otherwise.
ASCII characters have code points in the range U+0000-U+007F. For example:

``` python
>>> 'ASCII characters'.isascii()
True
>>> 'µ'.isascii()
False
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.7.*

## Çözümlü kısa örnek

ASCII sınırı ile boş girdinin özel sonucunu göster

```python
print(repr("abc".isascii()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.16: str.isascii davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII sınırı ile boş girdinin özel sonucunu göster

```python
"".isascii()
"İ".isascii()
"".isascii()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `True`.
- [ ] ASCII sınırı ile boş girdinin özel sonucunu göster

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isdecimal/README.md)
<!-- learning-task:end -->
