# Görev b:2.9.1: str davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; nesne temsilini bayt çözümlemeyle karıştırma

```python
str(b"ab")
str(b"ab","utf-8")
str(b"\xff","utf-8")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `"b'ab'"`; `'ab'`; `UnicodeDecodeError`.
- [ ] Nesne temsilini bayt çözümlemeyle karıştırma

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
