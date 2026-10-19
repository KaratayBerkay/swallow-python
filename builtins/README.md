# Built-in çalışma rotası

Bu rota tutorialdaki temel Python bilgilerini ve mevcut import bölümlerini tamamladıktan sonra gelir. Yerleşik araçların sözleşmelerini, sınırlarını ve birlikte doğru kullanılmasını çalıştırır.

Her adımda açıklama ve örneği incele, aynı sayfadaki bölüm görevini çöz, geçiş ölçütlerini kanıtla. Sonraki adım bağlantısını izle. Klasör sonundaki milestone bütün alt kontrollerden sonra yapılır. İlerlemeyi [görev sırasından](../TASKS.md) işaretle; [değerlendirme yöntemi](../DEGERLENDIRME.md) bütün kontrollerde geçerlidir.

Bir API yalnız başka sayfaya yönlendiriyorsa yeni görev yoktur: sayfa ortak davranışın asıl görevine bağlanır. List/bytearray veya set/frozenset aynı sözleşmeyi paylaştığında tür farkları o ortak görevde sınanır.

Python sürümünü görevde kontrol et. 3.12-3.15 özellikleri eski yorumlayıcıda açıkça izin verilen yazılı durum iziyle incelenebilir; bu, ilgili sürümde çalıştırma kanıtı sayılmaz. Async görevlerinde yalnız verilen protokol durumunu izlemek yeterlidir; event loop veya yeni framework kurulumu beklenmez. Thread safety görevleri GIL kapalı free-threaded bağlamı için yazılı olay sıraları kullanır.

## Contents

- [1. Sabitler](built-in-constants/README.md)
- [2. Türler ve yöntemleri](built-in-types/README.md)
- [3. Yerleşik fonksiyonlar](built-in-functions/README.md)
- [4. Hatalar ve uyarılar](built-in-exceptions/README.md)
- [5. Thread safety garantileri](thread-safety-guarantees/README.md)
- [6. İşlem maliyetleri](time-complexity-of-operations-on-built-in-types/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Built-in kararlarını tek kanıtla birleştir**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../TASKS.md) kontrol et.

### Tek görev

Türler milestoneundaki kayıt işleyiciyi yeniden kullan. Fonksiyonlar milestoneundaki boş girdi/iterator/strict testlerini, exception milestoneundaki dar handler ve cause bilgisini bu çözüme uygula. Son iki milestoneun concurrency ve maliyet incelemesini bu programın gerçekten kullandığı nesneler üzerinde yap. Yeni bir ikinci proje yazma.

### Geçiş ölçütleri

- [ ] Tek çalışma doğru veri türleriyle işler; boş/yanlış/Unicode/yinelenen girdiler için sonuç ve hata kanıtı vardır.
- [ ] Her seçimin nedenini, mutable paylaşımını ve maliyet varsayımını açıklarsın; hiçbir iddia yalnız çıktı ezberine dayanmaz.

[Değerlendirme yöntemi](../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

Bu öğrenme rotasındaki son kontrol.
<!-- learning-milestone:end -->
