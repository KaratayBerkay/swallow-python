# Görev b:2.11.24: symmetric_difference_update ile üyeliği güncelle

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`s={1,2}; diger=s` ile başla. İlk `s.symmetric_difference_update({2,3})` çağrısının dönüşünü ve iki adın üyelerini kaydet. Ardından aynı s üzerinde `s.symmetric_difference_update([1,3])` çağır; sonucu veya hata türünü göster.

## Geçiş ölçütleri

- [ ] İlk üyeler `{1,3}`, ilk dönüş None; küme sırasına dayalı beklenti yok.
- [ ] Tek taraftaki öğeler kalır; ikinci aynı girdi bunları kaldırır.
- [ ] Diger aynı kümenin güncel üyelerini görür.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
