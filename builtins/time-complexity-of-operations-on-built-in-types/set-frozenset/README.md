See [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md) as the [set](../../built-in-types/set-types-set-frozenset/set/README.md) and [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md) implementations are
similar, and the same caveats apply.
In the worst case, *O*(1) operations instead take *O*(*n*) time,
and operations that look up every element degrade accordingly.

A [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md) is [immutable](https://docs.python.org/3.15/glossary.html#term-immutable), so it does not support adding,
discarding, or the in-place update operations. The others below apply to it at
the same costs.

| Operation | Complexity |
| --- | --- |
| `x in s` | *O*(1) |
| Copy (`s.copy()`) [^1] [^2] | *O*(*n*) |
| Add (`s.add(x)`) [^3] | *O*(1) |
| Discard (`s.discard(x)`, `s.remove(x)`) | *O*(1) |
| Union (`s1 \| s2`, `s1.union(s2)`) [^2] | *O*(len(*s1*) + len(*s2*)) |
| Update (`s1 \|= s2`, `s1.update(s2)`) [^3] [^2] | *O*(len(*s2*)) |
| Intersection (`s1 & s2`, `s1.intersection(s2)`) [^2] [^4] | *O*(min(len(*s1*), len(*s2*))) |
| Intersection update (`s1 &= s2`, `s1.intersection_update(s2)`) [^3] [^2] [^4] | *O*(min(len(*s1*), len(*s2*))) |
| Difference (`s1 - s2`, `s1.difference(s2)`) [^2] [^5] | *O*(len(*s1*)) |
| Difference update (`s1 -= s2`, `s1.difference_update(s2)`) [^3] [^2] [^4] | *O*(min(len(*s1*), len(*s2*))) |
| Symmetric difference (`s1 ^ s2`, `s1.symmetric_difference(s2)`) [^2] | *O*(len(*s1*) + len(*s2*)) |
| Symmetric difference update (`s1 ^= s2`, `s1.symmetric_difference_update(s2)`) [^3] [^2] | *O*(len(*s2*)) |
| Get length (`len(s)`) [^6] | *O*(1) |

[^1]: Copying a [frozendict](../../built-in-types/mapping-types-dict-frozendict/frozendict/README.md) or a [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md) is *O*(1) as it returns the original object.
[^2]: These operations scan the container's internal hash table, which is not shrunk when elements are removed. After removing most elements, they still take time proportional to the container's former size, until a later insertion triggers a resize.
[^3]: Amortized. An individual operation may occasionally be *O*(*n*) when the underlying storage is resized, but this cost is spread over many operations, depending on the history of the container.
[^4]: *O*(len(*t*)) if *t* is not a set.
[^5]: *O*(len(*s*) + len(*t*)) if *t* is not a set.
[^6]: The number of elements is stored in the object, so `len()` does not need to count them.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:6.4: Maliyeti işlemden türet**

### Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

n ve m üyeli iki kümede union, intersection, difference, difference_update maliyetlerini karşılaştır. Diğer operand set yerine genel iterable olursa dipnotların etkisini ekle; frozenset kopyasını ayrı göster. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

### Geçiş ölçütleri

- [ ] Union O(n+m), intersection O(min(n,m)), difference O(n), difference_update O(min(n,m)) olağan varsayımlarla verilir.
- [ ] Genel iterable ve hash çakışması koşulları sonucu değiştirir; frozenset copy O(1), mutable set copy O(n).

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str-bytes-bytearray/README.md)
<!-- learning-task:end -->
