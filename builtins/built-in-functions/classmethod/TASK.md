# Görev b:3.14: classmethod sözleşmesini uygula

## Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Bir `Kayit` sınıfında `@classmethod def kur(cls, ad): return cls(ad)` alternatif kurucusunu yaz. `OzelKayit(Kayit)` alt sınıfını oluştur. İki sınıftan ve bir örnekten çağrıldığında alınan `cls` ve dönen nesnenin türünü doğrula.

## Geçiş ölçütleri

- [ ] Sınıftan ve örnekten çağrı ilk argüman olarak sınıfı alır.
- [ ] Alt sınıftaki kurucu alt sınıf örneği üretir; sınıf adı sabitlenmemiştir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
