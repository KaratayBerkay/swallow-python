# Milestone: Binary paketi kopya ve görünümle işle

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

## Tek görev

`bytearray(b"ID=7;OK")` verisinde ayırıcıyı bul, memoryview ile payloadın alt görünümünü al ve aynı uzunlukta değiştir. Str çıktısını decode ile üret; bağımsız bytes snapshotını ve readonly görünümü tut. Sonraki kaynak değişiminde hangisinin değiştiğini kanıtla; bütün görünümleri release ettikten sonra boyut değiştir.

## Geçiş ölçütleri

- [ ] Snapshot değişmez, görünümler aynı tamponu izler; ASCII bayt ile Unicode çözümlemesi ayrılır.
- [ ] Görünüm üzerinden boyut değiştirilemez; canlı export varken bytearray resize engeli hesaba katılmıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
