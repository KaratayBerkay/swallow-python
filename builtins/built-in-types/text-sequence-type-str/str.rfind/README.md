## `str.rfind`

```
str.rfind(sub[, start[, end]])
```

Return the highest index in the string where substring *sub* is found, such
that *sub* is contained within `s[start:end]`.  Optional arguments *start*
and *end* are interpreted as in slice notation.  Return `-1` on failure.
For example:

``` python
>>> 'spam, spam, spam'.rfind('sp')
12
>>> 'spam, spam, spam'.rfind('sp', 0, 10)
6
```
> Code: [example_01.py](example_01.py)

See also `find()` and `rindex()`.

## Çözümlü kısa örnek

Sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1

```python
print(repr("ababa".rfind("ba")))
# Sonuç: 3
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.34: str.rfind davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1

```python
"ababa".rfind("ba",0,4)
"abc".rfind("x")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `-1`.
- [ ] Sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.rindex/README.md)
<!-- learning-task:end -->
