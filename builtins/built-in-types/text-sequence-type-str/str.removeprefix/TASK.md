# Görev b:2.9.31: str.removeprefix davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

```python
"ababa".removeprefix("ab")
"baX".removeprefix("ab")
"abc".removeprefix("")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'aba'`; `'baX'`; `'abc'`.
- [ ] Yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
