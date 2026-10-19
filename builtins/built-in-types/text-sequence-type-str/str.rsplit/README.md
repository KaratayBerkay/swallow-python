## `str.rsplit`

```
str.rsplit(sep=None, maxsplit=-1)
```

Return a list of the words in the string, using *sep* as the delimiter string.
If *maxsplit* is given, at most *maxsplit* splits are done, the *rightmost*
ones.  If *sep* is not specified or `None`, any
[whitespace](../str.isspace/README.md) string is a
separator.  Except for splitting from the right, `rsplit()` behaves like
`split()` which is described in detail below.

## Çözümlü kısa örnek

Maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

```python
print(repr("a b".rsplit()))
# Sonuç: ['a', 'b']
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.38: str.rsplit davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

```python
"a b c".rsplit(None,1)
"a,,b".rsplit(",",1)
"".rsplit(",")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['a b', 'c']`; `['a,', 'b']`; `['']`.
- [ ] Maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.rstrip/README.md)
<!-- learning-task:end -->
