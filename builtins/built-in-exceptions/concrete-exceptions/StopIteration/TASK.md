# Görev b:4.4.21: Dönüş değerini tükenme hatasından oku

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Bir generator önce yield 4 sonra return 9 yapsın; sonraki next çağrısında yakalanan StopIteration.value değerini bul. Ayrı generator içinde açıkça raise StopIteration(9) yapmayı karşılaştır.

## Geçiş ölçütleri

- [ ] Return durumunda value=9 olan StopIteration tüketiciye ulaşır.
- [ ] Generator içinde açık StopIteration, cause alanında asıl hata korunarak RuntimeError durumuna dönüşür.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
