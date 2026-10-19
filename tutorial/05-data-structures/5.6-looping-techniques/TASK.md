# Görev 5.6: Aynı veriden farklı dolaşım görünümleri üret

**Odak:** items, enumerate, zip, reversed, sorted/set ve kaynak üzerinde değişiklik yapmadan filtreleme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.5](../5.5-dictionaries/README.md).

## Tek görev

1. names = ["Ece", "Ada", "Ada"], scores = [8, 5, 9] ve rooms = {"Ada": "A1", "Ece": "B2"} ile küçük rapor oluştur. enumerate ile sıra numarası/ad, zip ile ad/puan, items ile ad/oda satırlarını bas.

2. Adları tersten ve tekrarsız sıralı biçimde ayrıca göster.

3. README içindeki NaN filtreleme iskeletini [2.0, float("NaN"), 4.0] için kullan; kaynak listenin korunmasını kontrol et.

## Geçiş ölçütleri

- [ ] enumerate indeksleri 0, 1, 2; zip çiftleri Ece-8, Ada-5, Ada-9.
- [ ] items her anahtarı kendi değeriyle eşleştiriyor.
- [ ] Tersten görünüm Ada, Ada, Ece; tekrarsız sıralı görünüm Ada, Ece. Kaynak liste Ece, Ada, Ada olarak korunmuş.
- [ ] Filtre [2.0, 4.0] oluşturuyor; asıl veri değiştirilmemiş.
- [ ] Dolaşma araçlarının her birinin hangi eşleştirme ihtiyacını karşıladığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
