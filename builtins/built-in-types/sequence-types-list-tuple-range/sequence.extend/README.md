## `sequence.extend`

```
sequence.extend(iterable, /)
```

Extend *sequence* with the contents of *iterable*.
For the most part, this is the same as writing
`seq[len(seq):len(seq)] = iterable`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.23: extend etkisini izle**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`s=[1,2]; diger=s` ile başla. `sonuc=s.extend([7,8])` uygula. s, diger, sonuc ve `s is diger` değerlerini göster. Aynı işlemi yeni bir `[1,2,1]` listesinde tekrarla; değişen öğeleri işaretle.

Aynı kontrolü yeni bir `ba=bytearray([1,2])` üzerinde `ba.extend([7,8])` çağrısıyla tekrarla; dönüşü ve kalan baytları göster.

#### Geçiş ölçütleri

- [ ] İlk listede son durum `[1, 2, 7, 8]`; iki ad aynı nesneyi gösterir.
- [ ] Dönüş None; Extend iterableın öğelerini ayrı ayrı ekler.
- [ ] Extend iterableın öğelerini ayrı ayrı ekler.

- [ ] Ortak yöntem bytearrayda da doğru dönüş ve son durumla kanıtlanmış; öğeler 0..255 sınırında tutulmuştur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.insert/README.md)
<!-- learning-task:end -->
