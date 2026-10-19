# Görev 8.5: Hata çevirisinin nedenini görünür kıl

**Odak:** Örtük zincir, from exc ile açık neden ve from None ile zinciri göstermeme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.4](../8.4-raising-exceptions/README.md).

## Tek görev

1. int("bad") hatasını yakalayıp RuntimeError("invalid count") üreten üç ayrı sürüm yaz: doğrudan raise, raise ... from exc ve raise ... from None.

2. Her birini ayrı çalıştır ve traceback içinde görünen hata bölümleriyle aralarındaki ilişkiyi karşılaştır.

## Geçiş ölçütleri

- [ ] Üç sürümün son hatası RuntimeError.
- [ ] Doğrudan raise örtük bağlamı, from exc açık nedeni gösteriyor.
- [ ] from None çıktıda önceki bağlam zincirini göstermiyor; önceki işlemin gerçekleşmediği sanılmamış.
- [ ] Hata çevirisinin hangi düşük seviye işlemi hangi uygulama hatasına bağladığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
