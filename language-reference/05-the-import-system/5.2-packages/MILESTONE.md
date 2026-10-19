# Milestone: İki paket türünü aynı ağaçta çöz

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Regular başlangıç kodu ile namespace portion birleşiminin ayrımı.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir kökte `__init__` içeren app paketi, app altında `__init__` içermeyen plugins dizini; iki ayrı arama kökünde __init__siz extras paketinin farklı alt modülleri olsun.

2. Her import için paket türünü, çalışacak başlangıç dosyalarını ve kaynakların neden tek fiziksel kök zorunluluğu taşımadığını çiz.

3. Çizime yeni bir portion eklendiğinde arama yolunun hangi olayda güncelleneceğini ekle.

## Geçiş ölçütleri

- [ ] app regular; app.plugins namespace alt paket olarak doğru.
- [ ] extras portionları tek namespace altında birleşiyor.
- [ ] Namespace için sahte `__init__` yürütmesi varsayılmamış.
- [ ] Yol değişimini yeniden arama ilişkisiyle açıklayabiliyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
