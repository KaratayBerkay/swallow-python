## `str.startswith`

```
str.startswith(prefix[, start[, end]])
```

Return `True` if string starts with the *prefix*, otherwise return `False`.
*prefix* can also be a tuple of prefixes to look for.  With optional *start*,
test string beginning at that position.  With optional *end*, stop comparing
string at that position.

For example:

``` python
>>> 'Python'.startswith('Py')
True
>>> 'a tuple of prefixes'.startswith(('at', 'a'))
True
>>> 'Python is amazing'.startswith('is', 7)
True
```
> Code: [example_01.py](example_01.py)

See also `endswith()` and `removeprefix()`.

## Çözümlü kısa örnek

Tuple seçenekleriyle başlangıç dilimini ayır

```python
print(repr("ad.py".startswith("ad")))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.42: str.startswith davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tuple seçenekleriyle başlangıç dilimini ayır

```python
"ad.py".startswith(("x","ad"))
"xxad".startswith("ad",2)
"abc".startswith("z")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] Tuple seçenekleriyle başlangıç dilimini ayır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.strip/README.md)
<!-- learning-task:end -->
