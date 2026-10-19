## `bytes.swapcase`

```
bytes.swapcase()
bytearray.swapcase()
```

Return a copy of the sequence with all the lowercase ASCII characters
converted to their corresponding uppercase counterpart and vice-versa.

For example:

``` python
>>> b'Hello World'.swapcase()
b'hELLO wORLD'
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Unlike [str.swapcase()](../../text-sequence-type-str/str.swapcase/README.md), it is always the case that
`bin.swapcase().swapcase() == bin` for the binary versions. Case
conversions are symmetrical in ASCII, even though that is not generally
true for arbitrary Unicode code points.

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII case dönüşümü dışındaki baytlar korunur ve çift swapcase özgün veriyi verir.

```python
print(repr(b"aB".swapcase()))
# Sonuç: b'Ab'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.76: bytes.swapcase davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII case dönüşümü dışındaki baytlar korunur ve çift swapcase özgün veriyi verir.

```python
b"aB\xff".swapcase()
b"aB\xff".swapcase().swapcase()==b"aB\xff"
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'Ab\xff'`; `True`.
- [ ] ASCII case dönüşümü dışındaki baytlar korunur ve çift swapcase özgün veriyi verir.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.title/README.md)
<!-- learning-task:end -->
