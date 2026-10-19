# Görev 11.2: Eksik alanı tamamlamadan şablonu koru

**Odak:** Template $/{}/$$, substitute/safe_substitute ve özel delimiter.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.1](../11.1-output-formatting/README.md).
- Ön bilgi: [t:9.5](../../09-classes/9.5-inheritance/README.md).

## Tek görev

1. Template("${name}box costs $$5 for $owner.") oluştur. name="Study", owner="Ada" ile doldur; owner eksikken substitute ile safe_substitute sonuçlarını ayrı dene.

2. Sonra bölümdeki BatchRename iskeletindeki delimiter = "%" yaklaşımını kullanarak "%n%f" şablonunu n=2, f=".jpg" ile doldur.

3. Yalnız yeni dosya adını üret, dosya yeniden adlandırma işlemi gerekmiyor.

## Geçiş ölçütleri

- [ ] Tam sonuç Studybox costs $5 for Ada.
- [ ] Eksik owner substitute için KeyError, safe_substitute için $owner olarak kalıyor.
- [ ] ${name} bitişi, isimden sonra box ekine izin veriyor; $$ tek $ üretiyor.
- [ ] Özel ayraç sonucu 2.jpg; şablonun veriyle doldurulması program mantığından ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
