# Görev 6.4.1: Yıldızlı aktarımın sınırını gör

**Odak:** `__all__`, kendiliğinden alt modül taramama, önceden yüklenen adlar ve isim gölgeleme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.4](../README.md).

## Tek görev

1. Kendi lessonpack/tools paketinin kopyasında `__all__` = ["counts"] tanımla; from lessonpack.tools import * sonrasında gelen adı kontrol et.

2. Sonra `__all__` kaldırılmış, başlangıç dosyası boş bir kopyada aynı deneyi yeni oturumda yap; counts açıkça import edildikten sonraki durumu karşılaştır.

3. Üçüncü kopyada counts adlı bir fonksiyon tanımlayıp `__all__` içine counts ekle; modül yerine hangi nesnenin geleceğini izle.

## Geçiş ölçütleri

- [ ] `__all__` varsa counts adı dışarı aktarılıyor.
- [ ] Boş başlangıç dosyası ve `__all__` yokken diskteki bütün modüller taranıp aktarılmıyor.
- [ ] Önceden yüklenen alt modül paket adı alanında bulunduğu için sonraki * kapsamına girebiliyor.
- [ ] Aynı adlı fonksiyon modülü gölgeleyebiliyor; belirli adı açıkça import etmenin yararı açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
