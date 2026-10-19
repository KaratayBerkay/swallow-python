# Görev b:3.2: aiter sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

Verilen async iterable için `__aiter__()` çağrısının `it` nesnesini döndürdüğü biliniyor. `aiter(kaynak)` çağrısını ve `aiter(kaynak, "SON")` denemesini yazılı olarak izle. Sonucu, çağrılan metodu ve normal `iter` ile imza farkını göster.

## Geçiş ölçütleri

- [ ] İlk çağrı async iterator `it` nesnesini döndürür; öğe tüketmez.
- [ ] İkinci çağrı TypeError olur; iki argümanlı sentinel biçimi yoktur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
