# Görev 7.2.1: Dosya imlecini ve satır sonunu izle

**Odak:** read/readline/iteration, EOF, write dönüşü, tell/seek ve binary konumlar.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2](../README.md).

## Tek görev

1. Çalışma dosyasına "A\n\nB" yaz.

2. Yeniden açarak readline sonuçlarını EOF dahil sırayla repr ile göster.

3. Ayrı açılışlarda read(2) + read() ve list(f) sonuçlarını karşılaştır.

4. Binary dosyada b"0123456789" yaz; seek(4), read(1), seek(-2, 2), read(1) uygula. tell konumlarını ve write dönüşlerini kaydet.

5. Metin kipinde geri dönmek için yalnız tell ile aldığın konumu kullan.

## Geçiş ölçütleri

- [ ] readline sırası A\n, \n, B, boş metin; boş satır EOF ile karıştırılmamış.
- [ ] read(2) ilk iki karakteri tüketiyor; sonraki read kalan yerden.
- [ ] Binary okumalar b"4" ve b"8"; konum başlangıç/son referansına göre hesaplanmış.
- [ ] write metin kipinde karakter sayısını döndürüyor; metin konumu keyfi bayt hesabıyla değiştirilmemiş.
- [ ] Dosya üzerinde döngünün kaynak tüketimi ile bütün satırları listelemenin farkı açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
