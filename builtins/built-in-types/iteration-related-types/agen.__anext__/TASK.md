# Görev b:2.6.8: agen.__anext__ durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

İki yield ile 4,6 veren async generatorın __anext__ awaitablelarını sırayla bekle. Sonraki çağrı için tükenmeyi göster. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

## Geçiş ölçütleri

- [ ] Awaitable oluşturmak ile beklemek ayrıdır; beklenen sonuçlar 4,6 ve StopAsyncIteration olur.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
