# Görev 5.2: Öğeyi silmekle adı silmeyi ayır

**Odak:** del ile indeks, dilim, içerik ve ad silme; pop ile fark.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1](../5.1-more-on-lists/README.md).

## Tek görev

1. a = [10, 20, 30, 40, 50] ve other = a kur. del ile ilk öğeyi, sonra [1:3] dilimini, sonra bütün içeriği sil.

2. Her adımda other üzerinden sonucu kontrol et.

3. En sonda del a yap ve a ile other adlarını ayrı girişlerde değerlendir.

## Geçiş ölçütleri

- [ ] İçerikler sırasıyla [20, 30, 40, 50], [20, 50], [].
- [ ] del a[:] bütün ortak listenin içeriğini silerken del a yalnız bir adı kaldırıyor.
- [ ] a NameError; other hâlâ boş liste.
- [ ] pop değer döndürürken del bir değer üretmek amacıyla kullanılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
