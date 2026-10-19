## `bytes.isspace`

```
bytes.isspace()
bytearray.isspace()
```

Return `True` if all bytes in the sequence are ASCII whitespace and the
sequence is not empty, `False` otherwise.  ASCII whitespace characters are
those byte values in the sequence `b' \t\n\r\x0b\f'` (space, tab, newline,
carriage return, vertical tab, form feed).

## Çözümlü kısa örnek

Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.

```python
print(repr(b' '.isspace()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.66: bytes.isspace davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII koşulunu ve boş girdi sonucunu açıkla.

```python
b'\t\n'.isspace()
b'\xe3\x80\x80'.isspace()
b''.isspace()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.istitle/README.md)
<!-- learning-task:end -->
