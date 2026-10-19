# Görev b:2.4.3: int.to_bytes davranışını ayırt et

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; uzunluk, bayt sırası ve signed seçimi sonucu belirler

```python
(258).to_bytes(2,"little")
(-2).to_bytes(1,"big",signed=True)
(256).to_bytes(1)
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'\x02\x01'`; `b'\xfe'`; `OverflowError`.
- [ ] Uzunluk, bayt sırası ve signed seçimi sonucu belirler

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
