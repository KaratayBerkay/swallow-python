# Görev b:2.9.12: str.format_map davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; alanlar verilen mapping üzerinden çözülür

```python
"{ad}:{puan}".format_map({"ad":"Ece","puan":8})
"{eksik}".format_map({})
```

Kaynak örnekteki `Default(dict)` sınıfını kullan: `__missing__` bulunmayan alanın adını döndürüyor. `"{ad}:{sehir}".format_map(Default(ad="Ece"))` sonucunu çıkar. Aynı nesneyi önce `dict(...)` ile kopyalayınca eksik alan davranışını karşılaştır.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'Ece:8'`; `KeyError`.
- [ ] Alanlar verilen mapping üzerinden çözülür

- [ ] Doğrudan mapping kullanımında "Ece:sehir" elde edilir; normal dict kopyasında eksik alan KeyError verir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
