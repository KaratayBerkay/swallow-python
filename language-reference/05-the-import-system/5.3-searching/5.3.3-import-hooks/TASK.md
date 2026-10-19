# Görev 5.3.3: Hookun hangi aşamaya girdiğini seç

**Odak:** Meta hook ile path hook giriş noktalarının farkı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.2](../5.3.2-finders-and-loaders/README.md).

## Tek görev

1. İki gereksinimi kağıt üzerinde doğru hook listesine yerleştir: cache başarısız olduktan sonra built-in araması dahil normal arama akışının önüne geçmek; yalnız özel bir arama yolu girdisiyle karşılaşınca o girdiyi ele almak.

2. Her biri için sys.modules, sys.meta_path ve sys.path_hooks sırasındaki yerini göster.

## Geçiş ölçütleri

- [ ] İlk gereksinim meta hook/sys.meta_path, ikinci path hook/sys.path_hooks.
- [ ] Cache kontrolü meta hooktan önce.
- [ ] Path hook bütün importların ilk aşaması sayılmamış; sys.path veya paket `__path__` işlenirken devreye giriyor.
- [ ] Bu bölümde protokol uygulaması gösterilmediği için yeni hook sınıfı yazılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
