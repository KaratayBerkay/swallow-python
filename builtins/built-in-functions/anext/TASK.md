# Görev b:3.4: anext sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

Bir async iterator ilk beklemede 7, ikincide 9 veriyor, sonra StopAsyncIteration bildiriyor. Üç `await anext(it)` çağrısını izle. Yeni bir iterator için üçüncü çağrıyı `await anext(it, "SON")` yap ve sonucu karşılaştır.

## Geçiş ölçütleri

- [ ] Sıra 7, 9, StopAsyncIteration; default verilirse son sonuç "SON".
- [ ] Çağrı awaitable üretir; öğe veya tükenme, bu awaitable beklendiğinde ortaya çıkar.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
