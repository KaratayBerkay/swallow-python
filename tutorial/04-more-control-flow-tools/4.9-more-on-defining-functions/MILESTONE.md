# Milestone: Küçük bir fonksiyon arayüzünü tasarla

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Varsayılanlar, çağrı sözleşmesi, args/kwargs, lambda ve işlev açıklamalarını birlikte kullanma.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir mesaj üretici yaz: ilk prefix yalnız konumla, sıfır veya daha çok mesaj parçası `*parts` ile, sep varsayılan ":" ve yalnız anahtarla alınsın.

2. Tek bir metin döndürsün; docstring ve str dönüş annotation ekle.

3. Hazır parça listesini çağrıda * ile aç; sep değerini hazır sözlükten ** ile ver.

4. Ayrı olarak (sıra, mesaj) çiftlerini lambda key ile mesaja göre sırala.

5. Paylaşılan boş liste varsayılanı kullanılmadığını ve annotationın neyi garanti etmediğini açıkla.

## Geçiş ölçütleri

- [ ] Sıfır parçada yalnız prefix, çok parçada doğru ayraçla birleşim.
- [ ] Çağrıdaki açma ile tanımdaki toplama ayrılmış; sep konumsalla değişmiyor.
- [ ] Docstring gerçek davranışla tutarlı; annotation kendiliğinden çalışma zamanı kontrolü sayılmamış.
- [ ] Lambda mesaj alanını anahtar seçiyor.
- [ ] Bir sonraki çağrı önceki parçaları biriktirmiyor; en az iki çağrı kanıtı var.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
