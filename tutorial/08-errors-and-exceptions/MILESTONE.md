# Milestone: Kötü kayıtları kaybetmeden içe al

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Hata yakalama/yükseltme, not, grup ve kaynak temizliğini birlikte kullanma.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir yerel dosyaya "7\nbad\n0\n-2\n" yaz. with ile satırları oku; her satırı int yap, negatif için ValueError yükselt.

2. Geçerli sayıları topla; dönüşüm veya negatif hatasına satır numarası notu ekleyip listeye al.

3. Okuma bitince hatalar varsa ExceptionGroup ile yükselt.

4. Çağıranda except* ValueError ile ilgili grubu işle ve finally içinde son durum mesajı göster.

5. Dosya açılmaması gibi ilgisiz hataların aynı handler tarafından yutulmadığını ayrı senaryoda göster.

## Geçiş ölçütleri

- [ ] Geçerli değerler 7 ve 0; bad ve -2 için iki ayrı hata var.
- [ ] Hatalar kendi satır bağlamını taşıyor; ilk hatada bütün okuma durmuyor.
- [ ] Dosya hatadan önce veya sonra da doğru kapanıyor.
- [ ] except* yalnız hedef alt hataları işliyor; finally çalışması başarıyla karıştırılmamış.
- [ ] Özel alan hatası sınıfının hangi tabana oturacağı tasarım notunda açıklanmış; sınıf yazımı zorunlu değil.
- [ ] Tamamlanan, hatalı ve yayılan durumlar ayrı kanıtlarla gösterilmiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
