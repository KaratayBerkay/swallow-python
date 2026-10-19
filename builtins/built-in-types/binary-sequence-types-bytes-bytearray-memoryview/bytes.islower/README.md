## `bytes.islower`

```
bytes.islower()
bytearray.islower()
```

Return `True` if there is at least one lowercase ASCII character
in the sequence and no uppercase ASCII characters, `False` otherwise.

For example:

``` python
>>> b'hello world'.islower()
True
>>> b'Hello world'.islower()
False
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

## Çözümlü kısa örnek

Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.

```python
print(repr(b'ada'.islower()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.64: bytes.islower davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII koşulunu ve boş girdi sonucunu açıkla.

```python
b'ada 12!'.islower()
b'Ada'.islower()
b'123'.islower()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.isspace/README.md)
<!-- learning-task:end -->
