## `str.isupper`

```
str.isupper()
```

Return `True` if all cased characters [^1] in the string are uppercase and
there is at least one cased character, `False` otherwise.

``` python
>>> 'BANANA'.isupper()
True
>>> 'banana'.isupper()
False
>>> 'baNana'.isupper()
False
>>> ' '.isupper()
False
```
> Code: [example_01.py](example_01.py)

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).

## Çözümlü kısa örnek

Rakamlar case denetimi dışında kalır; en az bir cased karakter gerekir

```python
print(repr("ADA".isupper()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.25: str.isupper davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; rakamlar case denetimi dışında kalır; en az bir cased karakter gerekir

```python
"ADA 12!".isupper()
"Ada".isupper()
"123".isupper()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Rakamlar case denetimi dışında kalır; en az bir cased karakter gerekir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.ljust/README.md)
<!-- learning-task:end -->
