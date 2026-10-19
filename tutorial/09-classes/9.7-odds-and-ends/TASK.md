# Görev 9.7: Kayıt nesnesiyle metot bağını göster

**Odak:** Veri kaydı için verilen dataclass iskeleti, beklenen metotları sağlayabilme ve metot nitelikleri.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.6](../9.6-private-variables/README.md).
- Ön bilgi: [t:4.9.8](../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.8-function-annotations/README.md).

## Tek görev

1. README içindeki Employee dataclass tanımını hazır iskelet olarak kullan; iki çalışan oluşturup birinin dept değerini değiştir ve diğerinin korunduğunu göster.

2. Sonra kendi Notebook örneğindeki m = notebook.add_note için `m.__self__` ve `m.__func__` değerlerini, nesne ve sınıf işleviyle karşılaştır.

3. Son notunda read/readline bekleyen bir tüketiciye aynı metotları sağlayan başka nesnenin neden verilebildiğini açıkla.

4. Decorator mekanizmasını uygulaman gerekmiyor.

## Geçiş ölçütleri

- [ ] Çalışanların verileri ayrı; iskeletteki alanlar doğru argümanlarla doldurulmuş.
- [ ] `m.__self__` ilgili notebook, `m.__func__` Notebook.add_note işlevi.
- [ ] Veri kaydıyla davranış beklentisini karşılama ayrı ihtiyaçlar olarak açıklanmış.
- [ ] dataclass iç çalışma mekanizması veya daha önce öğretilmeyen bir seçenek kullanılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
