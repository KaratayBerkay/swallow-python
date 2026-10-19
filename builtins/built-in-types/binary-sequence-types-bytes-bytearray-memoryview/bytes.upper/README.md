## `bytes.upper`

```
bytes.upper()
bytearray.upper()
```

Return a copy of the sequence with all the lowercase ASCII characters
converted to their corresponding uppercase counterpart.

For example:

``` python
>>> b'Hello World'.upper()
b'HELLO WORLD'
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

Yalnız ASCII harfler büyür; bytearray sürümü de yeni nesne üretir.

```python
print(repr(b"ada".upper()))
# Sonuç: b'ADA'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.80: bytes.upper davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız ASCII harfler büyür; bytearray sürümü de yeni nesne üretir.

```python
b"a\xff1!".upper()
bytearray(b"ada").upper()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'A\xff1!'`; `bytearray(b'ADA')`.
- [ ] Yalnız ASCII harfler büyür; bytearray sürümü de yeni nesne üretir.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.zfill/README.md)
<!-- learning-task:end -->
