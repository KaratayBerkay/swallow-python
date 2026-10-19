# Görev 5.3.2: Bulucuyla yükleyicinin teslim sınırını çiz

**Odak:** Finder modül bilgisini/spec bulur, loader yürütür; importer iki rolü birleştirebilir.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.1](../5.3.1-the-module-cache/README.md).

## Tek görev

1. Bir modülün cache içinde olmadığı durumu çiz: arama isteği, finder, module spec, loader ve modül yürütmesi.

2. Disk, frozen ve built-in kaynaklarını bu çizimdeki arama stratejilerine yerleştir.

3. Finder spec döndüğünde modül gövdesinin yürümüş sayılıp sayılamayacağını açıkla.

## Geçiş ölçütleri

- [ ] Finder keşif, loader yürütme; spec aradaki bilgi aktarımı.
- [ ] Spec loader bilgisini içeriyor; finder doğrudan modül kodunu yürütmek zorunda değil.
- [ ] Aynı nesnenin iki rolü gerçekleştirebileceği importer kavramıyla açıklanmış.
- [ ] Eski finderın doğrudan loader döndürmesi tarihsel bilgi olarak ayrılmış; güncel iş akışına taşınmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
