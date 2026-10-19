# Görev b:2.13.2: Bastırma kararını görünür kıl

## Önce

[b:2.13](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aynı ValueError üreten gövdeyi __exit__ True ve False döndüren iki yönetici ile dene. Normal gövdede True dönüşüyle karşılaştır. Hata sınıfı, değeri ve traceback argümanlarını kaydet.

## Geçiş ölçütleri

- [ ] True gövde hatasını bastırır, False yayılmasını sürdürür.
- [ ] Normal bitişte (None,None,None) verilir; dönüşün doğruluğu normal akışı değiştirmez.
- [ ] Exit gövdedeki hatayı elle yeniden raise etmek zorunda değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
