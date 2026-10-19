# Çözümü kanıtla değerlendirme

Amaç bir cevabı hatırlamak değil; aynı mekanizmayı yeni bir girdide uygulayabilmek ve bir sorun çıktığında nereden geldiğini açıklayabilmek.

## Her adımda tek kontrol

1. Sıradaki bölümün anlatımını ve örneklerini tamamla. Aynı `README.md` içinde hemen ardından gelen bölüm görevini çöz. Alt bölüm bağlantıları bu kontrolden sonra gelir; milestone bütün alt görevler bittikten sonra yapılır.
2. Çözümünü, çalıştırmadan önceki beklentini ve gerçek gözlemi birlikte sun. Kod gerekmeyen incelemede, hangi olayın hangi kuralla gerçekleştiğini gösteren iz yeterlidir. Beklentin yanlış çıktıysa ilk beklentiyi silme; hangi varsayımı düzelttiğini ekle.
3. Değerlendiren kişi çözümü görev ölçütlerine göre inceler. Açıklamanın kodla uyuştuğunu, kullanılan her tekniğin bu ana kadar öğretildiğini ve gözlemin gerçekten sunulduğunu kontrol eder.
4. Son olarak aynı senaryoda tek bir girdi veya koşul değiştirilir. Sonucu önce açıklar, sonra çalıştırarak veya kaynağa dayalı iz sürerek doğrularsın. Bu küçük kontrol ayrı bir proje ya da yeni konu değildir.

Bu dört adım bütün bölüm görevleri ve yeni çözüm isteyen milestone'lar için ortaktır; görevlerde yeniden yazılmaz. Görev sayfasındaki özel ölçütler bu yönteme eklenir. Mevcut kanıtı kullanan milestone, tamamlanmış kontrolleri yeniden yaptırmaz.

Kaynakta yalnız adı geçen bir kavramı uygulamayı bilmen beklenmez. Bir örnekte ileri bir yapı hazır verildiyse, görev onun öğretilen kısmını sınayabilir; iç mekanizmasını yeniden yazmanı isteyemez.

## Geçiş kararı

| Karar | Gerekli kanıt | Sonraki hareket |
| --- | --- | --- |
| Geçti | Geçiş ölçütleri sağlandı; mekanizma doğru açıklandı; aynı konudaki küçük değişiklik doğru türetildi ve doğrulandı. | Sıradaki adıma geç. |
| Düzeltme gerekiyor | Sonuç, gerekçe veya sınır durumunda somut hata var. | Yalnız eksik bağı açıkla; aynı görevde ilgili kısmı yeniden dene. |
| Kanıt bekleniyor | Görevin izin verdiği çözüm/çalıştırma/iz kanıtı henüz sunulmadı. | Bilgi eksikliği varsayma; hangi kanıtın eksik olduğunu belirt. |

Görev ortam veya sürüm nedeniyle yazılı iz sürmeye açıkça izin veriyorsa, gerekçeli iz ve tek değişiklik kontrolü ölçütleri sağladığında karar **Geçti** olur; sıradaki adıma geçebilirsin. Örneğin Python 3.11 üzerinde 3.15'e özgü kısım için bu yol geçerlidir. Kayıtta ayrıca **Uygulama kanıtı: bekliyor (sürüm/ortam)** yazılır. Bu, çalıştırıldığı iddiası değildir ve ilerlemeyi engellemez. İzin verilen iz de yoksa karar **Kanıt bekleniyor** olur. Aynı kural milestone için de geçerlidir; ortamın desteklediği kısımların istenen çalıştırma kanıtı yine sunulur.

Gerçek uygulamayı açıkça şart koşan görevde, örneğin 12.2 sanal ortam deneyinde, yalnız komut taslağı geçiş için yeterli değildir. Ortam işlemi engelliyorsa gerçek hata ve eksik uygulama kanıtı kaydedilir; bilgi eksikliği varsayılmaz.

