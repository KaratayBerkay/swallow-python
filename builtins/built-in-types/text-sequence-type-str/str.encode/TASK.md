# Görev b:2.9.8: str.encode davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; kodlama yeni bytes üretir; strict hata, replace veri kaybı anlamına gelir

```python
"İ".encode("utf-8")
"İ".encode("ascii")
"İ".encode("ascii","replace")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'\xc4\xb0'`; `UnicodeEncodeError`; `b'?'`.
- [ ] Kodlama yeni bytes üretir; strict hata, replace veri kaybı anlamına gelir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
