# Time complexity of operations on built-in types

This page documents the time complexity of various operations on built-in types
in CPython. Other Python implementations may have different performance
characteristics. Additionally, the listed costs assume exact built-in types, as
instances of subclasses may have different costs.

We use [Big *O* notation](https://en.wikipedia.org/wiki/Big_O_notation) to describe how the running time of an operation grows
with the size of its inputs. Unless stated otherwise, *n* denotes the number of
elements currently in the container, and *k* is the value of a numeric
parameter, such as an index or a repeat count.


<!-- learning-task:start -->
## Bölüm görevi

**Görev b:6: Büyüme oranını girdiye bağla**

### Önce

[t:4.8](../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

Aynı türde iki işlem için maliyetlerin O(1) ve O(n) olduğu verilmiş. n 100den 1000e çıktığında iş miktarının nasıl değişmesini beklediğini açıkla. Ölçülen milisaniyeyi bu sınıflarla neden eşitleyemeyeceğini, exact built-in ve CPython koşuluyla belirt.

### Geçiş ölçütleri

- [ ] O(1) n ile büyümez; O(n) büyümesi yaklaşık 10 kat iş miktarı ölçeğindedir, kesin süre garantisi değildir.
- [ ] Alt sınıf, implementasyon ve çağrılan kullanıcı kodu maliyeti varsayımları korunmuştur.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](list/README.md)
<!-- learning-task:end -->
## Contents

- [list](list/README.md) — Lists are mutable sequences; for more detail on the implementation see How are lists implemented in CPython?.
- [tuple](tuple/README.md) — A tuple is an immutable sequence.
- [dict, frozendict](dict-frozendict/README.md) — The times listed for dict objects are average-case times, as they assume the hash function for the objects is sufficiently robust to make…
- [set, frozenset](set-frozenset/README.md) — See dict as the set and frozenset implementations are similar, and the same caveats apply.
- [str, bytes, bytearray](str-bytes-bytearray/README.md) — str and bytes objects are immutable sequences of characters and bytes, respectively.
- [memoryview](memoryview/README.md) — memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying.
- [range](range/README.md) — A range object computes its items on demand from its *start*, *stop* and *step* values, so most operations do not depend on the length of the range.
- [Notes](notes/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Veri yapısını iş yüküne göre seç**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../TASKS.md) kontrol et.

### Tek görev

Bir iş yükünde N kaydı tekrarlı list üyeliğiyle denetleme ve pop(0) ile işleme var. Aynı sonuçları set/dict üyeliği ve sondan pop veya sıralı iterasyonla üret. Maliyeti önce/sonra çıkar; işlem sırası gerekiyorsa onu koru. Binary bölümde kopya dilim yerine memoryview seçiminin maliyet ve paylaşım farkını ekle.

### Geçiş ölçütleri

- [ ] Genel kuadratik tarama/kaydırma nedenleri gösterilir; hash varsayımlarıyla yeni maliyet gerekçelendirilir.
- [ ] Sıra veya yinelenen kayıt semantiği optimizasyon uğruna değiştirilmez; kopyadan vazgeçmenin paylaşım etkisi açıklanır.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-milestone:end -->
