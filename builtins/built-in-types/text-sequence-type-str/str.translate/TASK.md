# Görev b:2.9.46: str.translate davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tabloda eksik karakter korunur; None siler; metin birden çok karaktere dönüşebilir

```python
"abca".translate({ord("a"):"XY",ord("b"):None})
"abc".translate({})
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'XYcXY'`; `'abc'`.
- [ ] Tabloda eksik karakter korunur; None siler; metin birden çok karaktere dönüşebilir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
