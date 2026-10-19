# Görev b:2.7: sequence-types-list-tuple-range davranışını ayırt et

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; negatif indeks ve dilimde dış sınırla tek indeks hatasını ayır

```python
[3,5,7][1:99]
[3,5,7][99]
[1,2]*2
```

`a=[[0]]*2` örneğinde bir iç listeyi değiştirerek tekrarın referans paylaştığını göster. Extended slice atamasında eşit uzunluk şartını ve tuple içinde mutable öğe bulunabileceğini ayrı örnekle kanıtla.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[5, 7]`; `IndexError`; `[1, 2, 1, 2]`.
- [ ] Negatif indeks ve dilimde dış sınırla tek indeks hatasını ayır
- [ ] Tekrarın iç nesneyi kopyalamadığı gösterilir; adımı 1 olmayan dilime uzunluk uyumsuz atama ValueError verir; tuple değişmezliği iç öğeyi dondurmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
