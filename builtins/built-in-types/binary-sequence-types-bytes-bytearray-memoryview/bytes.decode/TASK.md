# Görev b:2.10.10: bytes.decode davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; çözümleme str verir; geçersiz baytta hata politikasını ayır

```python
b"\xc4\xb0".decode("utf-8")
b"\xff".decode("utf-8")
b"\xff".decode("utf-8","replace")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'İ'`; `UnicodeDecodeError`; `'�'`.
- [ ] Çözümleme str verir; geçersiz baytta hata politikasını ayır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
