# Görev b:2.9.30: str.partition davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; i̇lk eşleşmede üç parça döner; bulunmama sabit üçlüdür

```python
"a=b=c".partition("=")
"abc".partition("=")
"abc".partition("")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `('a', '=', 'b=c')`; `('abc', '', '')`; `ValueError`.
- [ ] İlk eşleşmede üç parça döner; bulunmama sabit üçlüdür

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
