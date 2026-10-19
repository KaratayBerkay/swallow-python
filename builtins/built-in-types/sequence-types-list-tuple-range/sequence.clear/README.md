## `sequence.clear`

```
sequence.clear()
```

> *Added in version 3.3.*

Remove all items from *sequence*.
This is equivalent to writing `del sequence[:]`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.17: clear etkisini izle**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`s=[1,2]; diger=s` ile başla. `sonuc=s.clear()` uygula. s, diger, sonuc ve `s is diger` değerlerini göster. Aynı işlemi yeni bir `[1,2,1]` listesinde tekrarla; değişen öğeleri işaretle.

Aynı kontrolü yeni bir `ba=bytearray([1,2])` üzerinde `ba.clear()` çağrısıyla tekrarla; dönüşü ve kalan baytları göster.

#### Geçiş ölçütleri

- [ ] İlk listede son durum `[]`; iki ad aynı nesneyi gösterir.
- [ ] Dönüş None; Clear aynı nesneyi boşaltır; yeni listeye bağlamaz.
- [ ] Clear aynı nesneyi boşaltır; yeni listeye bağlamaz.

- [ ] Ortak yöntem bytearrayda da doğru dönüş ve son durumla kanıtlanmış; öğeler 0..255 sınırında tutulmuştur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.copy/README.md)
<!-- learning-task:end -->
