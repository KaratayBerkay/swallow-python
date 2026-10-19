# Görev 4.9.3.2: Konumsal parametrenin adını serbest bırak

**Odak:** / öncesi parametrelerin yalnız konumla verilmesi; sonrasındakilerin ayrılması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.1](../4.9.3.1-positional-or-keyword-arguments/README.md).

## Tek görev

1. def pair(first, /, second) gövdesinden [first, second] döndür. pair(3, 5), pair(3, second=5), pair(first=3, second=5) çağrılarını ayrı ayrı dene. first adını item olarak değiştirip geçerli çağrıların hangilerinin korunacağını açıkla.

## Geçiş ölçütleri

- [ ] İlk iki çağrı [3, 5] döndürüyor; üçüncüsü başarısız.
- [ ] / yalnızca solundaki parametreyi sınırlıyor.
- [ ] Konumsal çağrılar parametre adı değişince korunuyor; sıra değişirse anlamın değişeceği açıklanmış.

[Değerlendirme yöntemi](../../../../../DEGERLENDIRME.md) · [Sıra](../../../../../TASKS.md)
