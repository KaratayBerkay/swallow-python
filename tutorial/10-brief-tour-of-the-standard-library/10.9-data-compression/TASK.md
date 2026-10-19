# Görev 10.9: Sıkıştırılmış verinin geri dönebildiğini kanıtla

**Odak:** zlib compress/decompress, bytes uzunluğu ve crc32.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.8](../10.8-dates-and-times/README.md).

## Tek görev

1. payload = b"study " * 100 için compress ve decompress uygula.

2. Başlangıç/son uzunluklarını ve sıkıştırılmış verinin uzunluğunu göster; geri açılan içeriği aslıyla karşılaştır. crc32 değerini asıl ve geri açılmış veri için al.

3. Aynı deneyi b"x" için yapıp sıkıştırmanın her zaman kısaltma garantisi olup olmadığını değerlendir.

## Geçiş ölçütleri

- [ ] Her iki payload geri açılınca aslına eşit.
- [ ] Uzun veri için sıkıştırma etkisi gözlenmiş; kısa veri için büyüme başarısızlık sayılmamış.
- [ ] crc32 eşleşmesi içerik eşitliği denetiminin yerine tek kanıt olarak kullanılmamış.
- [ ] compress/decompress yönleri ve bytes gereksinimi açıklanmış; kesin sıkıştırılmış bayt dizisi ezberlenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
