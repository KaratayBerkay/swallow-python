# Görev b:2.4.4: int.from_bytes davranışını ayırt et

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; aynı baytların değeri byteorder ve signed ile değişir

```python
int.from_bytes(b"\x01\x02","little")
int.from_bytes(b"\xff","big",signed=True)
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `513`; `-1`.
- [ ] Aynı baytların değeri byteorder ve signed ile değişir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
