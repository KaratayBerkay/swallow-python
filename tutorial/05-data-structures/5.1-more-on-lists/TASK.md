# Görev 5.1: Liste düzenleme günlüğü tut

**Odak:** Liste metotlarının öğe/değer/indeks ayrımı, yerinde değişim, dönüş değeri ve sığ kopya.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).
- Ön bilgi: [t:4.8](../../04-more-control-flow-tools/4.8-defining-functions/README.md).

## Tek görev

1. Bir stok listesi üzerinde işlem günlüğü hazırla: stock = ["pear", "apple", "pear"]. count ve index ile tekrarları incele; insert ile başa "fig" koy; extend ile ["plum", "lime"] ekle; remove ile ilk "pear" değerini sil; pop ile son öğeyi al; sort ve reverse uygula.

2. Her satır için önce listeyi ve varsa dönüş değerini tahmin et, sonra dene.

3. Bağımsız kopyalarda append ile extend, copy ile atama ve clear ile boş listeye yeniden bağlama farkını göster.

4. Olmayan değeri arama/silme ve boş listeden pop denemelerini ayrı yap.

## Geçiş ölçütleri

- [ ] İlk count 2 ve index 0; ikinci pear için arama başlangıcı kullanılmış.
- [ ] remove ilk eşleşmeyi, pop son öğeyi seçiyor ve lime döndürüyor.
- [ ] Sıralama sonrası apple, fig, pear, plum; tersinde plum, pear, fig, apple.
- [ ] Yerinde düzenleyen metotların None dönüşü listeyle karıştırılmamış.
- [ ] append tek öğe, extend ayrı öğeler ekliyor; kopya ile ortak nesne farkı gösterilmiş.
- [ ] Eksik değer ValueError, boş pop IndexError; karışık sıralanamayan türlerin neden sorun olduğu açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
