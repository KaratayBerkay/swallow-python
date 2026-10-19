# Görev b:2.17: Dönüşüm sınırını işlem türüne göre ayır

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Sınırın 640 olarak ayarlandığı verilmiş bir ortamda 641 decimal basamak içeren int(metin), 641 hex basamak içeren int(metin,16), büyük int için str/hex ve int.from_bytes işlemlerini sınıflandır. Varsayılan sınırla minimum yapılandırılabilir eşiği karıştırma; sınırı kaldırmadan hata yolunu açıkla.

## Geçiş ölçütleri

- [ ] Decimal int/str dönüşümü sınırı aşarsa ValueError; iki kuvveti tabanlar, hex ve from_bytes bu decimal sınıra tabi değildir.
- [ ] Varsayılan 4300 ile minimum eşik 640 ayrılmıştır; sıfır ayarı sınırı kapatır, rastgele düşük pozitif ayar geçerli değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
