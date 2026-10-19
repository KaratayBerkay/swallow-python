# Görev b:2.4.12: complex.from_number sınırını göster

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

`complex.from_number(7)`, `complex.from_number("7")` çağrılarını ve __complex__, __float__, __index__ metotlarının hepsi verilmiş nesnedeki önceliği çıkar.

## Geçiş ölçütleri

- [ ] (7+0j), TypeError; öncelik __complex__, sonra __float__, sonra __index__ olur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
