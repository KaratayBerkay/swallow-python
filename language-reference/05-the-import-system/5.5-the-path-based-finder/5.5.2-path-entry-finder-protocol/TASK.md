# Görev 5.5.2: Path finder protokolünü doğru imzayla oku

**Odak:** Path entry find_spec imzası, loader/spec ve namespace portion bilgisi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.5.1](../5.5.1-path-entry-finders/README.md).

## Tek görev

1. Meta path finder ile path entry finder için find_spec çağrılarının parametrelerini yan yana yaz.

2. Normal modül speci ile namespace portion bildiren specin hangi bilgiyi farklı taşıdığını göster.

3. Kaynaktaki find_loader/find_module yöntemlerini tarihsel olarak etiketle; bunlarla yeni bir finder yazma.

## Geçiş ölçütleri

- [ ] Meta path fullname/path/target; path entry fullname/target olarak ayrılmış.
- [ ] Normal spec loader bilgisi taşır; namespace portion submodule_search_locations ile bildirilir.
- [ ] Path entry finder yolu başlangıçtaki hook seçiminden zaten biliyor.
- [ ] 3.12 ile kaldırılan eski protokoller güncel zorunluluk sanılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
