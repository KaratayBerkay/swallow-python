## `bytes.lower`

```
bytes.lower()
bytearray.lower()
```

Return a copy of the sequence with all the uppercase ASCII characters
converted to their corresponding lowercase counterpart.

For example:

``` python
>>> b'Hello World'.lower()
b'hello world'
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

Yalnız ASCII harfler küçülür; kaynak bytearray yerinde değişmez.

```python
print(repr(b"ADA".lower()))
# Sonuç: b'ada'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.72: bytes.lower davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız ASCII harfler küçülür; kaynak bytearray yerinde değişmez.

```python
b"A\xff1!".lower()
bytearray(b"ADA").lower()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'a\xff1!'`; `bytearray(b'ada')`.
- [ ] Yalnız ASCII harfler küçülür; kaynak bytearray yerinde değişmez.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.splitlines/README.md)
<!-- learning-task:end -->