Yalnız çalışmış olması, örneği kopyalamak, doğru çıktıyı sabit yazmak veya "anladım" demek tek başına geçiş kanıtı değildir. Buna karşılık aynı sonucu veren, öğretilmiş başka bir doğru çözüm reddedilmez. Görev belli bir mekanizmayı özellikle sınatıyorsa o mekanizma kullanılmalıdır.

Ölçütler görevdeki belirleyici davranışları kapsar. Tek görev bütün olası girdilerde ustalık kanıtı değildir; milestone bilgileri yeni bir senaryoda birleştirir veya kapsam önceki görevlerle zaten sınanmışsa onların kanıtını kullanır. İkinci durumda aynı iş tekrarlanmaz. Bir milestone önceki görevleri atlamak için kullanılamaz.

## Değerlendiren kişinin sınırları

- Önce görev ve mevcut bölüm kaynağını oku; sonra yalnız listelenmiş ön bilgileri ve önceki bölümleri kullan. İleri bağlantıyı, dış dokümanı veya Python'da bildiğin başka bir tekniği sessiz önkoşul yapma.
- Öğretilmemiş bir bilgi gerektiğini fark edersen öğrenciye puan kaybettirme. Görevdeki o isteği düzelt veya önce eksik örneği anlatıma ekle. Önce kaynağın düzeltilmesi gerekir.
- Çalıştırılmamış kod için "çalıştı" deme. Kaynak incelemesinden çıkan beklentiyle gerçek gözlemi ayrı yaz. Yazılı inceleme görevi için çalışan program isteme.
- Python sürümü, işletim sistemi, yerel ayar veya REPL desteği farklıysa görevdeki ortam notunu ve yukarıdaki geçiş kuralını kullan. İzin verilen yazılı iz ölçütleri sağlıyorsa **Geçti**, uygulama kanıtı ise **bekliyor (sürüm/ortam)** olarak ayrı kaydedilir.
- Her geri bildirimde tek eksik noktaya odaklan. Bilgi eksikse önce açıklamayı yap; öğretilmemiş bir şeyi tahmin ettirerek soru sorma. Uygun ipucundan sonra da takılıyorsa eksik adımı doğrudan göster.
- Küçük değişiklik kontrolünde yalnız bir değer, sınır, boşluk, sıra veya zaten işlenmiş bir koşul değiştir. Yeni API, algoritma, dil yapısı veya altyapı ekleme.
- Sonraki bölümü kendiliğinden açma. İlgili adımı değerlendirip sonucu ver; kullanıcı ilerlemek istediğinde sıradaki adımdan devam et.
- Dosya/ortam işlemleri yalnız yerel çalışma alanında olsun. Ağ, e-posta ve hesap örneklerini görevdeki yerel iz/taslak üzerinden değerlendir; dış hizmete yazma veya gönderim yapma.

## Kısa değerlendirme kaydı

Her görev için aşağıdaki kaydı kendi notlarında tutabilirsin; ayrı takip uygulaması gerekmiyor:

```text
Görev:
Çözüm ve gözlem:
Mekanizma açıklaması:
Tek değişiklik ve öngörülen sonuç:
Doğrulanan sonuç:
Karar: Geçti / Düzeltme gerekiyor / Kanıt bekleniyor
Uygulama kanıtı: doğrulandı / bekliyor (sürüm/ortam) / gerekmiyor (yazılı inceleme görevi)
Eksik tek nokta (varsa):
```

`scripts/validate_tasks.py` yalnız görev yapısını denetler. Bir cevap değerlendirme motoru değildir; çalıştırılması öğrenilmişlik kaydı oluşturmaz.

Görev metni düzenlenirken aynı klasördeki `TASK.md` veya `MILESTONE.md` kaynak dosyası kullanılır. Ardından `rtk proxy python scripts/place_tasks.py` komutu metni anlatımdaki doğru noktaya taşır. Denetleyici, sayfa içindeki metnin kaynakla aynı kaldığını ve yerinin doğru olduğunu kontrol eder.
