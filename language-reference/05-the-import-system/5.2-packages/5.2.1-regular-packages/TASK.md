# Görev 5.2.1: Paket başlatıcılarının yürütme sırasını çıkar

**Odak:** Regular paket `__init__` yürütmesi, ebeveyn içe aktarımı ve ayrı alt paketler.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.2](../README.md).

## Tek görev

1. Bölümdeki parent/one/two/three ağacının çalışma kopyasında her `__init__`.py içine kendi adını yazdıran tek satır ekle.

2. Aynı oturumda parent.one, parent.two ve tekrar parent.one içe aktar.

3. Mesaj sırasını ve her başlatıcının kaç kez çalışacağını önce çıkar, sonra gözlemle.

## Geçiş ölçütleri

- [ ] İlk import parent sonra parent.one başlatıcılarını yürütüyor.
- [ ] İkinci import yalnız parent.two başlatıcısını ilk kez yürütüyor.
- [ ] Tekrar parent.one yeni başlangıç yürütmesi yapmıyor.
- [ ] three açıkça istenmediği için çalışmıyor; alt klasörde `__init__` yokluğu otomatik regular paket sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
