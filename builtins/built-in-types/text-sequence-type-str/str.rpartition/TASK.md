# Görev b:2.9.37: str.rpartition davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

```python
"a=b=c".rpartition("=")
"abc".rpartition("=")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `('a=b', '=', 'c')`; `('', '', 'abc')`.
- [ ] Sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
