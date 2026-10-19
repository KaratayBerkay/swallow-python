# Görev b:3.68: super sözleşmesini uygula

## Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`A -> object`, `B -> A`, `C -> A`, `D -> B, C` sınıflarını kur. Her sınıfın aynı adlı yöntemi kendi harfini kaydetsin ve A dışındakiler `super()` ile devam etsin. D örneğinde çağrı sırasını kanıtla.

## Geçiş ölçütleri

- [ ] Sıra D, B, C, A olur; B içindeki super doğrudan A demek değildir.
- [ ] Arama D örneğinin MRO sırasına göre çağrının tanımlandığı sınıftan sonra sürer.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
