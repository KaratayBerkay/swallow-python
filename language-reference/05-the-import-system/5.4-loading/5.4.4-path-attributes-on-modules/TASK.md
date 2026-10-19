# Görev 5.4.4: Paket aramasının kapsamını daralt

**Odak:** `__path__` ile alt modül arama, sys.path farkı ve namespace yolu.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.3](../5.4.3-module-specs/README.md).

## Tek görev

1. Üst düzey sys.path = ["/global", "/plugins"], `lessonpack.__path__` = ["/plugins/lessonpack"] varsay. lessonpack.tools importunda hangi yolun tarandığını ve neden bütün sys.path girdilerinin doğrudan tools aramasına çevrilmediğini çiz. `__path__` boşken paket sayılma ile alt modül bulunabilirliğini ayrı değerlendir; regular/namespace paketlerde yolun nasıl hazırlanabildiğini açıkla.

## Geçiş ölçütleri

- [ ] Alt arama ebeveyn `lessonpack.__path__` üzerinden.
- [ ] `__path__` varlığı paket ölçütü; boş olma tek başına normal modüle dönüştürmüyor.
- [ ] sys.path_hooks paket yollarında da kullanılabiliyor.
- [ ] Regular paket başlangıç dosyası yolu değiştirebilir; namespace yolu machinery tarafından hazırlanır; gerçek sistem yolu değiştirilmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
