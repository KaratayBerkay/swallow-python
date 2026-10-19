# Görev b:4.1: Hata zincirini üç biçimde karşılaştır

## Önce

[b:4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

KeyError yakalandığında ValueError üreten üç küçük fonksiyon yaz: yalın raise, `from asil`, `from None`. Dışarıda hataları yakalayıp context/cause/suppress_context alanlarını göster; tracebackte hangi zincirin görünür olduğunu açıkla.

## Geçiş ölçütleri

- [ ] Yalın raise context tutar; açık from cause ve suppress_context=True ayarlar.
- [ ] From None görüntüde eski hatayı gizler ama __context__ içinden silmez.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
