# Öğrenme görevlerinin sırası

Her adım: anlatımı oku -> örneği incele/dene -> tek bölüm görevini çöz -> kanıtla değerlendir -> ilerle.

Görev metni anlatımın kendi `README.md` sayfasındadır: örneklerden sonra, alt bölüm listesinden önce. Milestone aynı klasörün alt bölüm listesinden sonra yer alır. Aşağıdaki görev bağlantıları anlatımı baştan açar; milestone bağlantıları tamamlanmış klasörün kontrolüne gider. Her kontrolün sonundaki **Sonraki adım** bağlantısıyla sırayı takip edebilirsin.

Milestone klasörün sonunda gelir. Tek konulu yaprak klasörde TASK.md o adımın kontrolüdür; ikinci bir görev yoktur. Kapsamı mevcut kontrolle zaten sınanmış milestone aynı çözüm kanıtını kullanır, tekrar iş çıkarmaz.

Görevler yalnız mevcut ve daha önce işlenmiş konulara dayanır. Bir ileri konuya bağlantı görmek, o konunun öğrenildiği anlamına gelmez. Hazır iskelet üzerinden inceleme isteniyorsa o iskeletin daha ileri mekanizmasını yeniden yazman beklenmez.

Her görevin ölçütlerini [değerlendirme yöntemiyle](DEGERLENDIRME.md) kullan. Ortak kanıt ve tek değişiklik kontrolü bu kılavuzda bir kez açıklanır; her görevde yeniden yazılmaz. Kutucuğu yalnız değerlendirme kararı Geçti olduktan sonra işaretle. Bölüm başlıkları ve ilk boş kutucuk kaldığın yeri gösterir. Doğru çıktı tek başına anlama kanıtı değildir. Bu dosya veya denetleyici, bir görevin öğrenci tarafından başarıldığını otomatik ilan etmez.

Kapsam: 147 bölüm görevi, 35 klasör milestone noktası. Bunların 6 tanesi mevcut kontrolün çözüm kanıtını tekrar iş yaptırmadan kullanır. Yalnız konu adlarını veren 8. bölüm girişinde ayrı görev yoktur; hata inceleme kontrolleri açıklamalardan sonra 8.1 ve 8.2'de yapılır.

## Ortam sınırları

Metin Python 3.15 örnekleri içeriyor; inceleme ortamı Python 3.11.16. Yıldızlı comprehension/generator örnekleri ilgili görevlerde 3.15 olarak işaretli. Eski sürümde yalnız o kısım gerekçeli yazılı iz ve aynı konudaki tek değişiklik kontrolüyle geçilebilir; sıradaki adıma geçişi engellemez. Çalıştırma kanıtı ayrıca bekleyen uygulama olarak kaydedilir, uygulama doğrulanmış sayılmaz. Yeni yorumlayıcı kurmak görevlerin önkoşulu değildir. REPL ve sum gibi sürüme bağlı farklar ilgili görevde belirtilir.

Örnek .py dosyalarının bir kısmı REPL parçası, kasıtlı hata, yer tutucu veya göreli import içerir. Hepsini topluca çalıştırma. Görevdeki anlatımın bağlamını kendi çalışma dosyana taşı; öğretilmemiş import/kurulum sorunlarını görev diye çözmen beklenmez.

## Tutorial

### 2. Yorumlayıcıyı kullanma

