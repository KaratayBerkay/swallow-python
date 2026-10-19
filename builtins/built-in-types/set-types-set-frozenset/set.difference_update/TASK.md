# Görev b:2.11.23: difference_update ile üyeliği güncelle

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`s={1,2}; diger=s` ile başla. İlk `s.difference_update({2,3})` çağrısının dönüşünü ve iki adın üyelerini kaydet. Ardından aynı s üzerinde `s.difference_update([1])` çağır; sonucu veya hata türünü göster.

## Geçiş ölçütleri

- [ ] İlk üyeler `{1}`, ilk dönüş None; küme sırasına dayalı beklenti yok.
- [ ] Fark yerinde uygulanır; yöntem iterable kabul eder.
- [ ] Diger aynı kümenin güncel üyelerini görür.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
