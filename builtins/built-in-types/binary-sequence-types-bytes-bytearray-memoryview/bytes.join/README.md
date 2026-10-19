## `bytes.join`

```
bytes.join(iterable, /)
bytearray.join(iterable, /)
```

Return a bytes or bytearray object which is the concatenation of the
binary data sequences in *iterable*.  A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) will be raised
if there are any values in *iterable* that are not `bytes-like
objects <bytes-like object>`, including [str](../../text-sequence-type-str/str/README.md) objects.  The
separator between elements is the contents of the bytes or
bytearray object providing this method.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; ayırıcı öğeler arasına girer; öğeler metin olmalıdır

```python
print(repr(b'-'.join([b'a',b'b'])))
# Sonuç: b'a-b'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.18: bytes.join davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; ayırıcı öğeler arasına girer; öğeler metin olmalıdır

```python
b'|'.join([])
b'|'.join([b'a'])
b'|'.join([b'a',2])
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b''`; `b'a'`; `TypeError`.
- [ ] ASCII bayt kurallarıyla çalış; ayırıcı öğeler arasına girer; öğeler metin olmalıdır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.maketrans/README.md)
<!-- learning-task:end -->
