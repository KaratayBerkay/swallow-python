# Görev b:6.6: Maliyeti işlemden türet

## Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

N baytlık kaynaktan memoryview oluşturma, k baytlık alt görünüm, onu bytesa çevirme, count ve index maliyetlerini ayır. Kopyalama ile görünüm üretiminin nerede olduğunu göster. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

## Geçiş ölçütleri

- [ ] Oluşturma ve dilim O(1); k öğelik dönüşüm O(k); taramalar aranan öğe sayısıyla doğrusal.
- [ ] Sabit maliyet alt görünüm veriyi kopyalamaz; sayma/indeks elemanları tek tek karşılaştırır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
