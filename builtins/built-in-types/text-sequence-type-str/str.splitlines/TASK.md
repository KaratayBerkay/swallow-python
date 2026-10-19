# Görev b:2.9.41: str.splitlines davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur

```python
"a\n".splitlines()
"a\n\nb".splitlines(True)
"".splitlines()
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['a']`; `['a\n', '\n', 'b']`; `[]`.
- [ ] Sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
