# Görev b:2.14.1: genericalias.__args__ davranışını ayırt et

## Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; argüman tupleı iç içe yapıyı korur

```python
dict[str,list[int]].__args__ == (str,list[int])
tuple[int,str].__args__ == (int,str)
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Argüman tupleı iç içe yapıyı korur

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
