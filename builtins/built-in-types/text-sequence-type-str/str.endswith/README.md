## `str.endswith`

```
str.endswith(suffix[, start[, end]])
```

Return `True` if the string ends with the specified *suffix*, otherwise return
`False`.  *suffix* can also be a tuple of suffixes to look for.  With optional
*start*, test beginning at that position.  With optional *end*, stop comparing
at that position. Using *start* and *end* is equivalent to
`str[start:end].endswith(suffix)`. For example:

``` python
>>> 'Python'.endswith('on')
True
>>> 'a tuple of suffixes'.endswith(('at', 'in'))
False
>>> 'a tuple of suffixes'.endswith(('at', 'es'))
True
>>> 'Python is amazing'.endswith('is', 0, 9)
True
```
> Code: [example_01.py](example_01.py)

See also `startswith()` and `removesuffix()`.

## Çözümlü kısa örnek

Tuple seçenekleri ve dilim sınırları son ek denetimini belirler

```python
print(repr("a.py".endswith(".py")))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.9: str.endswith davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tuple seçenekleri ve dilim sınırları son ek denetimini belirler

```python
"a.txt".endswith((".py",".txt"))
"abXY".endswith("b",0,2)
"abc".endswith("z")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] Tuple seçenekleri ve dilim sınırları son ek denetimini belirler

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.expandtabs/README.md)
<!-- learning-task:end -->
