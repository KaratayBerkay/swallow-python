# Görev 5.4.1: Loaderın sorumluluğunu makineninkinden ayır

**Odak:** create_module/exec_module, dönüş değeri, modül namespace ve tarihsel load_module.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4](../README.md).

**Kaynak/ortam notu:** Bu sayfada eski load_module uyumluluk paragrafları duruyor; üst 5.4 bölümündeki 3.15 kaldırılma notuyla birlikte oku. Görev modern create_module/exec_module sözleşmesini esas alır.

## Tek görev

1. Kod yazmadan loader sözleşme tablosu hazırla: create_module yeni nesne döndürüyor; create_module None döndürüyor; exec_module başarılı ama 123 döndürüyor; exec_module hata yükseltiyor.

2. Her satırda yaratmayı kim tamamlar, modülün verisi nerede oluşur ve sonuç/hata nasıl ele alınır yaz.

3. Metindeki load_module gerekliliklerini tarihsel API sütununda tut.

## Geçiş ölçütleri

- [ ] create_module None ise import machinery nesneyi oluşturuyor.
- [ ] exec_module kendisine verilen modülün namespace alanını dolduruyor, dönüşte 123 kullanılması gerekmiyor.
- [ ] Yükleyememe ImportError olabilir; diğer hatalar da yayılır.
- [ ] Eski load_module boilerplate sorumlulukları modern exec_module sorumluluğuyla karıştırılmamış.
- [ ] 3.15 hedefinde eski fallback güncel sözleşme sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
