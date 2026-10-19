## `bytes.istitle`

```
bytes.istitle()
bytearray.istitle()
```

Return `True` if the sequence is ASCII titlecase and the sequence is not
empty, `False` otherwise. See [bytes.title()](../bytes.title/README.md) for more details on the
definition of "titlecase".

For example:

``` python
>>> b'Hello World'.istitle()
True
>>> b'Hello world'.istitle()
False
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.

```python
print(repr(b'Ada Ece'.istitle()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.68: bytes.istitle davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII koşulunu ve boş girdi sonucunu açıkla.

```python
b'Ada 2Ece'.istitle()
b'ADA'.istitle()
b''.istitle()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Sınıflandırma ASCII baytlara uygulanır; UTF-8 ile kodlanmış Unicode harf veya boşluk otomatik ASCII sınıfına girmez.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.isupper/README.md)
<!-- learning-task:end -->
