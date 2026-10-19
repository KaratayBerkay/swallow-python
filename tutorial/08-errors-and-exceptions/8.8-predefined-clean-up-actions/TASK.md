# Görev 8.8: Blok hatayla bitse de dosyayı kapat

**Odak:** with ile önceden tanımlı temizlik ve hata sonrası kaynak durumu.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.7](../8.7-defining-clean-up-actions/README.md).
- Ön bilgi: [t:7.2](../../07-input-and-output/7.2-reading-and-writing-files/README.md).

## Tek görev

1. Kendi çalışma dosyanı with open(..., encoding="utf-8") as f ile aç; ilk satırdan sonra bilerek ValueError yükselt.

2. Dıştaki try/except içinde hatayı yakaladıktan sonra f.closed kontrol et.

3. Aynı akışın with kullanmadan yazılan taslağında close satırına neden ulaşılamayacağını göster.

## Geçiş ölçütleri

- [ ] Hata yakalandıktan sonra f.closed True.
- [ ] Hata with bloğu içinde oluşmuş; temizlik yalnız başarı yolunda sınanmamış.
- [ ] with kaynağın temizliğini, except hataya verilen tepkiyi yönetiyor.
- [ ] Kendi context manager sınıfını yazmak veya özel metot API bilgisi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
