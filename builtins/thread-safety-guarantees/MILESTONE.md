# Milestone: Paylaşılan veriye yönelik iddiayı denetle

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../TASKS.md) kontrol et.

## Tek görev

Bir list, dict ve bytearray görünümü paylaşan iki iş parçacığı için tasarım incelemesi yaz. Her biri için bir güvenli tek işlem, iki adımdan oluşan bir yarış ve varsayımı bozan argüman türünü göster. Memoryview readonly seçeneğiyle veri yarışının çözülmediğini kanıtla; gerekli dış eşgüdümün kapsamını akış üzerinde işaretle.

## Geçiş ölçütleri

- [ ] Atomik işlem ile algoritma garantisi ayrıdır; deterministik olay sırası karşı örnek üretir.
- [ ] Aynı tamponu paylaşma, özel iterable ve kullanıcı karşılaştırma kodu sınırları gözden kaçmaz; olasılıksal thread testi geçiş koşulu değildir.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)
