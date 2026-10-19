## `float.is_integer`

```
float.is_integer()
```

Return `True` if the float instance is finite with integral
value, and `False` otherwise:

``` python
>>> (-2.0).is_integer()
True
>>> (3.2).is_integer()
False
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Sonlu tam değer ile tamsayı türünü ayır

```python
print(repr((2.0).is_integer()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.9: float.is_integer davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sonlu tam değer ile tamsayı türünü ayır

```python
(2.5).is_integer()
float("inf").is_integer()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `False`.
- [ ] Sonlu tam değer ile tamsayı türünü ayır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../float.hex/README.md)
<!-- learning-task:end -->
