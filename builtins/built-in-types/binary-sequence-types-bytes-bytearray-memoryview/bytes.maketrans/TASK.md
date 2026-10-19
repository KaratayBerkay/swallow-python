# Görev b:2.10.20: bytes.maketrans davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; binary tablo 256 bayttır; iki taraf eşit uzunlukta olmalıdır

```python
bytes.maketrans(b"a",b"x")[97]
bytes.maketrans(b"ab",b"x")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `120`; `ValueError`.
- [ ] Binary tablo 256 bayttır; iki taraf eşit uzunlukta olmalıdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
