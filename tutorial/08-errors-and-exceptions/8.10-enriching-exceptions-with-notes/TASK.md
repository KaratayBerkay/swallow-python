# Görev 8.10: Hatanın kimliğini koruyup bağlam ekle

**Odak:** add_note, eklenme sırası, yeniden yükseltme ve grup içindeki yerel bağlam.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.9](../8.9-raising-and-handling-multiple-unrelated-exceptions/README.md).

## Tek görev

1. İki farklı sayı dönüşümünde oluşan ValueError hatalarını listeye topla.

2. Her hataya önce hangi girdiye ait olduğunu, sonra "count import" işlemini belirten iki not ekle.

3. Sonunda ExceptionGroup ile yükselt.

4. Hata türü/mesajı ile notların konum ve sırasını incele; tek hata için çıplak raise ile aynı notların korunmasını ayrıca göster.

## Geçiş ölçütleri

- [ ] Her alt hatanın kendi girdi notu var; notlar yanlış hataya taşınmamış.
- [ ] İki not eklenme sırasıyla hata mesajından sonra görünüyor.
- [ ] Asıl ValueError türü ve mesajı korunuyor.
- [ ] Not ekleme ile yeni exception oluşturarak hata çevirme arasındaki fark açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
