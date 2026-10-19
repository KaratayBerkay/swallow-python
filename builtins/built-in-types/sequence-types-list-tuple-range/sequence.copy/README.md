## `sequence.copy`

```
sequence.copy()
```

> *Added in version 3.3.*

Create a shallow copy of *sequence*.
This is equivalent to writing `sequence[:]`.

> **Hint**
>
> The `copy()` method is not part of the
> [MutableSequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.MutableSequence) [ABC](https://docs.python.org/3.15/library/abc.html#abc.ABC),
> but most concrete mutable sequence types provide it.

## Çözümlü kısa örnek

Dış kopya yeni nesnedir; içteki nesne paylaşılır

```python
a=[[1]]
print(repr(a.copy()==a))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.20: sequence.copy davranışını ayırt et**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dış kopya yeni nesnedir; içteki nesne paylaşılır

```python
a=[[1]]
a.copy() is a
a.copy()[0] is a[0]
```

`bytearray([1,2])` için copy al; kopyayı değiştirince özgün verinin korunmasını ve dönüş türünü göster. İç içe liste örneğinde görülen iç paylaşımı bytearraya neden taşımadığını açıkla.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Dış kopya yeni nesnedir; içteki nesne paylaşılır

- [ ] Bytearray kopyası bağımsız bytearraydır; tamsayı öğelerin paylaşımı mutable iç liste paylaşımı değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.extend/README.md)
<!-- learning-task:end -->
