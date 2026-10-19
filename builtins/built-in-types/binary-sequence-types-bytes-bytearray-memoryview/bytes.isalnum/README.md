## `bytes.isalnum`

```
bytes.isalnum()
bytearray.isalnum()
```

Return `True` if all bytes in the sequence are alphabetical ASCII characters
or ASCII decimal digits and the sequence is not empty, `False` otherwise.
Alphabetic ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`. ASCII decimal
digits are those byte values in the sequence `b'0123456789'`.

For example:

``` python
>>> b'ABCabc1'.isalnum()
True
>>> b'ABC abc1'.isalnum()
False
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.

```python
print(repr(b'a1'.isalnum()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.56: bytes.isalnum davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII koşulunu ve boş girdi sonucunu açıkla.

```python
b'\xc4\xb02'.isalnum()
b'a b'.isalnum()
b''.isalnum()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `False`; `False`.
- [ ] Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.isalpha/README.md)
<!-- learning-task:end -->
