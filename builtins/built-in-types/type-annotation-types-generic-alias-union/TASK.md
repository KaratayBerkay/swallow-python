# Görev b:2.14: Tür açıklamasını çalışma zamanı doğrulamasından ayır

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`list[int](["x"])` oluştur; anotasyonun öğeyi zorla int yapıp yapmadığını göster. `int | str` için isinstance dene; `list[int]` için isinstance sınırını göster. Unionda yinelenen türlerin ve sıra değişiminin etkisini açıkla.

## Geçiş ölçütleri

- [ ] Listede "x" kalır; generic alias runtime öğe doğrulaması değildir.
- [ ] isinstance(3,int|str) True; isinstance([],list[int]) TypeError verir.
- [ ] Union sırası ve tekrarlar ayrı seçenek yaratmaz; anotasyon ile gerçek nesnenin türü ayrılmıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
