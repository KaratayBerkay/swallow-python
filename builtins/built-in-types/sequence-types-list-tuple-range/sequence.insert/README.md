## `sequence.insert`

```
sequence.insert(index, value, /)
```

Insert *value* into *sequence* at the given *index*.
This is equivalent to writing `sequence[index:index] = [value]`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.26: insert etkisini izle**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`s=[1,2]; diger=s` ile başla. `sonuc=s.insert(1,7)` uygula. s, diger, sonuc ve `s is diger` değerlerini göster. Aynı işlemi yeni bir `[1,2,1]` listesinde tekrarla; değişen öğeleri işaretle.

Aynı kontrolü yeni bir `ba=bytearray([1,2])` üzerinde `ba.insert(1,7)` çağrısıyla tekrarla; dönüşü ve kalan baytları göster.

#### Geçiş ölçütleri

- [ ] İlk listede son durum `[1, 7, 2]`; iki ad aynı nesneyi gösterir.
- [ ] Dönüş None; Öğe verilen indeksin önüne girer.
- [ ] Öğe verilen indeksin önüne girer.

- [ ] Ortak yöntem bytearrayda da doğru dönüş ve son durumla kanıtlanmış; öğeler 0..255 sınırında tutulmuştur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.pop/README.md)
<!-- learning-task:end -->
