## `reversed()`

```
reversed(object, /)
```

Return a reverse [iterator](https://docs.python.org/3.15/glossary.html#term-iterator).  The argument must be an object which has
a [__reversed__()](https://docs.python.org/3.15/reference/datamodel.html#object.__reversed__) method or supports the sequence protocol (the
[__len__()](https://docs.python.org/3.15/reference/datamodel.html#object.__len__) method and the [__getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getitem__) method
with integer arguments starting at `0`).

## Çözümlü kısa örnek

Ters iterator oluşturmak kaynağı yerinde ters çevirmez.

```python
print(repr(list(reversed([1,2]))))
# Sonuç: [2, 1]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.58: reversed davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ters iterator oluşturmak kaynağı yerinde ters çevirmez.

```python
list(reversed([2,5,1]))
list(reversed([]))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[1, 5, 2]`; `[]`.
- [ ] Ters iterator oluşturmak kaynağı yerinde ters çevirmez.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../round/README.md)
<!-- learning-task:end -->
