# Görev 5.5.1: Finder cacheini modül cacheinden ayır

**Odak:** sys.path_importer_cache, path_hooks kabul/ret akışı, None cache ve boş yol girdisi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.5](../README.md).
- Ön bilgi: [r:5.3.1](../../5.3-searching/5.3.1-the-module-cache/README.md).

## Tek görev

1. Bir yol girdisi için importer_cache boş olsun; H1 hooku ImportError yükseltsin, H2 finder döndürsün.

2. İlk ve ikinci aramada hangi hookların çağrıldığını tabloya yaz.

3. Başka bir girdiyi bütün hooklar reddetsin; cache içine ne konduğunu göster. "" girdisinde geçerli dizinin ve bulunamayan dizinin özel durumlarını ekle. sys.modules ile bu cachein anahtar/değerlerini karşılaştır.

## Geçiş ölçütleri

- [ ] İlk aramada H1 reddi sonrası H2 denenir; finder cachelenince ikinci aramada hook seçimi tekrarlanmaz.
- [ ] Hiçbiri kabul etmezse yol için None cachelenir; bu sys.modules içindeki None ile aynı olay değil.
- [ ] Importer cache yol->finder; modules cache modül adı->modül.
- [ ] Geçerli çalışma dizini taze çözülür ve gerçek yolu cache anahtarıdır; mevcut değilse kayıt eklenmez.
- [ ] Metin olmayan sys.path girdilerinin yok sayılması ve alt modülde ebeveyn `__path__` kullanılması belirtilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
