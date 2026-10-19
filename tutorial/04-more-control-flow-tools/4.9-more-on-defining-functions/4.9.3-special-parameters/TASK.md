# Görev 4.9.3: İmzanın üç bölgesini işaretle

**Odak:** / ve * işaretlerinin konumsal, karma ve yalnız anahtarlı bölgeleri ayırması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.2](../4.9.2-keyword-arguments/README.md).

## Tek görev

1. def send(source, /, target, *, urgent) imzasını kâğıt üzerinde üç bölgeye ayır. send("a", "b", urgent=True), send("a", target="b", urgent=True), send(source="a", target="b", urgent=True) ve send("a", "b", True) çağrılarında her değerin bağlanma durumunu çıkar.

2. Bu adımda gövde yazmak gerekmiyor.

## Geçiş ölçütleri

- [ ] source yalnız konumsal, target iki biçimde, urgent yalnız anahtarla geçiriliyor.
- [ ] İlk iki çağrı geçerli; son ikisinin ayrı kural ihlalleri açıklanmış.
- [ ] / ve * değer alan parametreler gibi sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
