A [range](../../built-in-types/sequence-types-list-tuple-range/range/README.md) object computes its items on demand from its *start*, *stop* and
*step* values, so most operations do not depend on the length of the range.

| Operation | Complexity |
| --- | --- |
| Get item (`r[k]`) | *O*(1) |
| Get slice (`r[i:j]`) | *O*(1) |
| `x in r` [^1] | *O*(1) |
| Index and count (`r.index(x)`, `r.count(x)`) [^1] | *O*(1) |
| Iteration | *O*(*n*) |
| `min(r)`, `max(r)` | *O*(*n*) |
| Get length (`len(r)`) [^2] | *O*(1) |

[^1]: Assuming [int](https://docs.python.org/3.15/builtins/functions.html#int) or [bool](https://docs.python.org/3.15/builtins/functions.html#bool) arguments. For other types, the range is searched like any other sequence in *O*(*n*) time.
[^2]: The number of elements is stored in the object, so `len()` does not need to count them.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:6.7: Maliyeti işlemden türet**

### Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

Çok uzun range üzerinde indeks, dilim, int üyelik, float üyelik, iterasyon ve min maliyetlerini sınıflandır. Range nesnesi sabit alan tutarken tam gezinmenin neden ucuzlamadığını açıkla. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

### Geçiş ölçütleri

- [ ] İndeks/dilim/int veya bool üyelik O(1); diğer türlerde üyelik O(n) olabilir; iterasyon/min O(n).
- [ ] Girdinin türü ve gerçekten kaç öğeye bakıldığı varsayımları açıkça korunur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../notes/README.md)
<!-- learning-task:end -->
