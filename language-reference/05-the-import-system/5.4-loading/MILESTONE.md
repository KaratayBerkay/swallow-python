# Milestone: Başarısız importun geride bıraktığı durumu değerlendir

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Yaratma, spec, loader, parent bağı, cache ve bytecode politikasını birleştirme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir package.child ilk kez yükleniyor: parent zaten var; child metadata/cache kaydı hazırlanıyor; child başka modülü başarıyla yüklüyor ve sonra hata veriyor.

2. Son durumu namespace/cache haritasında göster.

3. Aynı akışın başarılı, cache içindeki nesneyi değiştiren ve reload sırasında hata veren varyantlarını karşılaştır.

4. Ayrı bir kod seçimi kararı olarak, diskteki checked hash cache geçersizse eski bytecode'un kullanılmasını mı, kaynaktan yeniden derlemeyi mi beklediğini açıkla. Bytecode geçerliliği ile modül gövdesinin çalışırken hata vermesini ayır.

## Geçiş ölçütleri

- [ ] İlk hatada child çıkar; parent ve başarıyla yüklenen diğer modül kalır.
- [ ] Başarı durumunda parent.child ile sys.modules kaydı tutarlı.
- [ ] exec_module dönüşü kullanılmıyor; nihai cache nesnesi önem taşıyor.
- [ ] Reload hata temizliği ilk yüklemeyle karıştırılmamış.
- [ ] Spec metadata taşıyor, `__path__` alt aramayı sınırlandırıyor; geçersiz checked hash için kaynak yeniden derleniyor. Bu karar gövdenin hatasız çalışacağı garantisi sayılmamış.
- [ ] Namespace paket durumu kısaltılmış sözde kod yüzünden imkansız sayılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
