# Görev 12.3: Paket değişiminin planını ve kanıtını yaz

**Odak:** pip install/pin/upgrade/uninstall, show/list/freeze ve requirements ile yeniden kurma.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:12.2](../12.2-creating-virtual-environments/README.md).

## Tek görev

1. Ağ veya kurulum çalıştırmadan, docs içindeki paket adlarını kullanarak bir komut planı hazırla: requests için tam sürüm kur; aynı sürümü yeniden iste; en yeni sürüme yükselt; show/list ile gözle; freeze çıktısını requirements.txt olarak sakla; ikinci ortamda bu dosyadan kur; ilk ortamdan requests kaldır.

2. Her komutun beklenen etkisini ve etkisiz kalabileceği durumu yaz. requirements taslağı için docs içindeki örnek verileri kullan; güncel sürüm olduklarını iddia etme.

## Geçiş ölçütleri

- [ ] Tam sürüm == ile; yükseltme --upgrade ile; dosyadan kurma -r ile.
- [ ] Aynı sürüm zaten varsa yeniden isteğin değişiklik gerektirmeyebileceği açıklanmış.
- [ ] show paket bilgisi, list kurulu paket görünümü, freeze yeniden kurulabilir sürüm satırları olarak ayrılmış.
- [ ] uninstall yalnız seçilen ortama yönelik; yorumlayıcı seçimi python -m pip üzerinden.
- [ ] Eski örnek sürümler güncel öneri veya gerçekten kurulmuş paket gibi sunulmamış; paket yayımlama yok.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
