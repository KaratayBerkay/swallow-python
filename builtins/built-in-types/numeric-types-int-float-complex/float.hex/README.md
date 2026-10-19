## `float.hex`

```
float.hex()
```

Return a representation of a floating-point number as a hexadecimal
string.  For finite floating-point numbers, this representation
will always include a leading `0x` and a trailing `p` and
exponent.

## Çözümlü kısa örnek

Hex gösterim saklanan değerin kayıpsız gösterimidir

```python
print(repr((1.5).hex()))
# Sonuç: '0x1.8000000000000p+0'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.10: float.hex davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; hex gösterim saklanan değerin kayıpsız gösterimidir

```python
(-2.25).hex()
float.fromhex((0.1).hex())==0.1
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'-0x1.2000000000000p+1'`; `True`.
- [ ] Hex gösterim saklanan değerin kayıpsız gösterimidir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../float.fromhex/README.md)
<!-- learning-task:end -->
