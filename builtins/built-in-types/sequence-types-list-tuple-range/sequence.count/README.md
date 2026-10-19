## `sequence.count`

```
sequence.count(value, /)
```

Return the total number of occurrences of *value* in *sequence*.

## Çözümlü kısa örnek

Count eşit öğeleri sayar; bulunmayan değerde sıfır verir

```python
print(repr([1,2,1].count(1)))
# Sonuç: 2
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.7: sequence.count davranışını ayırt et**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; count eşit öğeleri sayar; bulunmayan değerde sıfır verir

```python
(2,2,3).count(2)
[1,2].count(9)
```

Aynı sayma işlemini `range(2, 8, 2)` üzerinde hem bulunan 4 hem bulunmayan 5 için dene. Sonucun bir indeks değil, eşit öğelerin toplam adedi olduğunu açıkla.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `0`.
- [ ] Count eşit öğeleri sayar; bulunmayan değerde sıfır verir

- [ ] Range için sonuçlar 1 ve 0; bütün türlerde dönüş, aranan değerin kaç kez bulunduğunu gösteriyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.index/README.md)
<!-- learning-task:end -->
