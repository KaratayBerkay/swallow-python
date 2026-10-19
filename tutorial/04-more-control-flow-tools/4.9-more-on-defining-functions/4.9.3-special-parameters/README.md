### 4.9.3. Special parameters

By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

A function definition may look like:

``` text
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

where `/` and `*` are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.


<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.3: İmzanın üç bölgesini işaretle**

**Odak:** / ve * işaretlerinin konumsal, karma ve yalnız anahtarlı bölgeleri ayırması.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.2](../4.9.2-keyword-arguments/README.md).

##### Tek görev

1. def send(source, /, target, *, urgent) imzasını kâğıt üzerinde üç bölgeye ayır. send("a", "b", urgent=True), send("a", target="b", urgent=True), send(source="a", target="b", urgent=True) ve send("a", "b", True) çağrılarında her değerin bağlanma durumunu çıkar.

2. Bu adımda gövde yazmak gerekmiyor.

##### Geçiş ölçütleri

- [ ] source yalnız konumsal, target iki biçimde, urgent yalnız anahtarla geçiriliyor.
- [ ] İlk iki çağrı geçerli; son ikisinin ayrı kural ihlalleri açıklanmış.
- [ ] / ve * değer alan parametreler gibi sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](4.9.3.1-positional-or-keyword-arguments/README.md)
<!-- learning-task:end -->
#### Sections

- [4.9.3.1. Positional-or-Keyword Arguments](4.9.3.1-positional-or-keyword-arguments/README.md)
- [4.9.3.2. Positional-Only Parameters](4.9.3.2-positional-only-parameters/README.md)
- [4.9.3.3. Keyword-Only Arguments](4.9.3.3-keyword-only-arguments/README.md)
- [4.9.3.4. Function Examples](4.9.3.4-function-examples/README.md)
- [4.9.3.5. Recap](4.9.3.5-recap/README.md)

<!-- learning-milestone:start -->
#### Klasör milestone görevi

**Milestone: Parametre sözleşmesi kanıtlarını birleştir**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Çağrı kısıtları ile parametre türü seçiminin gerekçesini birlikte doğrulama.

##### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

##### Tek kontrol

Yeni işlev yazma. [Recap görevinin](4.9.3.5-recap/TASK.md) çözümünü bu klasörün son kontrolü olarak kullan. Bu çözüm, üç parametre türünün birlikte seçimini ve ad değişikliğinin çağrılara etkisini zaten sınar.

Değerlendiren kişi, bu çözümün geçiş ölçütleriyle birlikte [işlev örnekleri görevinde](4.9.3.4-function-examples/TASK.md) sunulan geçerli/geçersiz çağrı ve anahtar çakışması kanıtlarının da tamamlandığını kontrol eder. Eksik kanıt varsa yalnız ilgili eski görev tamamlanır. Aynı imzayı başka adlarla yeniden yazmak veya aynı deneyi ikinci kez yapmak gerekmez.

Klasörün diğer görevleri de tamamlanmış olmalıdır. Önceden geçen tek değişiklik kontrolleri burada yeniden yapılmaz.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.4-arbitrary-argument-lists/README.md)
<!-- learning-milestone:end -->
