# Görev 9.9: Durumu yield aralarında koru

**Odak:** Generator fonksiyonu, ertelenen yürütme, yield ile durma/devam ve otomatik tükenme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.8](../9.8-iterators/README.md).

## Tek görev

1. 0 ile limit arasındaki sayıları veren generator yaz.

2. Gövde başına "started", her yield sonrasına "resumed" mesajı koy. limit=2 için generator oluştur, bir next yap, ikinci next yap, üçüncü next dene.

3. Mesajların hangi olayda basıldığını önce tahmin et.

4. Boş sınır için yeni generator oluşturup listele.

## Geçiş ölçütleri

- [ ] Nesne oluşturmak started basmıyor; ilk next gövdeyi başlatıyor.
- [ ] İlk değer 0; ikinci 1; sonraki next son resumed ardından StopIteration.
- [ ] Yerel değişken ve yürütme konumu çağrılar arasında korunuyor.
- [ ] Boş generator [] üretiyor; `__iter__`/`__next__` elle yazılmamış.
- [ ] yield ile return farkı durma/devam edebilme üzerinden açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
