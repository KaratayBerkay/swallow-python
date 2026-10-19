## `str.index`

```
str.index(sub[, start[, end]])
```

Like [find()](../str.find/README.md), but raise [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the substring is
not found. For example:

``` python
>>> 'spam, spam, spam'.index('spam')
0
>>> 'spam, spam, spam'.index('eggs')
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    'spam, spam, spam'.index('eggs')
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: substring not found
```
> Code: [example_01.py](example_01.py)

See also `rindex()`.

## Çözümlü kısa örnek

Arama başarısızlığı ValueError verir; -1 ile karıştırma

```python
print(repr("ababa".index("ba")))
# Sonuç: 1
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.13: str.index davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; arama başarısızlığı ValueError verir; -1 ile karıştırma

```python
"ababa".index("ba",2)
"ababa".index("x")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `3`; `ValueError`.
- [ ] Arama başarısızlığı ValueError verir; -1 ile karıştırma

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isalnum/README.md)
<!-- learning-task:end -->
