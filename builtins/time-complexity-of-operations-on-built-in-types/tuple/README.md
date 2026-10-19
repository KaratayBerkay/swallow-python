A [tuple](../../built-in-types/sequence-types-list-tuple-range/tuple/README.md) is an [immutable](https://docs.python.org/3.15/glossary.html#term-immutable) sequence. Because a tuple can never
change, there are no insertion or deletion costs, and making a copy simply
returns the same object, so is constant time (*O*(1)).

| Operation | Complexity |
| --- | --- |
| Copy (`tuple(t)`) | *O*(1) |
| Get item (`t[k]`) | *O*(1) |
| Get slice (`t[i:j]`) | *O*(*j* - *i*) |
| Concatenate (`t1 + t2`) | *O*(len(*t1*) + len(*t2*)) |
| Multiply (`t * k`) | *O*(*nk*) |
| Iteration | *O*(*n*) |
| `x in t` | *O*(*n*) |
| `min(t)`, `max(t)` | *O*(*n*) |
| Get length (`len(t)`) [^1] | *O*(1) |

[^1]: The number of elements is stored in the object, so `len()` does not need to count them.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:6.2: Maliyeti işlemden türet**

### Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

Tuple kopyalama, k öğelik kısmi dilim, iki tuple birleştirme, üyelik ve len maliyetlerini çıkar; değişmezliğin hangi işlemi gerçekten ucuzlattığını belirt. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

### Geçiş ölçütleri

- [ ] Tuple(t) O(1), kısmi dilim O(k), birleştirme O(n+m), üyelik O(n), len O(1).
- [ ] Değişmez olmak bütün işlemleri sabit maliyet yapmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../dict-frozendict/README.md)
<!-- learning-task:end -->
