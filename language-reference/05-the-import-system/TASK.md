# Görev 5: Modülü bulmayla ad bağlamayı ayır

**Odak:** import arama/oluşturma ve yerel ad bağlama, doğrudan `__import__` çağrısının farkı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.4.2](../../tutorial/06-modules/6.4-packages/6.4.2-intra-package-references/README.md).

## Tek görev

1. Ayrı yeni oturumlarda üç ifade için olay tablosu yaz: import math; `__import__`("math"); m = `__import__`("math").

2. Her satırda modülün bulunması/oluşması ve yerel kapsamda math veya m adının bağlanması olaylarını ayır. dir() ile bağlanan adları kontrol et.

3. Var olmayan benzersiz bir modül adı için hata türünü de belirt.

## Geçiş ölçütleri

- [ ] import math yerel math adını bağlıyor.
- [ ] Doğrudan `__import__` modülü döndürüyor, yerel math adı oluşturması beklenmiyor.
- [ ] Atama üçüncü durumda m adını bağlıyor.
- [ ] Bulunamayan modül ModuleNotFoundError; arama yan etkileri ile yerel ad bağlama ayrılmış.
- [ ] importlib gibi başka giriş yollarının `__import__` mekanizmasını atlayabileceği kaynak sınırlarıyla açıklanmış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
