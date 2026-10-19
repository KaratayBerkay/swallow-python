# Milestone: Kalıtım aramasını durumdan ayrı izle

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Tek/çoklu kalıtım, override ve örnek türü ilişkilerini birleştirme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Base içinde run(self) yalnız self.label() döndürsün.

2. Left(Base) boş, Right(Base) label ile "right" döndürsün; Combined(Left, Right) boş olsun.

3. Combined örneğinde run sonucunu önce türet, sonra kontrol et.

4. Left içine label ekleyip değişimi göster; isinstance/issubclass ilişkilerini belirt.

5. Aynı örnekte üst metodun doğrudan çağrısıyla alt override çağrısını karşılaştır.

## Geçiş ölçütleri

- [ ] İlk sonuç right, Left override sonrası left.
- [ ] Ortak Base erken seçilerek Right atlanmamış.
- [ ] Tür/aile ilişkileri nesne ile sınıf düzeyinde doğru.
- [ ] Üst run içindeki self çağrısının dinamik olarak alt label bulması açıklanmış; MRO listesini ezberden saymak tek kanıt değil.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
