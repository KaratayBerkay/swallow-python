# Milestone: Durumu olan, dolaşılabilen küçük bir koleksiyon yap

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Nesne sahipliği, metot, iterator/generator ve kalıtımı birlikte kullanma.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. ReadingList sınıfında owner ve entries listesi örnek üzerinde tutulsun. add(title) ve `__iter__` içinde yield ile öğe dolaşımı olsun.

2. İki nesnenin bağımsızlığını göster.

3. TaggedReadingList alt sınıfı add davranışını önce etiketi ekleyip sonra üst add metodunu açık çağırarak genişletsin.

4. Generator expressionla başlık uzunluklarının toplamını al.

5. Son bir izde tükenen generator, yeni iter çağrısı ve kaydedilmiş bound method davranışını kendi nesnelerin üzerinden açıkla.

## Geçiş ölçütleri

- [ ] İki liste veri paylaşmıyor; alt sınıf eklemesi yalnız hedef örneğe gidiyor.
- [ ] for ile ekleme sırası korunuyor; tükenmiş generator yeniden değer üretmiyor.
- [ ] Yeni iter yeni generator üretebiliyor; bunun kendini döndüren tüketilmiş iterator örneğinden farkı açıklanmış.
- [ ] Toplam gerçek başlıklardan hesaplanıyor.
- [ ] Nitelik, metot ve modül kapsamı ayrılmış; private isimlerin erişim güvenliği sağlamadığı kaynak sınırıyla belirtilmiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
