# Görev b:3.29: getattr davranışını ayırt et

## Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; varsayılan değer yalnız eksik nitelikte kullanılır.

```python
class K: pass
o=K(); o.puan=4
getattr(o,"eksik",0)
getattr(o,"eksik")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `0`; `AttributeError`.
- [ ] Varsayılan değer yalnız eksik nitelikte kullanılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
