# Görev b:2.7.20: sequence.copy davranışını ayırt et

## Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dış kopya yeni nesnedir; içteki nesne paylaşılır

```python
a=[[1]]
a.copy() is a
a.copy()[0] is a[0]
```

`bytearray([1,2])` için copy al; kopyayı değiştirince özgün verinin korunmasını ve dönüş türünü göster. İç içe liste örneğinde görülen iç paylaşımı bytearraya neden taşımadığını açıkla.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Dış kopya yeni nesnedir; içteki nesne paylaşılır

- [ ] Bytearray kopyası bağımsız bytearraydır; tamsayı öğelerin paylaşımı mutable iç liste paylaşımı değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
