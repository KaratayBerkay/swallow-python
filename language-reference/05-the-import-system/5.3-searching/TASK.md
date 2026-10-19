# Görev 5.3: Noktalı importu sırayla çöz

**Odak:** Tam nitelikli ad, ebeveynleri sırayla içe aktarma ve ara düzeyde hata.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.2.2](../5.2-packages/5.2.2-namespace-packages/README.md).

## Tek görev

1. foo.bar.baz için üç arama aşaması yaz.

2. Ayrı senaryolarda foo yok, foo var ama bar yok, bütün ebeveynler var ama baz yok kabul et.

3. Her durumda hangi aşamaya kadar gelindiğini ve hangi hata ile durulduğunu göster.

4. Ebeveynler bulunmadan doğrudan son dosyaya gitmenin neden doğru model olmadığını açıkla.

## Geçiş ölçütleri

- [ ] Sıra foo, foo.bar, foo.bar.baz.
- [ ] Hata ilgili ilk başarısız düzeyde ModuleNotFoundError; sonrası yürütülmüyor.
- [ ] Tam adın disk yolu değil import adı olduğu ayrılmış.
- [ ] Henüz alt bölümdeki cache/finder ayrıntılarıyla yeni mekanizma tasarlamak gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
