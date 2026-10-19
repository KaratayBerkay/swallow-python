# Görev 5.3: Değişmeyen kaydın içindeki listeyi izle

**Odak:** Tuple packing/unpacking, virgül, boş/tek öğeli tuple ve değiştirilebilir içerik.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.2](../5.2-the-del-statement/README.md).
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

## Tek görev

1. record = "Ada", [3, 4] kaydını kur; name, scores = record ile aç. scores listesine 5 ekle ve record içeriğini göster. record[0] değerine yeni ad atamayı ayrı girişte dene.

2. Boş tuple, tek öğeli tuple ve yalnız parantezlenmiş metin oluşturup uzunluklarını karşılaştır.

3. İki öğeli kaydı üç değişkene açmayı da ayrı dene.

## Geçiş ölçütleri

- [ ] record içindeki liste [3, 4, 5] oluyor; tuple öğesinin kendisine atama TypeError.
- [ ] () uzunluğu 0; ("Ada",) uzunluğu 1; ("Ada") bir metin ve uzunluğu 3.
- [ ] Tuple oluşturanın virgül olduğu, packing ve unpacking yönleri açıklanmış.
- [ ] Fazla değişkenle açma ValueError; tuple değişmezliğinin içindeki listeyi değişmez yapmadığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
