# Görev b:2.6.10: agen.athrow durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

Async generator yield noktasında duruyor. ValueError yakalayıp 8 yield eden gövde için athrow(ValueError("x")) awaitableını izle. Yakalanmayan hata ve yieldsiz normal bitişi de karşılaştır. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

## Geçiş ölçütleri

- [ ] Yakalanıp yield edilirse 8, yakalanmazsa o hata, yieldsiz bitişte StopAsyncIteration yayılır.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
