# Görev b:2.6.9: agen.asend durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

Async generator `x = yield 4` satırında duruyor; sonraki ifade `yield x+1`. asend(7) awaitableı beklendiğinde ne olur? Başlatılmamış örnekte asend(7) ile karşılaştır. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

## Geçiş ölçütleri

- [ ] Durmuş örnek x=7 ile 8 üretir; yeni generator non-None ile başlatılamaz.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
