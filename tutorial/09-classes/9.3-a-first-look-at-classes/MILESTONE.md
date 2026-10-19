# Milestone: Birbirinden bağımsız durum taşıyan iki nesne kur

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Sınıf tanımı, örnek oluşturma, metot bağı ve ortak/ayrı verinin birlikte kullanımı.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Notebook sınıfı yaz: category sınıfta, owner ve notes örnek üzerinde olsun. add_note ve note_count metotları ekle.

2. İki nesne oluştur, farklı sayıda not ekle; saved = first.note_count kaydet. first değişkenini ikinci nesneye bağladıktan sonra saved ve first.note_count sonuçlarını karşılaştır.

## Geçiş ölçütleri

- [ ] Her nesnenin not listesi bağımsız; category ortak.
- [ ] `__init__` her örneğin durumunu hazırlıyor.
- [ ] saved eski örneğe bağlı kalırken first yeni örneği gösteriyor.
- [ ] Metot çağrısı ile ClassName.method(instance) ilişkisi kendi nesneleri üzerinden açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
