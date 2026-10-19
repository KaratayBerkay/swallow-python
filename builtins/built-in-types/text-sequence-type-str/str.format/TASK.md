# Görev b:2.9.3: str.format davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; alanları konumsal ve adlandırılmış argümanlara eşleştir

```python
"{1}:{0}".format("a","b")
"{ad}:{puan}".format(ad="Ada",puan=7)
"{eksik}".format(ad="Ada")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'b:a'`; `'Ada:7'`; `KeyError`.
- [ ] Alanları konumsal ve adlandırılmış argümanlara eşleştir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