- [ ] [Görev 2.1: Python oturumunu doğru başlat](tutorial/02-using-the-python-interpreter/2.1-invoking-the-interpreter/README.md)
- [ ] [Görev 2.1.1: Komutun programa bıraktığı argümanları izle](tutorial/02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.1-argument-passing/README.md)
- [ ] [Görev 2.1.2: Çok satırlı örneği REPL içinde tamamla](tutorial/02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.2-interactive-mode/README.md)
- [ ] [Milestone 2.1: Bir çalıştırma kaydını yeniden kur](tutorial/02-using-the-python-interpreter/2.1-invoking-the-interpreter/README.md#klasör-milestone-görevi)
- [ ] [Görev 2.2.1: Kaynak dosyasının kodlamasını seç](tutorial/02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/2.2.1-source-code-encoding/README.md)
- [ ] [Milestone 2.2: Kaynak kodlaması geçişi](tutorial/02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/README.md#klasör-milestone-görevi)
- [ ] [Milestone 2: Çalıştırılabilir öğrenme örneğini teslim et](tutorial/02-using-the-python-interpreter/README.md#klasör-milestone-görevi)

### 3. Sayı, metin, liste ve ilk programlar

- [ ] [Görev 3: Örnekten yalnızca Python girdisini ayır](tutorial/03-an-informal-introduction-to-python/README.md)
- [ ] [Görev 3.1.1: Bir siparişin hesabını yorumlayıcıda çıkar](tutorial/03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.1-numbers/README.md)
- [ ] [Görev 3.1.2: Bir metin etiketini parçalarından kur](tutorial/03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.2-text/README.md)
- [ ] [Görev 3.1.3: Ortak liste ile kopyayı ayır](tutorial/03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md)
- [ ] [Milestone 3.1: Kopyalanan alışveriş verisini koru](tutorial/03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/README.md#klasör-milestone-görevi)
- [ ] [Görev 3.2: Döngüdeki iki değerin değişimini izle](tutorial/03-an-informal-introduction-to-python/3.2-first-steps-towards-programming/README.md)
- [ ] [Milestone 3: Bir sonraki değeri eski durumdan üret](tutorial/03-an-informal-introduction-to-python/README.md#klasör-milestone-görevi)

### 4. Kontrol akışı ve fonksiyonlar

- [ ] [Görev 4.1: Tek bir koşul dalı seç](tutorial/04-more-control-flow-tools/4.1-if-statements/README.md)
- [ ] [Görev 4.2: Sırayı koruyarak bir koleksiyonu işle](tutorial/04-more-control-flow-tools/4.2-for-statements/README.md)
- [ ] [Görev 4.3: Aralığın sınırını ve adımını tasarla](tutorial/04-more-control-flow-tools/4.3-the-range-function/README.md)
- [ ] [Görev 4.4: Atlama ile döngüyü bitirmeyi ayır](tutorial/04-more-control-flow-tools/4.4-break-and-continue-statements/README.md)
- [ ] [Görev 4.5: Arama bittiğinde doğru mesajı üret](tutorial/04-more-control-flow-tools/4.5-else-clauses-on-loops/README.md)
- [ ] [Görev 4.6: Boş dalın akışını koru](tutorial/04-more-control-flow-tools/4.6-pass-statements/README.md)
- [ ] [Görev 4.7: Desen yönlendiricisinin karar tablosunu çıkar](tutorial/04-more-control-flow-tools/4.7-match-statements/README.md)
- [ ] [Görev 4.8: Yazdırılan sonuçla dönen sonucu ayır](tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md)
- [ ] [Görev 4.9.1: Varsayılan değerin ömrünü düzelt](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.1-default-argument-values/README.md)
- [ ] [Görev 4.9.2: Çağrıdaki değerleri parametrelere bağla](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.2-keyword-arguments/README.md)
- [ ] [Görev 4.9.3: İmzanın üç bölgesini işaretle](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/README.md)
- [ ] [Görev 4.9.3.1: Normal parametreyi iki biçimde çağır](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.1-positional-or-keyword-arguments/README.md)
- [ ] [Görev 4.9.3.2: Konumsal parametrenin adını serbest bırak](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.2-positional-only-parameters/README.md)
- [ ] [Görev 4.9.3.3: Anlamlı seçeneği anahtarla zorunlu kıl](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.3-keyword-only-arguments/README.md)
- [ ] [Görev 4.9.3.4: Karma imzayla ad çakışmasını çöz](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.4-function-examples/README.md)
- [ ] [Görev 4.9.3.5: Çağrı sözleşmesine uygun imzayı seç](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.5-recap/README.md)
- [ ] [Milestone 4.9.3: Parametre sözleşmesi kanıtlarını birleştir](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/README.md#klasör-milestone-görevi)
- [ ] [Görev 4.9.4: Değişken sayıda parçayı birleştir](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.4-arbitrary-argument-lists/README.md)
- [ ] [Görev 4.9.5: Hazır argümanları çağrıda aç](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.5-unpacking-argument-lists/README.md)
- [ ] [Görev 4.9.6: Küçük bir işlevi değer olarak taşı](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.6-lambda-expressions/README.md)
- [ ] [Görev 4.9.7: Davranışı anlatan docstring yaz](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.7-documentation-strings/README.md)
- [ ] [Görev 4.9.8: Tür açıklamasını çalışma zamanı denetiminden ayır](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.8-function-annotations/README.md)
- [ ] [Milestone 4.9: Küçük bir fonksiyon arayüzünü tasarla](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/README.md#klasör-milestone-görevi)
- [ ] [Görev 4.10: Aynı işlevi okunabilir biçimde yaz](tutorial/04-more-control-flow-tools/4.10-intermezzo-coding-style/README.md)
- [ ] [Milestone 4: Arama yapan küçük bir fonksiyon kur](tutorial/04-more-control-flow-tools/README.md#klasör-milestone-görevi)

### 5. Veri yapıları

- [ ] [Görev 5.1: Liste düzenleme günlüğü tut](tutorial/05-data-structures/5.1-more-on-lists/README.md)
- [ ] [Görev 5.1.1: Son eklenen işi geri al](tutorial/05-data-structures/5.1-more-on-lists/5.1.1-using-lists-as-stacks/README.md)
- [ ] [Görev 5.1.2: Sıraya ilk gireni önce işle](tutorial/05-data-structures/5.1-more-on-lists/5.1.2-using-lists-as-queues/README.md)
- [ ] [Görev 5.1.3: Dönüştürme ve filtreyi tek ifadede kur](tutorial/05-data-structures/5.1-more-on-lists/5.1.3-list-comprehensions/README.md)
- [ ] [Görev 5.1.4: Satırlarla sütunların yerini değiştir](tutorial/05-data-structures/5.1-more-on-lists/5.1.4-nested-list-comprehensions/README.md)
- [ ] [Görev 5.1.5: Açılan öğeyi kapsayıcıdan ayır](tutorial/05-data-structures/5.1-more-on-lists/5.1.5-unpacking-in-lists-and-list-comprehensions/README.md)
- [ ] [Milestone 5.1: Bekleyen işleri iki farklı sırayla işle](tutorial/05-data-structures/5.1-more-on-lists/README.md#klasör-milestone-görevi)
- [ ] [Görev 5.2: Öğeyi silmekle adı silmeyi ayır](tutorial/05-data-structures/5.2-the-del-statement/README.md)
- [ ] [Görev 5.3: Değişmeyen kaydın içindeki listeyi izle](tutorial/05-data-structures/5.3-tuples-and-sequences/README.md)
- [ ] [Görev 5.4: İki grubun ortak ve farklı üyelerini bul](tutorial/05-data-structures/5.4-sets/README.md)
- [ ] [Görev 5.5: Anahtarın yaşam döngüsünü yönet](tutorial/05-data-structures/5.5-dictionaries/README.md)
- [ ] [Görev 5.6: Aynı veriden farklı dolaşım görünümleri üret](tutorial/05-data-structures/5.6-looping-techniques/README.md)
- [ ] [Görev 5.7: Koşulun hangi kısmına gerçekten ulaşıldığını göster](tutorial/05-data-structures/5.7-more-on-conditions/README.md)
- [ ] [Görev 5.8: Sıralamanın ilk belirleyici öğesini bul](tutorial/05-data-structures/5.8-comparing-sequences-and-other-types/README.md)
- [ ] [Milestone 5: Katılımcı kayıtlarını veri yapılarına dönüştür](tutorial/05-data-structures/README.md#klasör-milestone-görevi)

### 6. Modüller ve paketler

- [ ] [Görev 6: İşlevi başka dosyadan kullan](tutorial/06-modules/README.md)
- [ ] [Görev 6.1: İçe aktarmanın adlara ve başlangıca etkisini izle](tutorial/06-modules/6.1-more-on-modules/README.md)
- [ ] [Görev 6.1.1: Dosyanın iki giriş yolunu ayır](tutorial/06-modules/6.1-more-on-modules/6.1.1-executing-modules-as-scripts/README.md)
- [ ] [Görev 6.1.2: Yanlış modülün neden seçildiğini bul](tutorial/06-modules/6.1-more-on-modules/6.1.2-the-module-search-path/README.md)
- [ ] [Görev 6.1.3: Önbelleğin neyi hızlandırdığını ayır](tutorial/06-modules/6.1-more-on-modules/6.1.3-compiled-python-files/README.md)
- [ ] [Milestone 6.1: Hem içe aktarılan hem çalıştırılan modülü izle](tutorial/06-modules/6.1-more-on-modules/README.md#klasör-milestone-görevi)
- [ ] [Görev 6.2: Yorumlayıcının standart modülünü kullan](tutorial/06-modules/6.2-standard-modules/README.md)
- [ ] [Görev 6.3: Adları doğru kapsamda ara](tutorial/06-modules/6.3-the-dir-function/README.md)
- [ ] [Görev 6.4: Paket yolunu çağrı biçimiyle eşleştir](tutorial/06-modules/6.4-packages/README.md)
- [ ] [Görev 6.4.1: Yıldızlı aktarımın sınırını gör](tutorial/06-modules/6.4-packages/6.4.1-importing-from-a-package/README.md)
- [ ] [Görev 6.4.2: Göreli yolu paket ağacında çöz](tutorial/06-modules/6.4-packages/6.4.2-intra-package-references/README.md)
- [ ] [Milestone 6.4: Paketin dışarı açtığı adları tasarla](tutorial/06-modules/6.4-packages/README.md#klasör-milestone-görevi)
- [ ] [Milestone 6: Tekrar kullanılabilir hesap paketini teslim et](tutorial/06-modules/README.md#klasör-milestone-görevi)

### 7. Girdi, çıktı ve dosyalar

- [ ] [Görev 7.1: Aynı verinin üç gösterimini ayır](tutorial/07-input-and-output/7.1-fancier-output-formatting/README.md)
- [ ] [Görev 7.1.1: Bir satırda hizalama ve teşhis bilgisi üret](tutorial/07-input-and-output/7.1-fancier-output-formatting/7.1.1-formatted-string-literals/README.md)
- [ ] [Görev 7.1.2: Şablon alanlarını argümana bağla](tutorial/07-input-and-output/7.1-fancier-output-formatting/7.1.2-the-string-format-method/README.md)
- [ ] [Görev 7.1.3: Alan doldurmayla kesmeyi birbirinden ayır](tutorial/07-input-and-output/7.1-fancier-output-formatting/7.1.3-manual-string-formatting/README.md)
- [ ] [Görev 7.1.4: Yüzde işaretinin iki rolünü ayır](tutorial/07-input-and-output/7.1-fancier-output-formatting/7.1.4-old-string-formatting/README.md)
- [ ] [Milestone 7.1: Bir raporun verisini ve görünümünü ayrı doğrula](tutorial/07-input-and-output/7.1-fancier-output-formatting/README.md#klasör-milestone-görevi)
- [ ] [Görev 7.2: Dosya kipinin veriye etkisini seç](tutorial/07-input-and-output/7.2-reading-and-writing-files/README.md)
- [ ] [Görev 7.2.1: Dosya imlecini ve satır sonunu izle](tutorial/07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md)
- [ ] [Görev 7.2.2: Yapılandırılmış veriyi dosyadan geri getir](tutorial/07-input-and-output/7.2-reading-and-writing-files/7.2.2-saving-structured-data-with-json/README.md)
- [ ] [Milestone 7.2: Dosya yaşam döngüsünü veriyle birlikte tamamla](tutorial/07-input-and-output/7.2-reading-and-writing-files/README.md#klasör-milestone-görevi)
- [ ] [Milestone 7: Bir veri dosyasından okunabilir rapor çıkar](tutorial/07-input-and-output/README.md#klasör-milestone-görevi)

### 8. Hatalar ve exception yönetimi

- [ ] [Görev 8.1: Okun işaret ettiği yerden asıl hataya git](tutorial/08-errors-and-exceptions/8.1-syntax-errors/README.md)
- [ ] [Görev 8.2: Hata izinden bozulan işlemi bul](tutorial/08-errors-and-exceptions/8.2-exceptions/README.md)
- [ ] [Görev 8.3: Yalnız beklediğin hatayı yakala](tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md)
- [ ] [Görev 8.4: Hatayı üret ve üst çağırana aktar](tutorial/08-errors-and-exceptions/8.4-raising-exceptions/README.md)
- [ ] [Görev 8.5: Hata çevirisinin nedenini görünür kıl](tutorial/08-errors-and-exceptions/8.5-exception-chaining/README.md)
- [ ] [Görev 8.6: Alan hatasını doğru exception ailesine yerleştir](tutorial/08-errors-and-exceptions/8.6-user-defined-exceptions/README.md)
- [ ] [Görev 8.7: Temizliği bütün çıkış yollarında izle](tutorial/08-errors-and-exceptions/8.7-defining-clean-up-actions/README.md)
- [ ] [Görev 8.8: Blok hatayla bitse de dosyayı kapat](tutorial/08-errors-and-exceptions/8.8-predefined-clean-up-actions/README.md)
- [ ] [Görev 8.9: Toplu hatadan yalnız seçilen türleri işle](tutorial/08-errors-and-exceptions/8.9-raising-and-handling-multiple-unrelated-exceptions/README.md)
- [ ] [Görev 8.10: Hatanın kimliğini koruyup bağlam ekle](tutorial/08-errors-and-exceptions/8.10-enriching-exceptions-with-notes/README.md)
- [ ] [Milestone 8: Kötü kayıtları kaybetmeden içe al](tutorial/08-errors-and-exceptions/README.md#klasör-milestone-görevi)

### 9. Sınıflar, iteratorler ve generatorler

- [ ] [Görev 9: Nesnenin veriyle davranışı nasıl birleştirdiğini çiz](tutorial/09-classes/README.md)
- [ ] [Görev 9.1: İki adın ortak nesneye etkisini izle](tutorial/09-classes/9.1-a-word-about-names-and-objects/README.md)
- [ ] [Görev 9.2: Bir adı nerede aradığını ve nereye yazdığını ayır](tutorial/09-classes/9.2-python-scopes-and-namespaces/README.md)
- [ ] [Görev 9.2.1: Kapsam izini tek değişiklikle yeniden çıkar](tutorial/09-classes/9.2-python-scopes-and-namespaces/9.2.1-scopes-and-namespaces-example/README.md)
- [ ] [Milestone 9.2: Kapsam geçişi](tutorial/09-classes/9.2-python-scopes-and-namespaces/README.md#klasör-milestone-görevi)
- [ ] [Görev 9.3.1: Sınıf gövdesinin ne zaman yürüdüğünü göster](tutorial/09-classes/9.3-a-first-look-at-classes/9.3.1-class-definition-syntax/README.md)
- [ ] [Görev 9.3.2: Sınıftan başlangıç durumu olan nesne üret](tutorial/09-classes/9.3-a-first-look-at-classes/9.3.2-class-objects/README.md)
- [ ] [Görev 9.3.3: Örnek niteliğinin oluşmasını ve silinmesini izle](tutorial/09-classes/9.3-a-first-look-at-classes/9.3.3-instance-objects/README.md)
- [ ] [Görev 9.3.4: Kaydedilen metodun hangi nesneye bağlı kaldığını göster](tutorial/09-classes/9.3-a-first-look-at-classes/9.3.4-method-objects/README.md)
- [ ] [Görev 9.3.5: Örneklere ait listeyi paylaşmaktan kurtar](tutorial/09-classes/9.3-a-first-look-at-classes/9.3.5-class-and-instance-variables/README.md)
- [ ] [Milestone 9.3: Birbirinden bağımsız durum taşıyan iki nesne kur](tutorial/09-classes/9.3-a-first-look-at-classes/README.md#klasör-milestone-görevi)
- [ ] [Görev 9.4: Nitelik aramasının önceliğini izle](tutorial/09-classes/9.4-random-remarks/README.md)
- [ ] [Görev 9.5: Üst metodun çağırdığı alt davranışı izle](tutorial/09-classes/9.5-inheritance/README.md)
- [ ] [Görev 9.5.1: Elmas hiyerarşide arama sırasını çıkar](tutorial/09-classes/9.5-inheritance/9.5.1-multiple-inheritance/README.md)
- [ ] [Milestone 9.5: Kalıtım aramasını durumdan ayrı izle](tutorial/09-classes/9.5-inheritance/README.md#klasör-milestone-görevi)
- [ ] [Görev 9.6: Ad çakışmasını erişim yasağından ayır](tutorial/09-classes/9.6-private-variables/README.md)
- [ ] [Görev 9.7: Kayıt nesnesiyle metot bağını göster](tutorial/09-classes/9.7-odds-and-ends/README.md)
- [ ] [Görev 9.8: Tükenen iteratorü yeniden kullanmayı dene](tutorial/09-classes/9.8-iterators/README.md)
- [ ] [Görev 9.9: Durumu yield aralarında koru](tutorial/09-classes/9.9-generators/README.md)
- [ ] [Görev 9.10: Liste üretmeden hesapla ve tüketimi izle](tutorial/09-classes/9.10-generator-expressions/README.md)
- [ ] [Milestone 9: Durumu olan, dolaşılabilen küçük bir koleksiyon yap](tutorial/09-classes/README.md#klasör-milestone-görevi)

### 10. Standart kütüphane

- [ ] [Görev 10.1: Dosya işlemini doğru arayüzle eşleştir](tutorial/10-brief-tour-of-the-standard-library/10.1-operating-system-interface/README.md)
- [ ] [Görev 10.2: Dosya adlarını kalıpla seç](tutorial/10-brief-tour-of-the-standard-library/10.2-file-wildcards/README.md)
- [ ] [Görev 10.3: Komut satırının sözleşmesini sınırda kontrol et](tutorial/10-brief-tour-of-the-standard-library/10.3-command-line-arguments/README.md)
- [ ] [Görev 10.4: Hata mesajıyla normal çıktıyı ayır](tutorial/10-brief-tour-of-the-standard-library/10.4-error-output-redirection-and-program-termination/README.md)
- [ ] [Görev 10.5: Örnekteki kalıpla eşleşeni ve değişeni bul](tutorial/10-brief-tour-of-the-standard-library/10.5-string-pattern-matching/README.md)
- [ ] [Görev 10.6: Kesin hesapla rastgele seçimin ölçütlerini ayır](tutorial/10-brief-tour-of-the-standard-library/10.6-mathematics/README.md)
- [ ] [Görev 10.7: Ağ örneğinin veri ve yan etki izini çıkar](tutorial/10-brief-tour-of-the-standard-library/10.7-internet-access/README.md)
- [ ] [Görev 10.8: Tarih farkını sabit girdilerle doğrula](tutorial/10-brief-tour-of-the-standard-library/10.8-dates-and-times/README.md)
- [ ] [Görev 10.9: Sıkıştırılmış verinin geri dönebildiğini kanıtla](tutorial/10-brief-tour-of-the-standard-library/10.9-data-compression/README.md)
- [ ] [Görev 10.10: Hızı ölçerken sonucu garanti etme](tutorial/10-brief-tour-of-the-standard-library/10.10-performance-measurement/README.md)
- [ ] [Görev 10.11: Davranış bozulunca testin yakaladığını göster](tutorial/10-brief-tour-of-the-standard-library/10.11-quality-control/README.md)
- [ ] [Görev 10.12: İhtiyaca uygun standart modülü seç](tutorial/10-brief-tour-of-the-standard-library/10.12-batteries-included/README.md)
- [ ] [Milestone 10: Küçük bir yerel rapor aracını sınır durumlarıyla doğrula](tutorial/10-brief-tour-of-the-standard-library/README.md#klasör-milestone-görevi)

### 11. Standart kütüphane: ileri araçlar

- [ ] [Görev 11.1: Görünümü verinin kendisinden ayır](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.1-output-formatting/README.md)
- [ ] [Görev 11.2: Eksik alanı tamamlamadan şablonu koru](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.2-templating/README.md)
- [ ] [Görev 11.3: Binary kayıttaki sınırları hesapla](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.3-working-with-binary-data-record-layouts/README.md)
- [ ] [Görev 11.4: Eşzamanlı akışta yalnız garanti edilen sırayı yaz](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.4-multi-threading/README.md)
- [ ] [Görev 11.5: Görünmeyen kayıtla çalışmayan kodu karıştırma](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.5-logging/README.md)
- [ ] [Görev 11.6: İzleyen tablonun nesneyi yaşatıp yaşatmadığını göster](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.6-weak-references/README.md)
- [ ] [Görev 11.7: Veri yapısını erişim ihtiyacına göre seç](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.7-tools-for-working-with-lists/README.md)
- [ ] [Görev 11.8: Ondalık girdiyi nasıl oluşturduğunu karşılaştır](tutorial/11-brief-tour-of-the-standard-library-part-ii/11.8-decimal-floating-point-arithmetic/README.md)
- [ ] [Milestone 11: Öncelikli yerel işlerin raporunu üret](tutorial/11-brief-tour-of-the-standard-library-part-ii/README.md#klasör-milestone-görevi)

### 12. Sanal ortamlar ve paket yönetimi

- [ ] [Görev 12.1: Çakışan bağımlılığı iki ortamda ayır](tutorial/12-virtual-environments-and-packages/12.1-introduction/README.md)
- [ ] [Görev 12.2: Oluşturma ile etkinleştirmeyi ayır](tutorial/12-virtual-environments-and-packages/12.2-creating-virtual-environments/README.md)
- [ ] [Görev 12.3: Paket değişiminin planını ve kanıtını yaz](tutorial/12-virtual-environments-and-packages/12.3-managing-packages-with-pip/README.md)
- [ ] [Milestone 12: İki uygulamanın bağımlılık planını yeniden üretilebilir yap](tutorial/12-virtual-environments-and-packages/README.md#klasör-milestone-görevi)

### 13. Devam kaynaklarını seçme

- [ ] [Görev 13: Soruyu doğru belgeye yönlendir](tutorial/13-what-now/README.md)

### 14. Etkileşimli giriş ve geçmiş

- [ ] [Görev 14: Düzenleme desteğini Python dilinden ayır](tutorial/14-interactive-input-editing-and-history-substitution/README.md)
- [ ] [Görev 14.1: Tamamlama kaynağını ve geçmişi tanı](tutorial/14-interactive-input-editing-and-history-substitution/14.1-tab-completion-and-history-editing/README.md)
- [ ] [Görev 14.2: Alternatif arayüzü ihtiyaca göre seç](tutorial/14-interactive-input-editing-and-history-substitution/14.2-alternatives-to-the-interactive-interpreter/README.md)
- [ ] [Milestone 14: Arayüz sorununu öğrenme eksikliğinden ayır](tutorial/14-interactive-input-editing-and-history-substitution/README.md#klasör-milestone-görevi)

### 15. Float temsili ve doğrulama

- [ ] [Görev 15: Gösterimi gerçek sayı değeriyle karıştırma](tutorial/15-floating-point-arithmetic-issues-and-limitations/README.md)
- [ ] [Görev 15.1: Saklanan yaklaşık kesrin neden yukarıda kaldığını kanıtla](tutorial/15-floating-point-arithmetic-issues-and-limitations/15.1-representation-error/README.md)
- [ ] [Milestone 15: Yaklaşık değer için doğrulama ölçütünü seç](tutorial/15-floating-point-arithmetic-issues-and-limitations/README.md#klasör-milestone-görevi)

### 16. Yorumlayıcı eki

- [ ] [Görev 16.1: REPL özelliklerini sürüm koşuluyla oku](tutorial/16-appendix/16.1-interactive-mode/README.md)
- [ ] [Görev 16.1.1: Aynı hatanın betikle oturumda farklı sonunu göster](tutorial/16-appendix/16.1-interactive-mode/16.1.1-error-handling/README.md)
- [ ] [Görev 16.1.2: Çalıştırılabilir betiğin başlığını doğrula](tutorial/16-appendix/16.1-interactive-mode/16.1.2-executable-python-scripts/README.md)
- [ ] [Görev 16.1.3: Başlangıç dosyasının hangi oturumda çalışacağını çıkar](tutorial/16-appendix/16.1-interactive-mode/16.1.3-the-interactive-startup-file/README.md)
- [ ] [Görev 16.1.4: Kullanıcı ve sistem özelleştirmesinin kapsamını ayır](tutorial/16-appendix/16.1-interactive-mode/16.1.4-the-customization-modules/README.md)
- [ ] [Milestone 16.1: Yorumlayıcı başlangıcını değiştirmeden teşhis et](tutorial/16-appendix/16.1-interactive-mode/README.md#klasör-milestone-görevi)
- [ ] [Milestone 16: Yorumlayıcı ekini tamamlama](tutorial/16-appendix/README.md#klasör-milestone-görevi)

### Tutorial sonu projesi

- [ ] [Milestone Tutorial: Python ile yerel ve sınanabilir bir veri akışı kur](tutorial/README.md#klasör-milestone-görevi)

## Language reference: dolu import bölümleri

Bu rota tutorial bittikten sonra gelir. Diğer referans bölümlerinin çoğu yalnız iskelettir.

### 5. Import sistemine giriş

- [ ] [Görev 5: Modülü bulmayla ad bağlamayı ayır](language-reference/05-the-import-system/README.md)

### 5.1. Dinamik import

- [ ] [Görev 5.1: Dinamik adla basit modül al](language-reference/05-the-import-system/5.1-importlib/README.md)

### 5.2. Paket türleri

- [ ] [Görev 5.2: Paket hiyerarşisini nesne modeliyle eşleştir](language-reference/05-the-import-system/5.2-packages/README.md)
- [ ] [Görev 5.2.1: Paket başlatıcılarının yürütme sırasını çıkar](language-reference/05-the-import-system/5.2-packages/5.2.1-regular-packages/README.md)
- [ ] [Görev 5.2.2: Ayrı konumlardan tek namespace paketi kurulduğunu izle](language-reference/05-the-import-system/5.2-packages/5.2.2-namespace-packages/README.md)
- [ ] [Milestone 5.2: İki paket türünü aynı ağaçta çöz](language-reference/05-the-import-system/5.2-packages/README.md#klasör-milestone-görevi)

### 5.3. Modül arama

- [ ] [Görev 5.3: Noktalı importu sırayla çöz](language-reference/05-the-import-system/5.3-searching/README.md)
- [ ] [Görev 5.3.1: Eksik cache kaydıyla None kaydını ayır](language-reference/05-the-import-system/5.3-searching/5.3.1-the-module-cache/README.md)
- [ ] [Görev 5.3.2: Bulucuyla yükleyicinin teslim sınırını çiz](language-reference/05-the-import-system/5.3-searching/5.3.2-finders-and-loaders/README.md)
- [ ] [Görev 5.3.3: Hookun hangi aşamaya girdiğini seç](language-reference/05-the-import-system/5.3-searching/5.3.3-import-hooks/README.md)
- [ ] [Görev 5.3.4: Meta path taramasının devam ve durma koşullarını izle](language-reference/05-the-import-system/5.3-searching/5.3.4-the-meta-path/README.md)
- [ ] [Milestone 5.3: Arama kararını cacheten spec teslimine kadar izle](language-reference/05-the-import-system/5.3-searching/README.md#klasör-milestone-görevi)

### 5.4. Modül yükleme

- [ ] [Görev 5.4: Yükleme hatasında yalnız başarısız modülü çıkar](language-reference/05-the-import-system/5.4-loading/README.md)
- [ ] [Görev 5.4.1: Loaderın sorumluluğunu makineninkinden ayır](language-reference/05-the-import-system/5.4-loading/5.4.1-loaders/README.md)
- [ ] [Görev 5.4.2: Alt modülün iki erişim yolunun aynı nesneye çıktığını göster](language-reference/05-the-import-system/5.4-loading/5.4.2-submodules/README.md)
- [ ] [Görev 5.4.3: Specin hangi sınırdan bilgi taşıdığını açıkla](language-reference/05-the-import-system/5.4-loading/5.4.3-module-specs/README.md)
- [ ] [Görev 5.4.4: Paket aramasının kapsamını daralt](language-reference/05-the-import-system/5.4-loading/5.4.4-path-attributes-on-modules/README.md)
- [ ] [Görev 5.4.5: Modül temsilinin yedek bilgi sırasını çıkar](language-reference/05-the-import-system/5.4-loading/5.4.5-module-reprs/README.md)
- [ ] [Görev 5.4.6: Bytecode geçerliliğini politika bazında ayır](language-reference/05-the-import-system/5.4-loading/5.4.6-cached-bytecode-invalidation/README.md)
- [ ] [Milestone 5.4: Başarısız importun geride bıraktığı durumu değerlendir](language-reference/05-the-import-system/5.4-loading/README.md#klasör-milestone-görevi)

### 5.5. Yol tabanlı finder

- [ ] [Görev 5.5: İki finder türünü farklı katmanlara yerleştir](language-reference/05-the-import-system/5.5-the-path-based-finder/README.md)
- [ ] [Görev 5.5.1: Finder cacheini modül cacheinden ayır](language-reference/05-the-import-system/5.5-the-path-based-finder/5.5.1-path-entry-finders/README.md)
- [ ] [Görev 5.5.2: Path finder protokolünü doğru imzayla oku](language-reference/05-the-import-system/5.5-the-path-based-finder/5.5.2-path-entry-finder-protocol/README.md)
- [ ] [Milestone 5.5: Bir yol girdisini seçme izini tamamla](language-reference/05-the-import-system/5.5-the-path-based-finder/README.md#klasör-milestone-görevi)

### 5.6. Import sistemini değiştirme

- [ ] [Görev 5.6: Aramayı sürdürmekle reddetmeyi ayır](language-reference/05-the-import-system/5.6-replacing-the-standard-import-system/README.md)

### 5.7. Göreli importlar

- [ ] [Görev 5.7: Göreli importu mutlak ada çöz](language-reference/05-the-import-system/5.7-package-relative-imports/README.md)

### 5.8. Ana modülün başlatılması

- [ ] [Görev 5.8: Ana modülü built-in modülle karıştırma](language-reference/05-the-import-system/5.8-special-considerations-for-main/README.md)
- [ ] [Görev 5.8.1: Çalıştırma biçimine göre ana specini belirle](language-reference/05-the-import-system/5.8-special-considerations-for-main/5.8.1-main-spec/README.md)
- [ ] [Milestone 5.8: Ana modül geçişi](language-reference/05-the-import-system/5.8-special-considerations-for-main/README.md#klasör-milestone-görevi)

### Import sistemi sonu kontrolü

- [ ] [Milestone 5: Import sorununu doğru katmanda teşhis et](language-reference/05-the-import-system/README.md#klasör-milestone-görevi)

## Anlatımı olmayan veya yalnız yönlendiren bölümler

Başlık ve klasör varlığı öğrenilmiş içerik değildir. Aşağıdakilerde eksik bir konuyu öğrenilmiş varsayan görev bulunmaz. Dolu alt bölüme geçişler yukarıdaki sırada yer alır.

<details>
<summary>Bölüm bazında kapsam dökümü</summary>

- Harita/kaynakça: [t:root](tutorial/README.md)
- Harita/kaynakça: [t:2](tutorial/02-using-the-python-interpreter/README.md)
- Harita/kaynakça: [t:2.2](tutorial/02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/README.md)
- Harita/kaynakça: [t:3.1](tutorial/03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/README.md)
- Harita/kaynakça: [t:4](tutorial/04-more-control-flow-tools/README.md)
- Harita/kaynakça: [t:4.9](tutorial/04-more-control-flow-tools/4.9-more-on-defining-functions/README.md)
- Harita/kaynakça: [t:5](tutorial/05-data-structures/README.md)
- Harita/kaynakça: [t:7](tutorial/07-input-and-output/README.md)
- Harita/kaynakça: [t:9.3](tutorial/09-classes/9.3-a-first-look-at-classes/README.md)
- Harita/kaynakça: [t:10](tutorial/10-brief-tour-of-the-standard-library/README.md)
- Harita/kaynakça: [t:11](tutorial/11-brief-tour-of-the-standard-library-part-ii/README.md)
- Harita/kaynakça: [t:12](tutorial/12-virtual-environments-and-packages/README.md)
- Harita/kaynakça: [t:16](tutorial/16-appendix/README.md)
- Harita/kaynakça: [r:root](language-reference/README.md)
- Anlatım bekleniyor: [r:1](language-reference/01-introduction/README.md)
- Anlatım bekleniyor: [r:1.1](language-reference/01-introduction/1.1-alternate-implementations/README.md)
- Anlatım bekleniyor: [r:1.2](language-reference/01-introduction/1.2-notation/README.md)
- Anlatım bekleniyor: [r:1.2.1](language-reference/01-introduction/1.2-notation/1.2.1-lexical-and-syntactic-definitions/README.md)
- Anlatım bekleniyor: [r:2](language-reference/02-lexical-analysis/README.md)
- Anlatım bekleniyor: [r:2.1](language-reference/02-lexical-analysis/2.1-line-structure/README.md)
- Anlatım bekleniyor: [r:2.1.1](language-reference/02-lexical-analysis/2.1-line-structure/2.1.1-logical-lines/README.md)
- Anlatım bekleniyor: [r:2.1.2](language-reference/02-lexical-analysis/2.1-line-structure/2.1.2-physical-lines/README.md)
- Anlatım bekleniyor: [r:2.1.3](language-reference/02-lexical-analysis/2.1-line-structure/2.1.3-comments/README.md)
- Anlatım bekleniyor: [r:2.1.4](language-reference/02-lexical-analysis/2.1-line-structure/2.1.4-encoding-declarations/README.md)
- Anlatım bekleniyor: [r:2.1.5](language-reference/02-lexical-analysis/2.1-line-structure/2.1.5-explicit-line-joining/README.md)
- Anlatım bekleniyor: [r:2.1.6](language-reference/02-lexical-analysis/2.1-line-structure/2.1.6-implicit-line-joining/README.md)
- Anlatım bekleniyor: [r:2.1.7](language-reference/02-lexical-analysis/2.1-line-structure/2.1.7-blank-lines/README.md)
- Anlatım bekleniyor: [r:2.1.8](language-reference/02-lexical-analysis/2.1-line-structure/2.1.8-indentation/README.md)
- Anlatım bekleniyor: [r:2.1.9](language-reference/02-lexical-analysis/2.1-line-structure/2.1.9-whitespace-between-tokens/README.md)
- Anlatım bekleniyor: [r:2.1.10](language-reference/02-lexical-analysis/2.1-line-structure/2.1.10-end-marker/README.md)
- Anlatım bekleniyor: [r:2.2](language-reference/02-lexical-analysis/2.2-other-tokens/README.md)
- Anlatım bekleniyor: [r:2.3](language-reference/02-lexical-analysis/2.3-names-identifiers-and-keywords/README.md)
- Anlatım bekleniyor: [r:2.3.1](language-reference/02-lexical-analysis/2.3-names-identifiers-and-keywords/2.3.1-keywords/README.md)
- Anlatım bekleniyor: [r:2.3.2](language-reference/02-lexical-analysis/2.3-names-identifiers-and-keywords/2.3.2-soft-keywords/README.md)
- Anlatım bekleniyor: [r:2.3.3](language-reference/02-lexical-analysis/2.3-names-identifiers-and-keywords/2.3.3-reserved-classes-of-identifiers/README.md)
- Anlatım bekleniyor: [r:2.3.4](language-reference/02-lexical-analysis/2.3-names-identifiers-and-keywords/2.3.4-non-ascii-characters-in-names/README.md)
- Anlatım bekleniyor: [r:2.4](language-reference/02-lexical-analysis/2.4-literals/README.md)
- Anlatım bekleniyor: [r:2.5](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/README.md)
- Anlatım bekleniyor: [r:2.5.1](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.1-triple-quoted-strings/README.md)
- Anlatım bekleniyor: [r:2.5.2](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.2-string-prefixes/README.md)
- Anlatım bekleniyor: [r:2.5.3](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.3-formal-grammar/README.md)
- Anlatım bekleniyor: [r:2.5.4](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/README.md)
- Anlatım bekleniyor: [r:2.5.4.1](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.1-ignored-end-of-line/README.md)
- Anlatım bekleniyor: [r:2.5.4.2](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.2-escaped-characters/README.md)
- Anlatım bekleniyor: [r:2.5.4.3](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.3-octal-character/README.md)
- Anlatım bekleniyor: [r:2.5.4.4](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.4-hexadecimal-character/README.md)
- Anlatım bekleniyor: [r:2.5.4.5](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.5-named-unicode-character/README.md)
- Anlatım bekleniyor: [r:2.5.4.6](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.6-hexadecimal-unicode-characters/README.md)
- Anlatım bekleniyor: [r:2.5.4.7](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.4-escape-sequences/2.5.4.7-unrecognized-escape-sequences/README.md)
- Anlatım bekleniyor: [r:2.5.5](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.5-bytes-literals/README.md)
- Anlatım bekleniyor: [r:2.5.6](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.6-raw-string-literals/README.md)
- Anlatım bekleniyor: [r:2.5.7](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.7-f-strings/README.md)
- Anlatım bekleniyor: [r:2.5.8](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.8-t-strings/README.md)
- Anlatım bekleniyor: [r:2.5.9](language-reference/02-lexical-analysis/2.5-string-and-bytes-literals/2.5.9-formal-grammar-for-f-strings/README.md)
- Anlatım bekleniyor: [r:2.6](language-reference/02-lexical-analysis/2.6-numeric-literals/README.md)
- Anlatım bekleniyor: [r:2.6.1](language-reference/02-lexical-analysis/2.6-numeric-literals/2.6.1-integer-literals/README.md)
- Anlatım bekleniyor: [r:2.6.2](language-reference/02-lexical-analysis/2.6-numeric-literals/2.6.2-floating-point-literals/README.md)
- Anlatım bekleniyor: [r:2.6.3](language-reference/02-lexical-analysis/2.6-numeric-literals/2.6.3-imaginary-literals/README.md)
- Anlatım bekleniyor: [r:2.7](language-reference/02-lexical-analysis/2.7-operators-and-delimiters/README.md)
- Anlatım bekleniyor: [r:3](language-reference/03-data-model/README.md)
- Anlatım bekleniyor: [r:3.1](language-reference/03-data-model/3.1-objects-values-and-types/README.md)
- Anlatım bekleniyor: [r:3.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/README.md)
- Anlatım bekleniyor: [r:3.2.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.1-none/README.md)
- Anlatım bekleniyor: [r:3.2.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.2-notimplemented/README.md)
- Anlatım bekleniyor: [r:3.2.3](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.3-ellipsis/README.md)
- Anlatım bekleniyor: [r:3.2.4](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.4-numbers-number/README.md)
- Anlatım bekleniyor: [r:3.2.4.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.4-numbers-number/3.2.4.1-numbers-integral/README.md)
- Anlatım bekleniyor: [r:3.2.4.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.4-numbers-number/3.2.4.2-numbers-real-float/README.md)
- Anlatım bekleniyor: [r:3.2.4.3](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.4-numbers-number/3.2.4.3-numbers-complex-complex/README.md)
- Anlatım bekleniyor: [r:3.2.5](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.5-sequences/README.md)
- Anlatım bekleniyor: [r:3.2.5.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.5-sequences/3.2.5.1-immutable-sequences/README.md)
- Anlatım bekleniyor: [r:3.2.5.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.5-sequences/3.2.5.2-mutable-sequences/README.md)
- Anlatım bekleniyor: [r:3.2.6](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.6-set-types/README.md)
- Anlatım bekleniyor: [r:3.2.7](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.7-mappings/README.md)
- Anlatım bekleniyor: [r:3.2.7.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.7-mappings/3.2.7.1-dictionaries/README.md)
- Anlatım bekleniyor: [r:3.2.7.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.7-mappings/3.2.7.2-frozen-dictionaries/README.md)
- Anlatım bekleniyor: [r:3.2.8](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/README.md)
- Anlatım bekleniyor: [r:3.2.8.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.1-user-defined-functions/README.md)
- Anlatım bekleniyor: [r:3.2.8.1.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.1-user-defined-functions/3.2.8.1.1-special-read-only-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.8.1.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.1-user-defined-functions/3.2.8.1.2-special-writable-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.8.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.2-instance-methods/README.md)
- Anlatım bekleniyor: [r:3.2.8.3](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.3-generator-functions/README.md)
- Anlatım bekleniyor: [r:3.2.8.4](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.4-coroutine-functions/README.md)
- Anlatım bekleniyor: [r:3.2.8.5](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.5-asynchronous-generator-functions/README.md)
- Anlatım bekleniyor: [r:3.2.8.6](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.6-built-in-functions/README.md)
- Anlatım bekleniyor: [r:3.2.8.7](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.7-built-in-methods/README.md)
- Anlatım bekleniyor: [r:3.2.8.8](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.8-classes/README.md)
- Anlatım bekleniyor: [r:3.2.8.9](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.8-callable-types/3.2.8.9-class-instances/README.md)
- Anlatım bekleniyor: [r:3.2.9](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.9-modules/README.md)
- Anlatım bekleniyor: [r:3.2.9.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.9-modules/3.2.9.1-import-related-attributes-on-module-objects/README.md)
- Anlatım bekleniyor: [r:3.2.9.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.9-modules/3.2.9.2-other-writable-attributes-on-module-objects/README.md)
- Anlatım bekleniyor: [r:3.2.9.3](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.9-modules/3.2.9.3-module-dictionaries/README.md)
- Anlatım bekleniyor: [r:3.2.10](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.10-custom-classes/README.md)
- Anlatım bekleniyor: [r:3.2.10.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.10-custom-classes/3.2.10.1-special-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.10.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.10-custom-classes/3.2.10.2-special-methods/README.md)
- Anlatım bekleniyor: [r:3.2.11](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.11-class-instances/README.md)
- Anlatım bekleniyor: [r:3.2.11.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.11-class-instances/3.2.11.1-special-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.12](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.12-i-o-objects-also-known-as-file-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/README.md)
- Anlatım bekleniyor: [r:3.2.13.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.1-code-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13.1.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.1-code-objects/3.2.13.1.1-special-read-only-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.13.1.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.1-code-objects/3.2.13.1.2-methods-on-code-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.2-frame-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13.2.1](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.2-frame-objects/3.2.13.2.1-special-read-only-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.13.2.2](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.2-frame-objects/3.2.13.2.2-special-writable-attributes/README.md)
- Anlatım bekleniyor: [r:3.2.13.2.3](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.2-frame-objects/3.2.13.2.3-frame-object-methods/README.md)
- Anlatım bekleniyor: [r:3.2.13.3](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.3-traceback-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13.4](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.4-slice-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13.5](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.5-static-method-objects/README.md)
- Anlatım bekleniyor: [r:3.2.13.6](language-reference/03-data-model/3.2-the-standard-type-hierarchy/3.2.13-internal-types/3.2.13.6-class-method-objects/README.md)
- Anlatım bekleniyor: [r:3.3](language-reference/03-data-model/3.3-special-method-names/README.md)
- Anlatım bekleniyor: [r:3.3.1](language-reference/03-data-model/3.3-special-method-names/3.3.1-basic-customization/README.md)
- Anlatım bekleniyor: [r:3.3.2](language-reference/03-data-model/3.3-special-method-names/3.3.2-customizing-attribute-access/README.md)
- Anlatım bekleniyor: [r:3.3.2.1](language-reference/03-data-model/3.3-special-method-names/3.3.2-customizing-attribute-access/3.3.2.1-customizing-module-attribute-access/README.md)
- Anlatım bekleniyor: [r:3.3.2.2](language-reference/03-data-model/3.3-special-method-names/3.3.2-customizing-attribute-access/3.3.2.2-implementing-descriptors/README.md)
- Anlatım bekleniyor: [r:3.3.2.3](language-reference/03-data-model/3.3-special-method-names/3.3.2-customizing-attribute-access/3.3.2.3-invoking-descriptors/README.md)
- Anlatım bekleniyor: [r:3.3.2.4](language-reference/03-data-model/3.3-special-method-names/3.3.2-customizing-attribute-access/3.3.2.4-slots/README.md)
- Anlatım bekleniyor: [r:3.3.3](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/README.md)
- Anlatım bekleniyor: [r:3.3.3.1](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.1-metaclasses/README.md)
- Anlatım bekleniyor: [r:3.3.3.2](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.2-resolving-mro-entries/README.md)
- Anlatım bekleniyor: [r:3.3.3.3](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.3-determining-the-appropriate-metaclass/README.md)
- Anlatım bekleniyor: [r:3.3.3.4](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.4-preparing-the-class-namespace/README.md)
- Anlatım bekleniyor: [r:3.3.3.5](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.5-executing-the-class-body/README.md)
- Anlatım bekleniyor: [r:3.3.3.6](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.6-creating-the-class-object/README.md)
- Anlatım bekleniyor: [r:3.3.3.7](language-reference/03-data-model/3.3-special-method-names/3.3.3-customizing-class-creation/3.3.3.7-uses-for-metaclasses/README.md)
- Anlatım bekleniyor: [r:3.3.4](language-reference/03-data-model/3.3-special-method-names/3.3.4-customizing-instance-and-subclass-checks/README.md)
- Anlatım bekleniyor: [r:3.3.5](language-reference/03-data-model/3.3-special-method-names/3.3.5-emulating-generic-types/README.md)
- Anlatım bekleniyor: [r:3.3.5.1](language-reference/03-data-model/3.3-special-method-names/3.3.5-emulating-generic-types/3.3.5.1-the-purpose-of-class-getitem/README.md)
- Anlatım bekleniyor: [r:3.3.5.2](language-reference/03-data-model/3.3-special-method-names/3.3.5-emulating-generic-types/3.3.5.2-class-getitem-versus-getitem/README.md)
- Anlatım bekleniyor: [r:3.3.6](language-reference/03-data-model/3.3-special-method-names/3.3.6-emulating-callable-objects/README.md)
- Anlatım bekleniyor: [r:3.3.7](language-reference/03-data-model/3.3-special-method-names/3.3.7-emulating-container-types/README.md)
- Anlatım bekleniyor: [r:3.3.8](language-reference/03-data-model/3.3-special-method-names/3.3.8-emulating-numeric-types/README.md)
- Anlatım bekleniyor: [r:3.3.9](language-reference/03-data-model/3.3-special-method-names/3.3.9-with-statement-context-managers/README.md)
- Anlatım bekleniyor: [r:3.3.10](language-reference/03-data-model/3.3-special-method-names/3.3.10-customizing-positional-arguments-in-class-pattern-matching/README.md)
- Anlatım bekleniyor: [r:3.3.11](language-reference/03-data-model/3.3-special-method-names/3.3.11-emulating-buffer-types/README.md)
- Anlatım bekleniyor: [r:3.3.12](language-reference/03-data-model/3.3-special-method-names/3.3.12-annotations/README.md)
- Anlatım bekleniyor: [r:3.3.13](language-reference/03-data-model/3.3-special-method-names/3.3.13-special-method-lookup/README.md)
- Anlatım bekleniyor: [r:3.4](language-reference/03-data-model/3.4-coroutines/README.md)
- Anlatım bekleniyor: [r:3.4.1](language-reference/03-data-model/3.4-coroutines/3.4.1-awaitable-objects/README.md)
- Anlatım bekleniyor: [r:3.4.2](language-reference/03-data-model/3.4-coroutines/3.4.2-coroutine-objects/README.md)
- Anlatım bekleniyor: [r:3.4.3](language-reference/03-data-model/3.4-coroutines/3.4.3-asynchronous-iterators/README.md)
- Anlatım bekleniyor: [r:3.4.4](language-reference/03-data-model/3.4-coroutines/3.4.4-asynchronous-context-managers/README.md)
- Anlatım bekleniyor: [r:4](language-reference/04-execution-model/README.md)
- Anlatım bekleniyor: [r:4.1](language-reference/04-execution-model/4.1-structure-of-a-program/README.md)
- Anlatım bekleniyor: [r:4.2](language-reference/04-execution-model/4.2-naming-and-binding/README.md)
- Anlatım bekleniyor: [r:4.2.1](language-reference/04-execution-model/4.2-naming-and-binding/4.2.1-binding-of-names/README.md)
- Anlatım bekleniyor: [r:4.2.2](language-reference/04-execution-model/4.2-naming-and-binding/4.2.2-resolution-of-names/README.md)
- Anlatım bekleniyor: [r:4.2.3](language-reference/04-execution-model/4.2-naming-and-binding/4.2.3-annotation-scopes/README.md)
- Anlatım bekleniyor: [r:4.2.4](language-reference/04-execution-model/4.2-naming-and-binding/4.2.4-lazy-evaluation/README.md)
- Anlatım bekleniyor: [r:4.2.5](language-reference/04-execution-model/4.2-naming-and-binding/4.2.5-builtins-and-restricted-execution/README.md)
- Anlatım bekleniyor: [r:4.2.6](language-reference/04-execution-model/4.2-naming-and-binding/4.2.6-interaction-with-dynamic-features/README.md)
- Anlatım bekleniyor: [r:4.3](language-reference/04-execution-model/4.3-exceptions/README.md)
- Anlatım bekleniyor: [r:4.4](language-reference/04-execution-model/4.4-runtime-components/README.md)
- Anlatım bekleniyor: [r:4.4.1](language-reference/04-execution-model/4.4-runtime-components/4.4.1-general-computing-model/README.md)
- Anlatım bekleniyor: [r:4.4.2](language-reference/04-execution-model/4.4-runtime-components/4.4.2-python-runtime-model/README.md)
- Harita/kaynakça: [r:5.9](language-reference/05-the-import-system/5.9-references/README.md)
- Anlatım bekleniyor: [r:6](language-reference/06-expressions/README.md)
- Anlatım bekleniyor: [r:6.1](language-reference/06-expressions/6.1-arithmetic-conversions/README.md)
- Anlatım bekleniyor: [r:6.2](language-reference/06-expressions/6.2-atoms/README.md)
- Anlatım bekleniyor: [r:6.2.1](language-reference/06-expressions/6.2-atoms/6.2.1-built-in-constants/README.md)
- Anlatım bekleniyor: [r:6.2.2](language-reference/06-expressions/6.2-atoms/6.2.2-identifiers-names/README.md)
- Anlatım bekleniyor: [r:6.2.2.1](language-reference/06-expressions/6.2-atoms/6.2.2-identifiers-names/6.2.2.1-private-name-mangling/README.md)
- Anlatım bekleniyor: [r:6.2.3](language-reference/06-expressions/6.2-atoms/6.2.3-literals/README.md)
- Anlatım bekleniyor: [r:6.2.3.1](language-reference/06-expressions/6.2-atoms/6.2.3-literals/6.2.3.1-literals-and-object-identity/README.md)
- Anlatım bekleniyor: [r:6.2.3.2](language-reference/06-expressions/6.2-atoms/6.2.3-literals/6.2.3.2-string-literal-concatenation/README.md)
- Anlatım bekleniyor: [r:6.2.4](language-reference/06-expressions/6.2-atoms/6.2.4-parenthesized-groups/README.md)
- Anlatım bekleniyor: [r:6.2.5](language-reference/06-expressions/6.2-atoms/6.2.5-container-displays/README.md)
- Anlatım bekleniyor: [r:6.2.5.1](language-reference/06-expressions/6.2-atoms/6.2.5-container-displays/6.2.5.1-list-displays/README.md)
- Anlatım bekleniyor: [r:6.2.5.2](language-reference/06-expressions/6.2-atoms/6.2.5-container-displays/6.2.5.2-set-displays/README.md)
- Anlatım bekleniyor: [r:6.2.5.3](language-reference/06-expressions/6.2-atoms/6.2.5-container-displays/6.2.5.3-tuple-displays/README.md)
- Anlatım bekleniyor: [r:6.2.5.4](language-reference/06-expressions/6.2-atoms/6.2.5-container-displays/6.2.5.4-dictionary-displays/README.md)
- Anlatım bekleniyor: [r:6.2.6](language-reference/06-expressions/6.2-atoms/6.2.6-comprehensions/README.md)
- Anlatım bekleniyor: [r:6.2.6.1](language-reference/06-expressions/6.2-atoms/6.2.6-comprehensions/6.2.6.1-filtering-in-comprehensions/README.md)
- Anlatım bekleniyor: [r:6.2.6.2](language-reference/06-expressions/6.2-atoms/6.2.6-comprehensions/6.2.6.2-complex-comprehensions/README.md)
- Anlatım bekleniyor: [r:6.2.6.3](language-reference/06-expressions/6.2-atoms/6.2.6-comprehensions/6.2.6.3-unpacking-in-comprehensions/README.md)
- Anlatım bekleniyor: [r:6.2.6.4](language-reference/06-expressions/6.2-atoms/6.2.6-comprehensions/6.2.6.4-asynchronous-comprehensions/README.md)
- Anlatım bekleniyor: [r:6.2.6.5](language-reference/06-expressions/6.2-atoms/6.2.6-comprehensions/6.2.6.5-formal-grammar-for-comprehensions/README.md)
- Anlatım bekleniyor: [r:6.2.7](language-reference/06-expressions/6.2-atoms/6.2.7-generator-expressions/README.md)
- Anlatım bekleniyor: [r:6.2.8](language-reference/06-expressions/6.2-atoms/6.2.8-yield-expressions/README.md)
- Anlatım bekleniyor: [r:6.2.8.1](language-reference/06-expressions/6.2-atoms/6.2.8-yield-expressions/6.2.8.1-examples/README.md)
- Anlatım bekleniyor: [r:6.2.8.2](language-reference/06-expressions/6.2-atoms/6.2.8-yield-expressions/6.2.8.2-asynchronous-generator-functions/README.md)
- Anlatım bekleniyor: [r:6.3](language-reference/06-expressions/6.3-primaries/README.md)
- Anlatım bekleniyor: [r:6.3.1](language-reference/06-expressions/6.3-primaries/6.3.1-attribute-references/README.md)
- Anlatım bekleniyor: [r:6.3.2](language-reference/06-expressions/6.3-primaries/6.3.2-subscriptions-and-slicings/README.md)
- Anlatım bekleniyor: [r:6.3.2.1](language-reference/06-expressions/6.3-primaries/6.3.2-subscriptions-and-slicings/6.3.2.1-slicings/README.md)
- Anlatım bekleniyor: [r:6.3.2.2](language-reference/06-expressions/6.3-primaries/6.3.2-subscriptions-and-slicings/6.3.2.2-comma-separated-subscripts/README.md)
- Anlatım bekleniyor: [r:6.3.2.3](language-reference/06-expressions/6.3-primaries/6.3.2-subscriptions-and-slicings/6.3.2.3-starred-subscriptions/README.md)
- Anlatım bekleniyor: [r:6.3.2.4](language-reference/06-expressions/6.3-primaries/6.3.2-subscriptions-and-slicings/6.3.2.4-formal-subscription-grammar/README.md)
- Anlatım bekleniyor: [r:6.3.3](language-reference/06-expressions/6.3-primaries/6.3.3-calls/README.md)
- Anlatım bekleniyor: [r:6.4](language-reference/06-expressions/6.4-await-expression/README.md)
- Anlatım bekleniyor: [r:6.5](language-reference/06-expressions/6.5-the-power-operator/README.md)
- Anlatım bekleniyor: [r:6.6](language-reference/06-expressions/6.6-unary-arithmetic-and-bitwise-operations/README.md)
- Anlatım bekleniyor: [r:6.7](language-reference/06-expressions/6.7-binary-arithmetic-operations/README.md)
- Anlatım bekleniyor: [r:6.8](language-reference/06-expressions/6.8-shifting-operations/README.md)
- Anlatım bekleniyor: [r:6.9](language-reference/06-expressions/6.9-binary-bitwise-operations/README.md)
- Anlatım bekleniyor: [r:6.10](language-reference/06-expressions/6.10-comparisons/README.md)
- Anlatım bekleniyor: [r:6.10.1](language-reference/06-expressions/6.10-comparisons/6.10.1-value-comparisons/README.md)
- Anlatım bekleniyor: [r:6.10.2](language-reference/06-expressions/6.10-comparisons/6.10.2-membership-test-operations/README.md)
- Anlatım bekleniyor: [r:6.10.3](language-reference/06-expressions/6.10-comparisons/6.10.3-identity-comparisons/README.md)
- Anlatım bekleniyor: [r:6.11](language-reference/06-expressions/6.11-boolean-operations/README.md)
- Anlatım bekleniyor: [r:6.12](language-reference/06-expressions/6.12-assignment-expressions/README.md)
- Anlatım bekleniyor: [r:6.13](language-reference/06-expressions/6.13-conditional-expressions/README.md)
- Anlatım bekleniyor: [r:6.14](language-reference/06-expressions/6.14-lambdas/README.md)
- Anlatım bekleniyor: [r:6.15](language-reference/06-expressions/6.15-expression-lists/README.md)
- Anlatım bekleniyor: [r:6.15.1](language-reference/06-expressions/6.15-expression-lists/6.15.1-iterable-unpacking/README.md)
- Anlatım bekleniyor: [r:6.16](language-reference/06-expressions/6.16-evaluation-order/README.md)
- Anlatım bekleniyor: [r:6.17](language-reference/06-expressions/6.17-operator-precedence/README.md)
- Anlatım bekleniyor: [r:7](language-reference/07-simple-statements/README.md)
- Anlatım bekleniyor: [r:7.1](language-reference/07-simple-statements/7.1-expression-statements/README.md)
- Anlatım bekleniyor: [r:7.2](language-reference/07-simple-statements/7.2-assignment-statements/README.md)
- Anlatım bekleniyor: [r:7.2.1](language-reference/07-simple-statements/7.2-assignment-statements/7.2.1-augmented-assignment-statements/README.md)
- Anlatım bekleniyor: [r:7.2.2](language-reference/07-simple-statements/7.2-assignment-statements/7.2.2-annotated-assignment-statements/README.md)
- Anlatım bekleniyor: [r:7.3](language-reference/07-simple-statements/7.3-the-assert-statement/README.md)
- Anlatım bekleniyor: [r:7.4](language-reference/07-simple-statements/7.4-the-pass-statement/README.md)
- Anlatım bekleniyor: [r:7.5](language-reference/07-simple-statements/7.5-the-del-statement/README.md)
- Anlatım bekleniyor: [r:7.6](language-reference/07-simple-statements/7.6-the-return-statement/README.md)
- Anlatım bekleniyor: [r:7.7](language-reference/07-simple-statements/7.7-the-yield-statement/README.md)
- Anlatım bekleniyor: [r:7.8](language-reference/07-simple-statements/7.8-the-raise-statement/README.md)
- Anlatım bekleniyor: [r:7.9](language-reference/07-simple-statements/7.9-the-break-statement/README.md)
- Anlatım bekleniyor: [r:7.10](language-reference/07-simple-statements/7.10-the-continue-statement/README.md)
- Anlatım bekleniyor: [r:7.11](language-reference/07-simple-statements/7.11-the-import-statement/README.md)
- Anlatım bekleniyor: [r:7.11.1](language-reference/07-simple-statements/7.11-the-import-statement/7.11.1-lazy-imports/README.md)
- Anlatım bekleniyor: [r:7.11.1.1](language-reference/07-simple-statements/7.11-the-import-statement/7.11.1-lazy-imports/7.11.1.1-compatibility-via-lazy-modules/README.md)
- Anlatım bekleniyor: [r:7.11.2](language-reference/07-simple-statements/7.11-the-import-statement/7.11.2-future-statements/README.md)
- Anlatım bekleniyor: [r:7.12](language-reference/07-simple-statements/7.12-the-global-statement/README.md)
- Anlatım bekleniyor: [r:7.13](language-reference/07-simple-statements/7.13-the-nonlocal-statement/README.md)
- Anlatım bekleniyor: [r:7.14](language-reference/07-simple-statements/7.14-the-type-statement/README.md)
- Anlatım bekleniyor: [r:8](language-reference/08-compound-statements/README.md)
- Anlatım bekleniyor: [r:8.1](language-reference/08-compound-statements/8.1-the-if-statement/README.md)
- Anlatım bekleniyor: [r:8.2](language-reference/08-compound-statements/8.2-the-while-statement/README.md)
- Anlatım bekleniyor: [r:8.3](language-reference/08-compound-statements/8.3-the-for-statement/README.md)
- Anlatım bekleniyor: [r:8.4](language-reference/08-compound-statements/8.4-the-try-statement/README.md)
- Anlatım bekleniyor: [r:8.4.1](language-reference/08-compound-statements/8.4-the-try-statement/8.4.1-except-clause/README.md)
- Anlatım bekleniyor: [r:8.4.2](language-reference/08-compound-statements/8.4-the-try-statement/8.4.2-except-clause/README.md)
- Anlatım bekleniyor: [r:8.4.3](language-reference/08-compound-statements/8.4-the-try-statement/8.4.3-else-clause/README.md)
- Anlatım bekleniyor: [r:8.4.4](language-reference/08-compound-statements/8.4-the-try-statement/8.4.4-finally-clause/README.md)
- Anlatım bekleniyor: [r:8.5](language-reference/08-compound-statements/8.5-the-with-statement/README.md)
- Anlatım bekleniyor: [r:8.6](language-reference/08-compound-statements/8.6-the-match-statement/README.md)
- Anlatım bekleniyor: [r:8.6.1](language-reference/08-compound-statements/8.6-the-match-statement/8.6.1-overview/README.md)
- Anlatım bekleniyor: [r:8.6.2](language-reference/08-compound-statements/8.6-the-match-statement/8.6.2-guards/README.md)
- Anlatım bekleniyor: [r:8.6.3](language-reference/08-compound-statements/8.6-the-match-statement/8.6.3-irrefutable-case-blocks/README.md)
- Anlatım bekleniyor: [r:8.6.4](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.1](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.1-or-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.2](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.2-as-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.3](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.3-literal-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.4](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.4-capture-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.5](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.5-wildcard-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.6](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.6-value-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.7](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.7-group-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.8](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.8-sequence-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.9](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.9-mapping-patterns/README.md)
- Anlatım bekleniyor: [r:8.6.4.10](language-reference/08-compound-statements/8.6-the-match-statement/8.6.4-patterns/8.6.4.10-class-patterns/README.md)
- Anlatım bekleniyor: [r:8.7](language-reference/08-compound-statements/8.7-function-definitions/README.md)
- Anlatım bekleniyor: [r:8.8](language-reference/08-compound-statements/8.8-class-definitions/README.md)
- Anlatım bekleniyor: [r:8.8.1](language-reference/08-compound-statements/8.8-class-definitions/8.8.1-multiple-inheritance/README.md)
- Anlatım bekleniyor: [r:8.9](language-reference/08-compound-statements/8.9-coroutines/README.md)
- Anlatım bekleniyor: [r:8.9.1](language-reference/08-compound-statements/8.9-coroutines/8.9.1-coroutine-function-definition/README.md)
- Anlatım bekleniyor: [r:8.9.2](language-reference/08-compound-statements/8.9-coroutines/8.9.2-the-async-for-statement/README.md)
- Anlatım bekleniyor: [r:8.9.3](language-reference/08-compound-statements/8.9-coroutines/8.9.3-the-async-with-statement/README.md)
- Anlatım bekleniyor: [r:8.10](language-reference/08-compound-statements/8.10-type-parameter-lists/README.md)
- Anlatım bekleniyor: [r:8.10.1](language-reference/08-compound-statements/8.10-type-parameter-lists/8.10.1-generic-functions/README.md)
- Anlatım bekleniyor: [r:8.10.2](language-reference/08-compound-statements/8.10-type-parameter-lists/8.10.2-generic-classes/README.md)
- Anlatım bekleniyor: [r:8.10.3](language-reference/08-compound-statements/8.10-type-parameter-lists/8.10.3-generic-type-aliases/README.md)
- Anlatım bekleniyor: [r:8.11](language-reference/08-compound-statements/8.11-annotations/README.md)
- Anlatım bekleniyor: [r:9](language-reference/09-top-level-components/README.md)
- Anlatım bekleniyor: [r:9.1](language-reference/09-top-level-components/9.1-complete-python-programs/README.md)
- Anlatım bekleniyor: [r:9.2](language-reference/09-top-level-components/9.2-file-input/README.md)
- Anlatım bekleniyor: [r:9.3](language-reference/09-top-level-components/9.3-interactive-input/README.md)
- Anlatım bekleniyor: [r:9.4](language-reference/09-top-level-components/9.4-expression-input/README.md)
- Anlatım bekleniyor: [r:10](language-reference/10-full-grammar-specification/README.md)

</details>

`builtins/` içindeki 45 yer tutucu klasörde anlatım yok. Bu klasörler için henüz görev veya milestone atanmadı; boş bölümler öğrenilmiş sayılmıyor.

## Yapıyı denetleme

Depo kökünde aşağıdaki komut kapsamı, kaynak değişimini, bağlantıları, önkoşul sırasını ve milestone zamanını denetler:

```bash
rtk proxy python scripts/validate_tasks.py
```

İlerleme kutucuklarının işaretlenmesine ilişkin regresyon kontrolleri:

```bash
rtk proxy python -B -m unittest discover -s scripts -p 'test_*.py'
```

Bu bakım denetimi öğrenci cevabının doğruluğunu veya kavramsal öğrenmeyi ölçmez. Görev çözümü [değerlendirme kılavuzuna](DEGERLENDIRME.md) göre ayrıca incelenir.
