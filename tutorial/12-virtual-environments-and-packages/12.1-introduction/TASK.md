# Görev 12.1: Çakışan bağımlılığı iki ortamda ayır

**Odak:** Sürüm çatışması ve sanal ortamın uygulama başına izolasyonu.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.12](../../10-brief-tour-of-the-standard-library/10.12-batteries-included/README.md).

## Tek görev

1. Kod veya kurulum yapmadan şu durumun ortam çizimini hazırla: A uygulaması lib 1.0, B uygulaması lib 2.0 istiyor; sonra B 3.0 istiyor.

2. Önce tek ortamda çatışmayı, sonra iki ayrı ortamda paket yerleşimini göster.

3. Python yorumlayıcı sürümü ile paketin sürümünü çizimde ayrı etiketle.

## Geçiş ölçütleri

- [ ] A ve B için ayrı bağımlılık alanları var; B yükselmesi A ortamını değiştirmiyor.
- [ ] Tek ortamın aynı ihtiyaçları neden karşılayamayacağı belirtilmiş.
- [ ] Sanal ortam paket sürümü ile Python sürümü karıştırılmamış; henüz öğretilmeyen komutlar gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
