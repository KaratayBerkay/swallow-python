# Görev 7.2: Dosya kipinin veriye etkisini seç

**Odak:** r/w/a/r+, metin/binary, encoding, with/close ve kapanmış dosya.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.1](../7.1-fancier-output-formatting/README.md).
- Ön bilgi: [t:6](../../06-modules/README.md).

**Kaynak/ortam notu:** Kaynak 3.15 metni UTF-8 varsayılanından söz ediyor. Yerel 3.11 üzerinde aynı sonucu almak için metin dosyalarında encoding="utf-8" kullan.

## Tek görev

1. Yalnız kendi çalışma klasöründe note.txt oluştur. open ile w kipinde "first\n" yaz, kapat; a kipinde "second\n" ekle; with ve r ile oku, blok dışında f.closed göster.

2. Aynı işlemi yeniden w ile açmanın önceki içeriğe etkisini ayrı bir kopyada dene.

3. Metin dosyası ile bir resim dosyasını açmak için kip/encoding seçimlerini yazılı karşılaştır; kapanmış dosyadan okumayı ayrı girişte dene.

## Geçiş ölçütleri

- [ ] Okunan içerik first ve second satırları; a koruyor, w eski içeriği siliyor.
- [ ] with sonrası closed True; kapalı dosyadan okuma ValueError.
- [ ] Metin str, binary bytes ile ilişkilendirilmiş; binary kipte encoding verilmemiş.
- [ ] r varsayılan, r+ iki yönlü; satır sonu dönüşümünün binary dosyaya neden uygun olmadığı açıklanmış.
- [ ] Dosyaya yazma tamamlanması için with/close gereksinimi açıklanmış; UTF-8 açıkça verilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
