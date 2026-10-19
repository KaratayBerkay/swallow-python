## `bytes.rsplit`

```
bytes.rsplit(sep=None, maxsplit=-1)
bytearray.rsplit(sep=None, maxsplit=-1)
```

Split the binary sequence into subsequences of the same type, using *sep*
as the delimiter string. If *maxsplit* is given, at most *maxsplit* splits
are done, the *rightmost* ones.  If *sep* is not specified or `None`,
any subsequence consisting solely of
[ASCII whitespace](../bytes.isspace/README.md) is a separator.
Except for splitting from the right, `rsplit()` behaves like
`split()` which is described in detail below.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

```python
print(repr(b'a b'.rsplit()))
# Sonuç: [b'a', b'b']
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.44: bytes.rsplit davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

```python
b'a b c'.rsplit(None,1)
b'a,,b'.rsplit(b',',1)
b''.rsplit(b',')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[b'a b', b'c']`; `[b'a,', b'b']`; `[b'']`.
- [ ] ASCII bayt kurallarıyla çalış; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.rstrip/README.md)
<!-- learning-task:end -->
