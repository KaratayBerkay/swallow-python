## `bytes.zfill`

```
bytes.zfill(width, /)
bytearray.zfill(width, /)
```

Return a copy of the sequence left filled with ASCII `b'0'` digits to
make a sequence of length *width*. A leading sign prefix (`b'+'`/
`b'-'`) is handled by inserting the padding *after* the sign character
rather than before. For [bytes](../bytes/README.md) objects, the original sequence is
returned if *width* is less than or equal to `len(seq)`.

For example:

``` python
>>> b"42".zfill(5)
b'00042'
>>> b"-42".zfill(5)
b'-0042'
```
> Code: [example_01.py](example_01.py)

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; sıfırlar işaretten sonra eklenir; kısa genişlik kesmez

```python
print(repr(b'42'.zfill(4)))
# Sonuç: b'0042'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.82: bytes.zfill davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sıfırlar işaretten sonra eklenir; kısa genişlik kesmez

```python
b'-7'.zfill(4)
b'+7'.zfill(4)
b'123'.zfill(2)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'-007'`; `b'+007'`; `b'123'`.
- [ ] ASCII bayt kurallarıyla çalış; sıfırlar işaretten sonra eklenir; kısa genişlik kesmez
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
