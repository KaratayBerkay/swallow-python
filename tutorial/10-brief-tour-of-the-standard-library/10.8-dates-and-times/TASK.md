# Görev 10.8: Tarih farkını sabit girdilerle doğrula

**Odak:** date oluşturma, today, strftime ve çıkarma sonucunun days niteliği.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.7](../10.7-internet-access/README.md).

## Tek görev

1. dt.date ile 2024-02-28 ve 2024-03-01 tarihlerini oluştur; farkın days değerini bul.

2. Son tarihi "%m-%d-%y" ve "%d %b %Y" biçimlerinde göster. today() çağrısını ayrı yapıp neden bugünün tarihine sabit bir beklenen değer yazılamayacağını açıkla.

## Geçiş ölçütleri

- [ ] Fark 2 gün; artık gün tarih aritmetiğiyle hesaba katılmış.
- [ ] Sayısal görünüm 03-01-24; ikinci görünüm aynı tarihi ifade ediyor.
- [ ] %b yerel ayara göre farklı metin üretebilir; sistem locale ayarı değiştirilmemiş.
- [ ] Çıkarma sonucu ile biçimlenen str birbirinden ayrılmış; timezone API tasarımı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
