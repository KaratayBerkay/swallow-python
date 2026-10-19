# Görev b:2.11.22: intersection_update ile üyeliği güncelle

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`s={1,2}; diger=s` ile başla. İlk `s.intersection_update({2,3})` çağrısının dönüşünü ve iki adın üyelerini kaydet. Ardından aynı s üzerinde `s.intersection_update([2])` çağır; sonucu veya hata türünü göster.

## Geçiş ölçütleri

- [ ] İlk üyeler `{2}`, ilk dönüş None; küme sırasına dayalı beklenti yok.
- [ ] Yalnız ortak öğeler yerinde korunur.
- [ ] Diger aynı kümenin güncel üyelerini görür.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
