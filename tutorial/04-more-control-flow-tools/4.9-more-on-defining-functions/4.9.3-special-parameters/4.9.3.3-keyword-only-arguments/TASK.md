# Görev 4.9.3.3: Anlamlı seçeneği anahtarla zorunlu kıl

**Odak:** * sonrasındaki parametrenin yalnız anahtarla verilmesi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.2](../4.9.3.2-positional-only-parameters/README.md).

## Tek görev

1. def label(name, *, color) gövdesinden name + ":" + color döndür. label("box", color="red"), label(name="box", color="red") ve label("box", "red") çağrılarını karşılaştır.

## Geçiş ölçütleri

- [ ] İlk iki çağrı box:red döndürüyor; üçüncü çağrı kabul edilmiyor.
- [ ] * işaretinin name parametresini konumsal olmaya zorlamadığı açıklanmış.
- [ ] color değerinin neden açık isimle verilmesi gerektiği imzadan gösterilmiş.

[Değerlendirme yöntemi](../../../../../DEGERLENDIRME.md) · [Sıra](../../../../../TASKS.md)
