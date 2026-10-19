## `bytes.isdigit`

```
bytes.isdigit()
bytearray.isdigit()
```

Return `True` if all bytes in the sequence are ASCII decimal digits
and the sequence is not empty, `False` otherwise. ASCII decimal digits are
those byte values in the sequence `b'0123456789'`.

For example:

``` python
>>> b'1234'.isdigit()
True
>>> b'1.23'.isdigit()
False
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; üst simge rakam kabul edilir; kesir her zaman digit değildir

```python
print(repr(b'12'.isdigit()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.62: bytes.isdigit davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; üst simge rakam kabul edilir; kesir her zaman digit değildir

```python
b'\xc2\xb2'.isdigit()
b'\xe2\x85\x95'.isdigit()
b''.isdigit()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `False`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; üst simge rakam kabul edilir; kesir her zaman digit değildir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.islower/README.md)
<!-- learning-task:end -->
