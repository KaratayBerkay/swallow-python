## `abs()`

```
abs(number, /)
```

Return the absolute value of a number.  The argument may be an
integer, a floating-point number, or an object implementing
[__abs__()](https://docs.python.org/3.15/reference/datamodel.html#object.__abs__).
If the argument is a complex number, its magnitude is returned.

## Çözümlü kısa örnek

İşaretin kaldırılmasıyla complex büyüklüğünü ayır.

```python
print(repr(abs(-4)))
# Sonuç: 4
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.1: abs davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; i̇şaretin kaldırılmasıyla complex büyüklüğünü ayır.

```python
abs(-7.5)
abs(3+4j)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `7.5`; `5.0`.
- [ ] İşaretin kaldırılmasıyla complex büyüklüğünü ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../aiter/README.md)
<!-- learning-task:end -->
