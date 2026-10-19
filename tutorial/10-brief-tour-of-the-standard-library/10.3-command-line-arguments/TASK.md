# Görev 10.3: Komut satırının sözleşmesini sınırda kontrol et

**Odak:** argparse konumsal çoklu değer, int dönüşümü, seçenek adı ve varsayılan.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.2](../10.2-file-wildcards/README.md).
- Ön bilgi: [t:2.1.1](../../02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.1-argument-passing/README.md).

## Tek görev

1. Bölümdeki parser iskeletini kopyala: filenames nargs="+", -l/--lines type=int ve default=10 kalsın.

2. Dosya okumadan yalnız ayrıştırılan değerleri göster.

3. İki dosya adı; --lines=3 ile iki dosya; -l 0 ile bir dosya; hiç dosya vermeme; --lines=bad ile bir dosya senaryolarını ayrı çalıştır.

4. Aynı girdinin sys.argv içinde neye benzediğini karşılaştır.

## Geçiş ölçütleri

- [ ] Seçenek yokken lines 10; diğer geçerli değerler 3 ve 0, türleri int.
- [ ] filenames sıra korunmuş metin listesi.
- [ ] Eksik zorunlu konumsal ve geçersiz int girdileri parser tarafından reddediliyor.
- [ ] sys.argv ham metinler ile argparse sonucu aynı yapı sanılmamış; dosya açma bu göreve eklenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
