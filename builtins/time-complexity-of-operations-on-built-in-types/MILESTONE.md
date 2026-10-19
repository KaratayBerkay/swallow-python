# Milestone: Veri yapısını iş yüküne göre seç

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../TASKS.md) kontrol et.

## Tek görev

Bir iş yükünde N kaydı tekrarlı list üyeliğiyle denetleme ve pop(0) ile işleme var. Aynı sonuçları set/dict üyeliği ve sondan pop veya sıralı iterasyonla üret. Maliyeti önce/sonra çıkar; işlem sırası gerekiyorsa onu koru. Binary bölümde kopya dilim yerine memoryview seçiminin maliyet ve paylaşım farkını ekle.

## Geçiş ölçütleri

- [ ] Genel kuadratik tarama/kaydırma nedenleri gösterilir; hash varsayımlarıyla yeni maliyet gerekçelendirilir.
- [ ] Sıra veya yinelenen kayıt semantiği optimizasyon uğruna değiştirilmez; kopyadan vazgeçmenin paylaşım etkisi açıklanır.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)
