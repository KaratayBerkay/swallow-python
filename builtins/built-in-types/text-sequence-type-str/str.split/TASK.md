# Görev b:2.9.40: str.split davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sep verilmezse boşluklar birleşir; açık sep boş alanları korur

```python
"  a  b  ".split()
"a,,b,".split(",")
"".split()
"".split(",")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['a', 'b']`; `['a', '', 'b', '']`; `[]`; `['']`.
- [ ] Sep verilmezse boşluklar birleşir; açık sep boş alanları korur

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
