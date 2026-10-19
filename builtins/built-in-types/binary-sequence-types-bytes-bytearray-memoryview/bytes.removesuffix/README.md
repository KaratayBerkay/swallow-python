## `bytes.removesuffix`

```
bytes.removesuffix(suffix, /)
bytearray.removesuffix(suffix, /)
```

If the binary data ends with the *suffix* string and that *suffix* is
not empty, return `bytes[:-len(suffix)]`.  Otherwise, return a copy of
the original binary data:

``` python
>>> b'MiscTests'.removesuffix(b'Tests')
b'Misc'
>>> b'TmpDirMixin'.removesuffix(b'Tests')
b'TmpDirMixin'
```
> Code: [example_01.py](example_01.py)

The *suffix* may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

> *Added in version 3.9.*

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; tam son ek yalnız bir kez kaldırılır; boş ek metni silmez

```python
print(repr(b'ad.txt'.removesuffix(b'.txt')))
# Sonuç: b'ad'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.8: bytes.removesuffix davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tam son ek yalnız bir kez kaldırılır; boş ek metni silmez

```python
b'ababa'.removesuffix(b'ba')
b'abc'.removesuffix(b'')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'aba'`; `b'abc'`.
- [ ] ASCII bayt kurallarıyla çalış; tam son ek yalnız bir kez kaldırılır; boş ek metni silmez
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.decode/README.md)
<!-- learning-task:end -->
