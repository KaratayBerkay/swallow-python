# Görev 9.3.2: Sınıftan başlangıç durumu olan nesne üret

**Odak:** Sınıf nitelikleri, `__doc__`, sınıf çağrısı ve `__init__` argümanları.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.1](../9.3.1-class-definition-syntax/README.md).

## Tek görev

1. Bir Point sınıfına kısa docstring, category = "point" sınıf niteliği ve `__init__`(self, x, y) ekle; self.x/self.y atamalarını yap.

2. Point(2, 5) oluşturup koordinatları, Point.category ve `Point.__doc__` değerlerini göster.

3. İkinci bir nesneyi farklı koordinatlarla oluştur; `__init__` ne zaman ve hangi nesne için çalışıyor açıkla.

## Geçiş ölçütleri

- [ ] İki nesnenin başlangıç koordinatları kendilerine verilen değerler.
- [ ] Sınıfa çağrı yeni örnek oluşturuyor; örnek `__init__` içine ilk argüman olarak geliyor.
- [ ] Sınıf niteliği ve docstring sınıftan erişiliyor.
- [ ] `__init__` çağrının dönüş nesnesi yerine yalnız başlatıcı olarak açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
