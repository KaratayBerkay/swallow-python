# Görev 4.9.3.4: Karma imzayla ad çakışmasını çöz

**Odak:** Üç parametre türünün birlikte kullanımı ve konumsal adın `**kwds` içindeki anahtarla çakışması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.3](../4.9.3.3-keyword-only-arguments/README.md).
- Ön bilgi: [t:4.9.2](../../4.9.2-keyword-arguments/README.md).

## Tek görev

1. def inspect(name, /, value, *, active, `**kwds`) gövdesinden [name, value, active, kwds] döndür. inspect("outer", 2, active=True, name="inner") çağrısını çalıştır.

2. Aynı imzadan / işaretini kaldırınca aynı çağrının neden başarısız olduğunu göster.

3. Son olarak bir geçerli karma çağrı ve her parametre türü için bir geçersiz çağrı hazırla.

## Geçiş ölçütleri

- [ ] İlk çağrıda name outer; kwds içinde name anahtarı inner değerinde.
- [ ] / kaldırıldığında aynı name parametresine iki değer bağlanmaya çalışılıyor.
- [ ] Üç farklı parametre kısıtı ayrı ayrı gösterilmiş; `**kwds` parametreye bağlanmış değerleri tekrar toplamıyor.

[Değerlendirme yöntemi](../../../../../DEGERLENDIRME.md) · [Sıra](../../../../../TASKS.md)
