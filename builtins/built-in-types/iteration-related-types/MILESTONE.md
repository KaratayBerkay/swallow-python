# Milestone: Tüketim protokolünü birleştir

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

## Tek görev

Bir generator önce hazır bilgisini yield etsin, send ile aldığı sayıyı yield etsin, sonra return 9 yapsın. Oluşturma, ilk next, send, son next ve close durumlarını kaydet. Aynı işlemin async karşılıklarını, hazır verilen asend/anext sözleşmeleriyle yazılı eşleştir.

## Geçiş ölçütleri

- [ ] Gönderilen değer yield ifadesine bağlanır; StopIteration.value=9 okunur.
- [ ] Iterator yeniden başlamaz; async awaitable oluşturma ve çalıştırma anları ayrılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
