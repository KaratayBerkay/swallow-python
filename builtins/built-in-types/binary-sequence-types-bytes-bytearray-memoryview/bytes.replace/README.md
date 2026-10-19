## `bytes.replace`

```
bytes.replace(old, new, /, count=-1)
bytearray.replace(old, new, /, count=-1)
```

Return a copy of the sequence with all occurrences of subsequence *old*
replaced by *new*.  If *count* is given, only the first *count* occurrences
are replaced.  If *count* is not specified or `-1`, then all occurrences
are replaced.

The subsequence to search for and its replacement may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

> *Changed in version 3.15:* *count* is now supported as a keyword argument.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; count sınırı ve özgün metnin korunmasını açıkla

```python
print(repr(b'aba'.replace(b'a',b'x')))
# Sonuç: b'xbx'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.24: bytes.replace davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; count sınırı ve özgün metnin korunmasını açıkla

```python
b'aaaa'.replace(b'aa',b'x',1)
b'abc'.replace(b'z',b'x')
b'abc'.replace(b'a',b'x',0)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'xaa'`; `b'abc'`; `b'abc'`.
- [ ] ASCII bayt kurallarıyla çalış; count sınırı ve özgün metnin korunmasını açıkla
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.rfind/README.md)
<!-- learning-task:end -->
