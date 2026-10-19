# Milestone: Canlı ayarla dondurulmuş ayarı ayır

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

Sürüm farkında yalnız yeni özelliği gerekçeli yazılı iz ile inceleyebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

Dict ile varsayılan ayarlara kullanıcı ayarlarını sağ taraf önceliğiyle uygula. Python 3.15 frozendict ile dış eşlemeyi dondur; iç listeyi değiştirmenin etkisini, yeni eşleme üretimini ve hashability koşulunu göster. Eski snapshotın hangi düzeyde bağımsız olduğunu açıkla.

## Geçiş ölçütleri

- [ ] Çakışma önceliği ve ekleme sırası korunur; eski dış eşleme yeni anahtar almaz.
- [ ] Frozendict derin dondurma değildir; hash için değerlerin de hashable olması gerekir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
