# Görev b:4.4.30: Geçersiz veri aralığını ayır

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`b"A\xffB".decode("utf-8")` ve `"AİB".encode("ascii")` hatalarını ayrı yakala. Encoding, object, start, end, reason alanlarını ve `e.object[e.start:e.end]` dilimini göster.

## Geçiş ölçütleri

- [ ] İlk hata UnicodeDecodeError ve sorunlu dilim b"\xff"; ikinci UnicodeEncodeError ve sorunlu dilim "İ".
- [ ] Start dahil, end hariçtir; encoding ve reason tanı koymak için korunur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
