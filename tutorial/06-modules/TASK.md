# Görev 6: İşlevi başka dosyadan kullan

**Odak:** Modül dosyası, import ile ad bağlama, modül niteliği ve `__name__`.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../04-more-control-flow-tools/4.8-defining-functions/README.md).

## Tek görev

1. Ayrı bir çalışma klasöründe counts.py içine count_items(items) işlevini yaz; len(items) döndürsün.

2. Aynı klasörden başlattığın REPL içinde import counts ile işlevi çağır, `counts.__name__` değerini göster ve f = counts.count_items ile ikinci ad üzerinden çağır.

3. Python oturumu yeniden başlayınca nelerin kaybolduğunu, dosyanın neden kaldığını açıkla.

## Geçiş ölçütleri

- [ ] counts.count_items([3, 5]) ve f([3, 5]) sonuçları 2.
- [ ] import counts, count_items adını tek başına yerel alana eklemiyor.
- [ ] `counts.__name__` counts metni; dosya adı .py son ekiyle ilişkili.
- [ ] Yeni oturumda tekrar import gerektiği açıklanmış; sonraki bölümdeki from/as teknikleri gerekmiyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
