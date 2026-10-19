# Görev b:2.7.2: list davranışını ayırt et

## Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yeni dış listeyle ortak iç nesneyi ayır

```python
a=[[1]]
list(a) is a
list(a)[0] is a[0]
```

Bir listeyi key fonksiyonuyla yerinde sort et; dönüşü ve özgün nesne kimliğini kaydet. Eşit keyli iki öğenin sırasını ve key fonksiyonunun her öğe için bir kez çalışmasını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Yeni dış listeyle ortak iç nesneyi ayır
- [ ] Sort None döndürür, aynı dış listeyi düzenler; stable sıra ve öğe başına tek key hesabı kanıtlanmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
