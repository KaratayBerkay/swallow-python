## `len()`

```
len(object, /)
```

Return the length (the number of items) of an object.  The argument may be a
sequence (such as a string, bytes, tuple, list, or range) or a collection
(such as a dictionary, set, or frozen set).

> **CPython implementation detail:** `len` raises [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) on lengths larger than
> [sys.maxsize](https://docs.python.org/3.15/library/sys.html#sys.maxsize), such as [range(2 ** 100)](../range/README.md).

## Çözümlü kısa örnek

Uzunluk kavramını her nesneye ve bayt sayısına genelleme.

```python
print(repr(len([1,2])))
# Sonuç: 2
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.41: len davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; uzunluk kavramını her nesneye ve bayt sayısına genelleme.

```python
len("İ")
len("İ".encode("utf-8"))
len(7)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `2`; `TypeError`.
- [ ] Uzunluk kavramını her nesneye ve bayt sayısına genelleme.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../locals/README.md)
<!-- learning-task:end -->
