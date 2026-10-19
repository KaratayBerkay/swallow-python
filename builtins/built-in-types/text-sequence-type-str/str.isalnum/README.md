## `str.isalnum`

```
str.isalnum()
```

Return `True` if all characters in the string are alphanumeric and there is at
least one character, `False` otherwise.  A character `c` is alphanumeric if one
of the following returns `True`: `c.isalpha()`, `c.isdecimal()`,
`c.isdigit()`, or `c.isnumeric()`. For example:

``` python
>>> 'abc123'.isalnum()
True
>>> 'abc123!@#'.isalnum()
False
>>> ''.isalnum()
False
>>> ' '.isalnum()
False
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Her karakter uygun ve en az bir karakter bulunmalıdır

```python
print(repr("a1".isalnum()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.14: str.isalnum davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; her karakter uygun ve en az bir karakter bulunmalıdır

```python
"İ2".isalnum()
"a b".isalnum()
"".isalnum()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Her karakter uygun ve en az bir karakter bulunmalıdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isalpha/README.md)
<!-- learning-task:end -->
