## `bytes.removeprefix`

```
bytes.removeprefix(prefix, /)
bytearray.removeprefix(prefix, /)
```

If the binary data starts with the *prefix* string, return
`bytes[len(prefix):]`. Otherwise, return a copy of the original
binary data:

``` python
>>> b'TestHook'.removeprefix(b'Test')
b'Hook'
>>> b'BaseTestCase'.removeprefix(b'Test')
b'BaseTestCase'
```
> Code: [example_01.py](example_01.py)

The *prefix* may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

> *Added in version 3.9.*

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

```python
print(repr(b'pre-ad'.removeprefix(b'pre-')))
# Sonuç: b'ad'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.6: bytes.removeprefix davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

```python
b'ababa'.removeprefix(b'ab')
b'baX'.removeprefix(b'ab')
b'abc'.removeprefix(b'')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'aba'`; `b'baX'`; `b'abc'`.
- [ ] ASCII bayt kurallarıyla çalış; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.removesuffix/README.md)
<!-- learning-task:end -->
