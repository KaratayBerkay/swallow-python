# Görev b:6.1: Maliyeti işlemden türet

## Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

n öğelik listeden pop(), pop(0), ortadan insert, k öğelik dilim, append ve sort maliyetlerini çıkar. N kez pop(0) ile listeyi boşaltmayı N kez pop() ile karşılaştır. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

## Geçiş ölçütleri

- [ ] Sondan pop amortized O(1), baştan pop O(n), dilim O(k), genel sort O(n log n).
- [ ] Baştan tekrarlı boşaltma O(N²), sondan O(N); append amortized maliyet ile tek resize maliyeti ayrılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
