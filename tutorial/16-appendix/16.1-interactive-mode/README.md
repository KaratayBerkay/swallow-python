## 16.1. Interactive Mode

There are two variants of the interactive REPL. The classic basic interpreter is supported on all platforms with minimal line control capabilities.

Since Python 3.13, a new interactive shell is used by default. This one supports color, multiline editing, history browsing, and paste mode. To disable color, see Controlling color for details. Function keys provide some additional functionality. F1 enters the interactive help browser `pydoc`. F2 allows for browsing command-line history with neither output nor the \>\>\> and ... prompts. F3 enters "paste mode", which makes pasting larger blocks of code easier. Press F3 to return to the regular prompt.

When using the new interactive shell, exit the shell by typing exit or quit. Adding call parentheses after those commands is not required.

If the new interactive shell is not desired, it can be disabled via the `PYTHON_BASIC_REPL` environment variable.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 16.1: REPL özelliklerini sürüm koşuluyla oku**

**Odak:** Temel ve yeni REPL, 3.13 koşulu, F1/F2/F3 ve çıkış biçimleri.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:14.2](../../14-interactive-input-editing-and-history-substitution/14.2-alternatives-to-the-interactive-interpreter/README.md).
- Ön bilgi: [t:15.1](../../15-floating-point-arithmetic-issues-and-limitations/15.1-representation-error/README.md).

#### Tek görev

1. Kendi Python sürümünü kaydet.

2. Bölümden iki sütunlu özellik kartı çıkar: temel REPL; 3.13+ yeni REPL.

3. F1, F2, F3, çok satırlı düzenleme, parantezsiz exit/quit ve PYTHON_BASIC_REPL öğelerini uygun tarafa yerleştir.

4. Destekleyen ortam varsa bir özelliği gözlemle; yoksa görev yazılı kart üzerinden değerlendirilsin.

#### Geçiş ölçütleri

- [ ] Yeni özellikler 3.13+ şartıyla ilişkilendirilmiş, 3.11 üzerinde yokluğu yanlış öğrenme sayılmamış.
- [ ] F1 yardım, F2 geçmiş taraması, F3 yapıştırma modu; tekrar F3 ile dönüş.
- [ ] Klasik quit() ile yeni parantezsiz çıkış ayrılmış.
- [ ] PYTHON_BASIC_REPL arayüz seçimiyle ilişkilendirilmiş; kalıcı ortam ayarı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](16.1.1-error-handling/README.md)
<!-- learning-task:end -->
### Sections

- [16.1.1. Error Handling](16.1.1-error-handling/README.md)
- [16.1.2. Executable Python Scripts](16.1.2-executable-python-scripts/README.md)
- [16.1.3. The Interactive Startup File](16.1.3-the-interactive-startup-file/README.md)
- [16.1.4. The Customization Modules](16.1.4-the-customization-modules/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Yorumlayıcı başlangıcını değiştirmeden teşhis et**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** REPL sürümü, betik başlığı, hata akışı ve başlangıç özelleştirme kapsamı.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Bir betik terminalde farklı, REPLde farklı davranıyor senaryosu için inceleme kaydı hazırla.

2. Kod hatasını, stdout/stderr ayrımını, shebang/PATH/izin durumunu ve PYTHONSTARTUP ile usercustomize/sitecustomize etkilerini ayrı kanıt kaynaklarına ayır.

3. Bir örnek olarak marker değişkeninin yalnız etkileşimli startup dosyasında tanımlı olduğu durumda betikten erişimi açıklayıp yerel minimal taslağı yaz.

4. Kullanıcı başlangıç dosyalarını değiştirmek gerekmiyor.

#### Geçiş ölçütleri

- [ ] REPL destek sınırı sürümle ilişkilendirilmiş.
- [ ] Betik hatasıyla giriş arayüzü ve çalıştırma izni sorunları karıştırılmamış.
- [ ] Startup marker normal betiğe otomatik taşınmıyor.
- [ ] Customization sırası ve -s kullanıcı sınırı doğru.
- [ ] Önerilen inceleme gerçek dosya/başlangıç düzenini değiştirmeden yapılabilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-milestone:end -->
