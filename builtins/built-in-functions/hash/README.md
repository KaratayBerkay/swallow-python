## `hash()`

```
hash(object, /)
```

Return the hash value of the object (if it has one).  Hash values are
integers.  They are used to quickly compare dictionary keys during a
dictionary lookup.  Numeric values that compare equal have the same hash
value (even if they are of different types, as is the case for 1 and 1.0).

> **Note**
>
> For objects with custom [__hash__()](https://docs.python.org/3.15/reference/datamodel.html#object.__hash__) methods,
> note that hash()
> truncates the return value based on the bit width of the host machine.

## Çözümlü kısa örnek

Eşit hash değerinin tek başına nesnelerin eşitliğini kanıtlamadığını açıkla; tam sayıyı ezberleme.

```python
print(repr(hash(3)==hash(3.0)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.32: hash davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; eşit hash değerinin tek başına nesnelerin eşitliğini kanıtlamadığını açıkla; tam sayıyı ezberleme.

```python
hash((1,2))==hash((1,2))
hash([1,2])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `TypeError`.
- [ ] Eşit hash değerinin tek başına nesnelerin eşitliğini kanıtlamadığını açıkla; tam sayıyı ezberleme.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../help/README.md)
<!-- learning-task:end -->
