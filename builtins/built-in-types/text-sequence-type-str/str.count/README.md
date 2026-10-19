## `str.count`

```
str.count(sub[, start[, end]])
```

Return the number of non-overlapping occurrences of substring *sub* in the
range [*start*, *end*].  Optional arguments *start* and *end* are
interpreted as in slice notation.

If *sub* is empty, returns the number of empty strings between characters
which is the length of the string plus one. For example:

``` python
>>> 'spam, spam, spam'.count('spam')
3
>>> 'spam, spam, spam'.count('spam', 5)
2
>>> 'spam, spam, spam'.count('spam', 5, 10)
1
>>> 'spam, spam, spam'.count('eggs')
0
>>> 'spam, spam, spam'.count('')
17
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla

```python
print(repr("aba".count("a")))
# Sonuç: 2
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.7: str.count davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla

```python
"aaaa".count("aa")
"abc".count("")
"ababa".count("a",1,4)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `4`; `1`.
- [ ] Örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.encode/README.md)
<!-- learning-task:end -->
