## 4.9. More on Defining Functions

It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

### Sections

- [4.9.1. Default Argument Values](4.9.1-default-argument-values/README.md)
- [4.9.2. Keyword Arguments](4.9.2-keyword-arguments/README.md)
- [4.9.3. Special parameters](4.9.3-special-parameters/README.md)
- [4.9.4. Arbitrary Argument Lists](4.9.4-arbitrary-argument-lists/README.md)
- [4.9.5. Unpacking Argument Lists](4.9.5-unpacking-argument-lists/README.md)
- [4.9.6. Lambda Expressions](4.9.6-lambda-expressions/README.md)
- [4.9.7. Documentation Strings](4.9.7-documentation-strings/README.md)
- [4.9.8. Function Annotations](4.9.8-function-annotations/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Küçük bir fonksiyon arayüzünü tasarla**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Varsayılanlar, çağrı sözleşmesi, args/kwargs, lambda ve işlev açıklamalarını birlikte kullanma.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Bir mesaj üretici yaz: ilk prefix yalnız konumla, sıfır veya daha çok mesaj parçası `*parts` ile, sep varsayılan ":" ve yalnız anahtarla alınsın.

2. Tek bir metin döndürsün; docstring ve str dönüş annotation ekle.

3. Hazır parça listesini çağrıda * ile aç; sep değerini hazır sözlükten ** ile ver.

4. Ayrı olarak (sıra, mesaj) çiftlerini lambda key ile mesaja göre sırala.

5. Paylaşılan boş liste varsayılanı kullanılmadığını ve annotationın neyi garanti etmediğini açıkla.

#### Geçiş ölçütleri

- [ ] Sıfır parçada yalnız prefix, çok parçada doğru ayraçla birleşim.
- [ ] Çağrıdaki açma ile tanımdaki toplama ayrılmış; sep konumsalla değişmiyor.
- [ ] Docstring gerçek davranışla tutarlı; annotation kendiliğinden çalışma zamanı kontrolü sayılmamış.
- [ ] Lambda mesaj alanını anahtar seçiyor.
- [ ] Bir sonraki çağrı önceki parçaları biriktirmiyor; en az iki çağrı kanıtı var.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.10-intermezzo-coding-style/README.md)
<!-- learning-milestone:end -->
