# Milestone: Tekrar kullanılabilir hesap paketini teslim et

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Modül/paket sınırları, kontrollü başlangıç, public adlar ve keşif.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. studycalc paketinde operations.py içinde total(values), driver.py içinde yalnız ana girişte örnek veriyle sonuç yazdıran kod olsun. `__init__`.py üzerinden total adını açıkça sun.

2. Ayrı REPLde import studycalc, from studycalc import total ve bir alias çağrısı yap; dir ile erişilebilir adları kontrol et. driver için paket bağlamında -m başlatma planı yaz.

3. Bir ad gölgeleme hatasını oluşturmak yerine hangi dosya adından kaçınacağını açıklayan teşhis notu ekle.

## Geçiş ölçütleri

- [ ] Paket işlevi ve doğrudan alınan işlev aynı veride aynı sonucu veriyor.
- [ ] Normal importta driver raporu çalışmıyor.
- [ ] Public adlar bilinçli dışarı açılmış; tüm adları * ile yayma varsayımı yok.
- [ ] Arama yolu ve yeniden import/reload farkı açıklanmış.
- [ ] Başka klasörden çalıştırma gereksinimi paket dosyalarının yanında olmakla karıştırılmamış; daha önce işlenmeyen paket kurulumu gerekmiyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
