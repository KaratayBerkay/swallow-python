## `id()`

```
id(object, /)
```

Return the "identity" of an object.  This is an integer which
is guaranteed to be unique and constant for this object during its lifetime.
Two objects with non-overlapping lifetimes may have the same id()
value.

> **CPython implementation detail:** This is the address of the object in memory.

Raises an auditing event `builtins.id` with argument `id`.

## Çözümlü kısa örnek

Aynı nesneye ikinci ad verme ile eşit içerikli yeni nesneyi ayır.

```python
a=[1]; b=a; c=a[:]
print(repr(id(a)==id(b)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.35: id davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; aynı nesneye ikinci ad verme ile eşit içerikli yeni nesneyi ayır.

```python
a=[1]; b=a; c=a[:]
id(a)==id(c)
a==c
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Aynı nesneye ikinci ad verme ile eşit içerikli yeni nesneyi ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../input/README.md)
<!-- learning-task:end -->
