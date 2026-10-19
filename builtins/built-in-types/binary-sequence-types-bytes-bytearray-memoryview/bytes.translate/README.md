## `bytes.translate`

```
bytes.translate(table, /, delete=b'')
bytearray.translate(table, /, delete=b'')
```

Return a copy of the bytes or bytearray object where all bytes occurring in
the optional argument *delete* are removed, and the remaining bytes have
been mapped through the given translation table, which must be a bytes
object of length 256.

You can use the [bytes.maketrans()](../bytes.maketrans/README.md) method to create a translation
table.

Set the *table* argument to `None` for translations that only delete
characters:

``` python
>>> b'read this short text'.translate(None, b'aeiou')
b'rd ths shrt txt'
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.6:* *delete* is now supported as a keyword argument.

## Çözümlü kısa örnek

Binary tablo baytı bayta eşler; delete önce siler

```python
print(repr(b"ab".translate(None,b"a")))
# Sonuç: b'b'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.34: bytes.translate davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; binary tablo baytı bayta eşler; delete önce siler

```python
b"abca".translate(bytes.maketrans(b"a",b"x"),delete=b"b")
b"a".translate(b"x")
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'xcx'`; `ValueError`.
- [ ] Binary tablo baytı bayta eşler; delete önce siler
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.center/README.md)
<!-- learning-task:end -->
