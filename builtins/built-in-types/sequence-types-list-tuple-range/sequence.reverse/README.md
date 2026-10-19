## `sequence.reverse`

```
sequence.reverse()
```

Reverse the items of *sequence* in place.
This method maintains economy of space when reversing a large sequence.
To remind users that it operates by side-effect, it returns `None`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.35: reverse etkisini izle**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`s=[1,2]; diger=s` ile başla. `sonuc=s.reverse()` uygula. s, diger, sonuc ve `s is diger` değerlerini göster. Aynı işlemi yeni bir `[1,2,1]` listesinde tekrarla; değişen öğeleri işaretle.

Aynı kontrolü yeni bir `ba=bytearray([1,2])` üzerinde `ba.reverse()` çağrısıyla tekrarla; dönüşü ve kalan baytları göster.

#### Geçiş ölçütleri

- [ ] İlk listede son durum `[2, 1]`; iki ad aynı nesneyi gösterir.
- [ ] Dönüş None; Reverse yerinde çalışır; yeni ters liste döndürmez.
- [ ] Reverse yerinde çalışır; yeni ters liste döndürmez.

- [ ] Ortak yöntem bytearrayda da doğru dönüş ve son durumla kanıtlanmış; öğeler 0..255 sınırında tutulmuştur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
