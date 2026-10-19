# Görev b:2.14.4: genericalias.__unpacked__ davranışını ayırt et

## Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unpacked alias işaretiyle normal aliası ayır

```python
(*tuple[float,str],)[0].__unpacked__
(*tuple[float,str],)[0].__origin__ is tuple
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Unpacked alias işaretiyle normal aliası ayır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
