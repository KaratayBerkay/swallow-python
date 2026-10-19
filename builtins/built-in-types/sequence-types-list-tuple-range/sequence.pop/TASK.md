# Görev b:2.7.29: pop etkisini izle

## Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`s=[1,2]; diger=s` ile başla. `sonuc=s.pop(0)` uygula. s, diger, sonuc ve `s is diger` değerlerini göster. Boş listede pop çağrısını ayrıca dene.

Aynı kontrolü yeni bir `ba=bytearray([1,2])` üzerinde `ba.pop(0)` çağrısıyla tekrarla; dönüşü ve kalan baytları göster.

## Geçiş ölçütleri

- [ ] İlk listede son durum `[2]`; iki ad aynı nesneyi gösterir.
- [ ] İlk dönüş 1; boş listede IndexError.
- [ ] Pop indeksteki öğeyi döndürür ve kaldırır.

- [ ] Ortak yöntem bytearrayda da doğru dönüş ve son durumla kanıtlanmış; öğeler 0..255 sınırında tutulmuştur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
