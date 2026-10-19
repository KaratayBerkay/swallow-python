# Görev b:2.7.32: remove etkisini izle

## Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`s=[1,2]; diger=s` ile başla. `sonuc=s.remove(1)` uygula. s, diger, sonuc ve `s is diger` değerlerini göster. Aynı işlemi yeni bir `[1,2,1]` listesinde tekrarla; değişen öğeleri işaretle.

Aynı kontrolü yeni bir `ba=bytearray([1,2])` üzerinde `ba.remove(1)` çağrısıyla tekrarla; dönüşü ve kalan baytları göster.

## Geçiş ölçütleri

- [ ] İlk listede son durum `[2]`; iki ad aynı nesneyi gösterir.
- [ ] Dönüş None; Remove indeks değil değer arar; ilk eşleşmeyi kaldırır.
- [ ] Remove indeks değil değer arar; ilk eşleşmeyi kaldırır.

- [ ] Ortak yöntem bytearrayda da doğru dönüş ve son durumla kanıtlanmış; öğeler 0..255 sınırında tutulmuştur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
