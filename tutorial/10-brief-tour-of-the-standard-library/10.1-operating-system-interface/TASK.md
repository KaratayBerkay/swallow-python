# Görev 10.1: Dosya işlemini doğru arayüzle eşleştir

**Odak:** os ile çalışma dizini, nitelikli import, help/dir ve shutil copy/move.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2](../../07-input-and-output/7.2-reading-and-writing-files/README.md).
- Ön bilgi: [t:6.3](../../06-modules/6.3-the-dir-function/README.md).

## Tek görev

1. Kendi geçici çalışma klasöründe source.txt ve dest alt klasörünü hazırla. os.getcwd ile konumu kaydet; shutil.copyfile ile source.txt dosyasını copy.txt olarak kopyala, ardından shutil.move ile copy.txt dosyasını dest içine taşı.

2. Sonuçları open ile okuyarak karşılaştır. os.chdir örneğinin sonraki göreli dosya adlarını nasıl etkilediğini ve os.system("mkdir today") satırının ne yaptığını yazılı izle. help(os) ile dir(os) amaçlarını ayır.

## Geçiş ölçütleri

- [ ] Asıl source.txt korunuyor; taşınan kopya dest içinde aynı içeriğe sahip.
- [ ] Kopyalama ile taşıma farkı yalnız mesajdan değil dosyaların son yerlerinden gösterilmiş.
- [ ] Çalışma dizini değişimi göreli dosya aramasını etkiliyor; shell komutu Python ifadesi sanılmamış.
- [ ] import os biçiminin os.open ile built-in open karışmasını önlediği açıklanmış; sistem dizinlerine yazılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
