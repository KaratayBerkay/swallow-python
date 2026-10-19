# Görev 6.3: Adları doğru kapsamda ara

**Odak:** dir(modül), dir() ve dir(builtins) farkı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.2](../6.2-standard-modules/README.md).

## Tek görev

1. Yeni REPL içinde local_marker = 7 tanımla; counts modülünü ve builtins modülünü import et. local_marker, counts, count_items ve len adlarının hangilerini dir(), dir(counts), dir(builtins) içinde bulduğunu listele. from counts import count_items sonrasında dir() sonucunun nasıl değiştiğini göster.

## Geçiş ölçütleri

- [ ] local_marker ve counts yerel ad listesinde; count_items counts modülünün listesinde.
- [ ] from sonrasında count_items yerel ad listesine de ekleniyor.
- [ ] len yerelde tanımlanmadan builtins içinde bulunuyor.
- [ ] dir çıktısındaki bütün sürüme bağlı adların birebir eşit olması beklenmemiş; dir sıralı metin listesi olarak açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
