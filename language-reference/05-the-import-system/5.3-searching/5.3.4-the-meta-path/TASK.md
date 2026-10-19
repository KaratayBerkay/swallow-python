# Görev 5.3.4: Meta path taramasının devam ve durma koşullarını izle

**Odak:** find_spec argümanları, None/spec/hata sonuçları, cache sonrası sıra ve reload target.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.3](../5.3.3-import-hooks/README.md).

## Tek görev

1. Cache boş ve meta path sırası F1, F2, F3 olsun.

2. F1 None, F2 spec, F3 hata verecek şekilde tanımlandığında hangi çağrılar gerçekleşir?

3. Sonra F1 hata versin; sonra hepsi None versin. foo.bar.baz için tam ad/path/target argümanlarını her ebeveyn düzeyinde tabloya yaz; foo.bar reload olduğunda target farkını belirt.

## Geçiş ölçütleri

- [ ] İlk senaryoda F3 çağrılmaz; ikinci hata hemen yayılır; hepsi None ise ModuleNotFoundError.
- [ ] Üst düzey path None, alt düzeylerde ebeveyn `__path__`.
- [ ] Normal import target None; reload mevcut modül hedefi kullanıyor.
- [ ] Noktalı import için meta path birden fazla kez dolaşılabiliyor.
- [ ] Built-in/frozen/path finder rolleri ve kaldırılmış find_module yerine find_spec kullanımı ayrılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
