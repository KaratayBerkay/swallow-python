# Görev b:3.35: id davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; aynı nesneye ikinci ad verme ile eşit içerikli yeni nesneyi ayır.

```python
a=[1]; b=a; c=a[:]
id(a)==id(c)
a==c
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Aynı nesneye ikinci ad verme ile eşit içerikli yeni nesneyi ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
