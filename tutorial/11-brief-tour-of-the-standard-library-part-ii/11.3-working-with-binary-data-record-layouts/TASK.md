# Görev 11.3: Binary kayıttaki sınırları hesapla

**Odak:** struct alan boyutu/sırası, little-endian ve dilim üzerinden kayıt okuma.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.2](../11.2-templating/README.md).
- Ön bilgi: [t:7.2.1](../../07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md).

## Tek görev

1. Bölümdeki <IIIHH düzeninde struct.unpack sonucunun (1, 4, 9, 3, 2) olduğunu kabul ederek bir kayıt okuma izi çıkar.

2. Bu tuple içindeki değerleri crc32, comp_size, uncomp_size, filenamesize, extra_size alanlarına eşleştir.

3. Alan bloğu başlangıcını 14 kabul ederek örnekteki start akışında alan bloğu, dosya adı, ek alan ve sonraki kayda ilerleme sınırlarını hesapla.

4. Gerçek ZIP dosyası veya bölümde örneklenmeyen pack çağrısı yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] Alan bloğu 16 bayt; üç I dörder, iki H ikişer bayt.
- [ ] Geri açılan beş değer verilen sırada ve aynı.
- [ ] Alan bloğu [14:30], ad [30:33], ek alan [33:35], veri 4 bayt sonrası sonraki başlangıç 39.
- [ ] < little-endian; kayıt sınırları dosyanın rastgele yerinden tahmin edilmemiş.
- [ ] Gerçek ZIP yapısını sıfırdan bilmek veya zipfile API ayrıntıları gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
