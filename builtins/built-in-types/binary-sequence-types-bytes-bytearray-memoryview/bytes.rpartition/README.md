## `bytes.rpartition`

```
bytes.rpartition(sep, /)
bytearray.rpartition(sep, /)
```

Split the sequence at the last occurrence of *sep*, and return a 3-tuple
containing the part before the separator, the separator itself or its
bytearray copy, and the part after the separator.
If the separator is not found, return a 3-tuple
containing two empty bytes or bytearray objects, followed by a copy of the
original sequence.

The separator to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

```python
print(repr(b'a=b'.rpartition(b'=')))
# Sonuç: (b'a', b'=', b'b')
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.30: bytes.rpartition davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

```python
b'a=b=c'.rpartition(b'=')
b'abc'.rpartition(b'=')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(b'a=b', b'=', b'c')`; `(b'', b'', b'abc')`.
- [ ] ASCII bayt kurallarıyla çalış; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.startswith/README.md)
<!-- learning-task:end -->
