## `float.fromhex`

```
float.fromhex(s)
```

Class method to return the float represented by a hexadecimal
string *s*.  The string *s* may have leading and trailing
whitespace.

## Çözümlü kısa örnek

p sonrası üs iki tabanındadır

```python
print(repr(float.fromhex("0x1.8p+1")))
# Sonuç: 3.0
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.11: float.fromhex davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; p sonrası üs iki tabanındadır

```python
float.fromhex("  -0x1p-1 ")
float.fromhex("gecersiz")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `-0.5`; `ValueError`.
- [ ] p sonrası üs iki tabanındadır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../complex.from_number/README.md)
<!-- learning-task:end -->
