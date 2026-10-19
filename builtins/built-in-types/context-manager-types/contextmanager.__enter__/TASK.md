# Görev b:2.13.1: Giriş değerini yöneticiden ayır

## Önce

[b:2.13](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

__enter__ metodu self yerine "hazir" döndüren context manager yaz. With as değişkeni ve yönetici nesnenin farklı olduğunu göster. __enter__ hata verirse gövde ve __exit__ çalışır mı, akış üzerinden açıkla.

## Geçiş ölçütleri

- [ ] As değişkeni "hazir" olur; yönetici __exit__ çağrısı için ayrıca tutulur.
- [ ] Enter tamamlanmazsa gövdeye girilmez ve bu yöneticinin exit metodu çağrılmaz.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
