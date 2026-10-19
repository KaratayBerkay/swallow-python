# Görev b:3.19: dir davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dir keşif için isim listesi verir; içerik türün davranışına göre değişebilir.

```python
class K: puan=4
o=K()
"eksik" in dir(o)
dir(o)==sorted(dir(o))
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Dir keşif için isim listesi verir; içerik türün davranışına göre değişebilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
