# Görev b:2.9.10: str.expandtabs davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir

```python
"ab\tc".expandtabs(4)
"abcd\tx".expandtabs(4)
"a\nb\tc".expandtabs(4)
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'ab  c'`; `'abcd    x'`; `'a\nb   c'`.
- [ ] Tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
