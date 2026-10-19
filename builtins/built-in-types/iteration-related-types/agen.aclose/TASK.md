# Görev b:2.6.11: agen.aclose durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

Yield noktasındaki async generatora aclose uygulanıp bekleniyor. Normal kapanış, kapanış sırasında yield, farklı hata yayılması ve tekrar kapanışı ayrı durumlar olarak çöz. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

## Geçiş ölçütleri

- [ ] GeneratorExit aktarılır; normal kapanış None, yield RuntimeError, farklı hata dışarı yayılır; sonraki anext StopAsyncIteration verir.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
