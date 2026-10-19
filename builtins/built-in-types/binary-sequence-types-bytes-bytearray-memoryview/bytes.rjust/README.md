## `bytes.rjust`

```
bytes.rjust(width, fillbyte=b' ', /)
bytearray.rjust(width, fillbyte=b' ', /)
```

Return a copy of the object right justified in a sequence of length *width*.
Padding is done using the specified *fillbyte* (default is an ASCII
space). For [bytes](../bytes/README.md) objects, the original sequence is returned if
*width* is less than or equal to `len(s)`.

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; dolgu sola eklenir; kısa genişlik kesme yapmaz

```python
print(repr(b'ab'.rjust(4,b'.')))
# Sonuç: b'..ab'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.42: bytes.rjust davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; dolgu sola eklenir; kısa genişlik kesme yapmaz

```python
b'ab'.rjust(1,b'.')
b'ab'.rjust(4,b'..')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'ab'`; `TypeError`.
- [ ] ASCII bayt kurallarıyla çalış; dolgu sola eklenir; kısa genişlik kesme yapmaz
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.rsplit/README.md)
<!-- learning-task:end -->
