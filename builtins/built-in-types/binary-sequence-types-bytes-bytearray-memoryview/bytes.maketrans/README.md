## `bytes.maketrans`

```
bytes.maketrans(from, to, /)
bytearray.maketrans(from, to, /)
```

This static method returns a translation table usable for
[bytes.translate()](../bytes.translate/README.md) that will map each character in *from* into the
character at the same position in *to*; *from* and *to* must both be
[bytes-like objects](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) and have the same length.

> *Added in version 3.1.*

## Çözümlü kısa örnek

Binary tablo 256 bayttır; iki taraf eşit uzunlukta olmalıdır

```python
print(repr(len(bytes.maketrans(b"a",b"x"))))
# Sonuç: 256
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.20: bytes.maketrans davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; binary tablo 256 bayttır; iki taraf eşit uzunlukta olmalıdır

```python
bytes.maketrans(b"a",b"x")[97]
bytes.maketrans(b"ab",b"x")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `120`; `ValueError`.
- [ ] Binary tablo 256 bayttır; iki taraf eşit uzunlukta olmalıdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.partition/README.md)
<!-- learning-task:end -->
