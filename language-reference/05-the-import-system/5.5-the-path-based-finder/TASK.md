# Görev 5.5: İki finder türünü farklı katmanlara yerleştir

**Odak:** PathFinder meta path içinde; path entry finder tek bir yol türünü işler.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.6](../5.4-loading/5.4.6-cached-bytecode-invalidation/README.md).

## Tek görev

1. Bir import akışını iki katmanlı çiz: sys.meta_path içindeki PathFinder, altındaki dizin/zip girdileri ve her girdiyi bilen path entry finder.

2. PathFinder listeden kaldırılmış olsaydı path entry hooklarının neden bu yoldan çalışmayacağını açıkla.

3. URL veya veritabanı yolunun kavramsal yerini göster; bu kaynaklar için bağlantı kodu yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] PathFinder bütün yol girdilerini doğrudan yükleyen loader olarak çizilmemiş.
- [ ] Meta path finder ile path entry finder farklı katmanlarda.
- [ ] PathFinder devreden çıkınca onun alt protokolü de bu arama yolu üzerinden çağrılmıyor.
- [ ] Dizin/zip ve özel konumlar metin girdisi olabiliyor; paylaşımlı kütüphanelerin zip sınırı kaynak notuyla ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
