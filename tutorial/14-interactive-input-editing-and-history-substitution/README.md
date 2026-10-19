# 14. Interactive Input Editing and History Substitution

Some versions of the Python interpreter support editing of the current input line and history substitution, similar to facilities found in the Korn shell and the GNU Bash shell. This is implemented using the [GNU Readline](https://tiswww.case.edu/php/chet/readline/rltop.html) library, which supports various styles of editing. This library has its own documentation which we won't duplicate here.


<!-- learning-task:start -->
## Bölüm görevi

**Görev 14: Düzenleme desteğini Python dilinden ayır**

**Odak:** Yorumlayıcı arayüzü, satır düzenleme desteği ve platform bağımlılığı.

### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:2.1](../02-using-the-python-interpreter/2.1-invoking-the-interpreter/README.md).
- Ön bilgi: [t:13](../13-what-now/README.md).

### Tek görev

1. Kısa bir ortam notunda iki şeyi ayır: Python ifadesinin anlamı; o ifadeyi oturuma girerken imleç/geçmiş düzenleme desteği.

2. Bölümdeki Readline açıklamasına göre neden iki bilgisayarda aynı Python kodu çalışırken giriş düzenleme deneyiminin farklı olabileceğini açıkla.

### Geçiş ölçütleri

- [ ] Dil semantiği ile etkileşimli arayüz özelliği ayrı.
- [ ] Readline desteğinin her sürüm/platformda aynı olduğu varsayılmamış.
- [ ] Henüz listelenmeyen özel tuş kombinasyonları veya shell kurulumu gerekmiyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](14.1-tab-completion-and-history-editing/README.md)
<!-- learning-task:end -->
## Sections

- [14.1. Tab Completion and History Editing](14.1-tab-completion-and-history-editing/README.md)
- [14.2. Alternatives to the Interactive Interpreter](14.2-alternatives-to-the-interactive-interpreter/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Arayüz sorununu öğrenme eksikliğinden ayır**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Satır düzenleme, tamamlama, geçmiş ve alternatif arayüzü kanıta göre değerlendirme.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek kontrol

Yeni bir teşhis notu yazma. [Bölüm görevinin](TASK.md) dil/arayüz ayrımını, [14.1 görevinin](14.1-tab-completion-and-history-editing/TASK.md) tamamlama/geçmiş gözlemini ve [14.2 görevinin](14.2-alternatives-to-the-interactive-interpreter/TASK.md) alternatif seçimini aynı kontrol kaydında kullan.

Değerlendiren kişi bu üç görevin geçiş ölçütlerinin ve tek değişiklik kontrollerinin tamamlandığını doğrular. Desteklenmeyen REPL özelliği, ilgili görevin izin verdiği ortam kaydıyla değerlendirilir. Eksik kanıt varsa yalnız ilgili görev tamamlanır; daha önce sunulan açıklama veya deney tekrarlanmaz.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../15-floating-point-arithmetic-issues-and-limitations/README.md)
<!-- learning-milestone:end -->
