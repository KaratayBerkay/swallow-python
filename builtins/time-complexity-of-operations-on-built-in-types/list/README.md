Lists are mutable sequences; for more detail on the implementation see
[How are lists implemented in CPython?](https://docs.python.org/3.15/faq/design.html#how-are-lists-implemented). The largest costs come from growing beyond the
current allocation size (because everything must move), or from inserting or
deleting somewhere near the beginning (because everything after that must move).
If you need to add or remove at both ends, consider using a
[collections.deque](https://docs.python.org/3.15/library/collections.html#collections.deque) instead.

| Operation | Complexity |
| --- | --- |
| Copy (`l.copy()`) | *O*(*n*) |
| Append (`l.append(x)`) [^1] | *O*(1) |
| Pop (`l.pop(k)`) [^1] [^2] | *O*(*n* - *k*) |
| Insert (`l.insert(k, x)`) [^1] [^2] | *O*(*n* - *k*) |
| Get item (`l[k]`) | *O*(1) |
| Set item (`l[k] = x`) | *O*(1) |
| Delete item (`del l[k]`) [^2] | *O*(*n* - *k*) |
| Iteration | *O*(*n*) |
| Get slice (`l[i:j]`) | *O*(*j* - *i*) |
| Set slice (`l[i:j] = t`) [^1] | *O*(*j* - *i*) if len(*t*) == *j* - *i*, otherwise *O*(*n* - *i* + len(*t*)) |
| Delete slice (`del l[i:j]`) | *O*(*n* - *i*) |
| Extend (`l.extend(t)`) [^1] [^3] | *O*(len(*t*)) |
| Sort (`l.sort()`) [^4] | *O*(*n* log *n*) |
| Concatenate (`l1 + l2`) | *O*(len(*l1*) + len(*l2*)) |
| Multiply (`l * k`) | *O*(*nk*) |
| `x in l` | *O*(*n*) |
| `min(l)`, `max(l)` | *O*(*n*) |
| Get length (`len(l)`) [^5] | *O*(1) |

[^1]: Amortized. An individual operation may occasionally be *O*(*n*) when the underlying storage is resized, but this cost is spread over many operations, depending on the history of the container.
[^2]: Popping or deleting the element at index *k* of a list of size *n* shifts all elements after *k* one slot to the left, moving *n* - *k* - 1 elements; inserting at index *k* shifts the elements from *k* onwards one slot to the right, moving *n* - *k* elements. The worst case is index 0, where the whole rest of the list has to be moved; the average case, an index in the middle of the list, takes *O*(*n*/2) = *O*(*n*) operations; and operating at the end of the list moves nothing and is *O*(1).
[^3]: Plus the cost of iterating over *t*, which may be expensive for an arbitrary iterable.
[^4]: This is the worst case scenario. Sorting is adaptive and input that is already sorted or reverse-sorted takes only *O*(*n*) comparisons. See [Objects/listsort.txt](https://github.com/python/cpython/tree/3.15/Objects/listsort.txt) for more information.
[^5]: The number of elements is stored in the object, so `len()` does not need to count them.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:6.1: Maliyeti işlemden türet**

### Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

n öğelik listeden pop(), pop(0), ortadan insert, k öğelik dilim, append ve sort maliyetlerini çıkar. N kez pop(0) ile listeyi boşaltmayı N kez pop() ile karşılaştır. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

### Geçiş ölçütleri

- [ ] Sondan pop amortized O(1), baştan pop O(n), dilim O(k), genel sort O(n log n).
- [ ] Baştan tekrarlı boşaltma O(N²), sondan O(N); append amortized maliyet ile tek resize maliyeti ayrılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../tuple/README.md)
<!-- learning-task:end -->
