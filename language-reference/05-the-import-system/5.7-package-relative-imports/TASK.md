# Görev 5.7: Göreli importu mutlak ada çöz

**Odak:** Nokta sayısı, package bağlamı, alias ve göreli import için from gerekliliği.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.6](../5.6-replacing-the-standard-import-system/README.md).
- Ön bilgi: [t:6.4.2](../../../tutorial/06-modules/6.4-packages/6.4.2-intra-package-references/README.md).

## Tek görev

1. README içindeki package.subpackage1.moduleX konumundan .moduleY, ..subpackage2.moduleZ ve ..moduleA yollarını mutlak importlara çevir. spam as ham aktarımında kaynak nesne ile yerel adı ayır.

2. Aynı göreli ifadenin subpackage1/`__init__`.py içinde neden aynı hedefi bulduğunu açıkla. import .moduleY biçiminin neden geçerli olmadığını yaz.

## Geçiş ölçütleri

- [ ] Hedefler package.subpackage1.moduleY, package.subpackage2.moduleZ, package.moduleA.
- [ ] Bir nokta mevcut paket, her ek nokta bir üst paket.
- [ ] Alias yerel adı değiştiriyor, kaynağı değiştirmiyor.
- [ ] Göreli import from biçiminde; başlangıç noktası dosya sisteminin çalışma dizini değil paket bağlamı.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
