# Görev b:6.5: Maliyeti işlemden türet

## Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

N eşit uzunluklu parçayı döngüde + ile biriktirmeyi join ile tek sonuca çevirmeyle karşılaştır. Kısmi dilim, ileri/geri alt metin araması, encode/decode ve bytearray baştan del maliyetlerini dipnotlarıyla yaz. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

## Geçiş ölçütleri

- [ ] Tekrarlı değişmez birleştirme genel durumda O(N²) toplam kopyalamaya yol açar; join tek çıktı kurar.
- [ ] İleri arama O(n), geri arama en kötü O(n × aranan uzunluk); sınırlandırılmış aramada n aranan bölgedir.
- [ ] Bytearray baştan del amortized O(1); genel list baştan silme kuralı buna taşınmaz; codec varsayımı belirtilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
