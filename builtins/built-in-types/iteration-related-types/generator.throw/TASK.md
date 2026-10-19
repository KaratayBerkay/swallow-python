# Görev b:2.6.6: generator.throw durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Hazır bir generatorın yield noktasında durduğu biliniyor. Gövdedeki try/except ValueError bu hatayı yakalayıp 8 yield ediyor. throw(ValueError("x")) sonucunu, yakalanmayan TypeError ile karşılaştır. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

## Geçiş ölçütleri

- [ ] Yakalanan hata generator içinde işlenir, 8 döner; yakalanmayan TypeError dışarı yayılır ve generator kapanır.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
