# Görev b:3.61: setattr sözleşmesini uygula

## Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Boş `class K: pass` örneğine `setattr(o,"puan",4)` uygula. Aynı niteliği 9 yap ve hem `o.puan` hem `getattr(o,"puan")` ile doğrula. Sınıf nesnesine atamayla örneğe atamanın nerede depolandığını ayır.

## Geçiş ölçütleri

- [ ] İlk sonuç 4, güncel sonuç 9 olur; ad string olarak verilmiştir.
- [ ] Örnekteki atama örneğin, sınıftaki atama sınıfın namespace alanını değiştirir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
