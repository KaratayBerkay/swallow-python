# Görev 5.5: Anahtarın yaşam döngüsünü yönet

**Odak:** Sözlük oluşturma, ekleme/güncelleme/silme, get, üyelik, anahtar sırası, uygun anahtar ve birleştirme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.4](../5.4-sets/README.md).
- Ön bilgi: [t:5.2](../5.2-the-del-statement/README.md).

**Kaynak/ortam notu:** Yalnız son örnekteki {`**i` for ...} Python 3.15 gerektirir; sözlük oluşturma ve {`**left`, `**right`} birleştirmesi eski sürümlerde de kullanılabilir.

## Tek görev

1. stock = {"pear": 2, "apple": 1} için pear miktarını 5 yap, fig ekle, apple sil.

2. Var olan ve olmayan anahtarları [] ve get ile ayrı ayrı sorgula; list(stock) ve sorted(stock) sonuçlarını karşılaştır.

3. Aynı veriyi çiftler listesinden dict ile yeniden kur. 1, 2, 3 için kareler sözlüğü üret; başka bir sözlükle aynı anahtarın da bulunduğu ** birleştirmesi yap.

4. Anahtar olarak metin, sayı, yalnız değişmez öğeler içeren tuple ve liste seçeneklerini değerlendir.

## Geçiş ölçütleri

- [ ] Güncelleme yeni pear anahtarı üretmiyor; silme/ekleme sonrası anahtarlar pear, fig sırasıyla.
- [ ] Eksik [] KeyError; get varsayılanı None veya verilen değer; üyelik anahtarları kontrol ediyor.
- [ ] Comprehension {1: 1, 2: 4, 3: 9}; sağdaki sözlüğün çakışan değeri kazanıyor.
- [ ] Liste ve içinde liste bulunan tuple anahtar olarak kabul edilmiyor; değerler aynı kısıta tabi tutulmamış.
- [ ] {`**i` for i in all_values} örneğinin neyi birleştirdiği yazılı olarak açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
