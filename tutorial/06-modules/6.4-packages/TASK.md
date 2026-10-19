# Görev 6.4: Paket yolunu çağrı biçimiyle eşleştir

**Odak:** Paket ağacı, `__init__`.py, noktalı adlar ve üç import biçiminin ad bağlaması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.3](../6.3-the-dir-function/README.md).

## Tek görev

1. Çalışma klasöründe lessonpack/ ve lessonpack/tools/ paketlerini boş `__init__`.py dosyalarıyla kur. tools/counts.py içinde count_items(items) olsun.

2. Ayrı oturumlarda import lessonpack.tools.counts, from lessonpack.tools import counts, from lessonpack.tools.counts import count_items biçimlerini kullanıp aynı iki öğenin sayısını al.

3. Her çağrıda kullanılabilir adı yaz ve README içindeki sound ağacına eşleştir.

## Geçiş ölçütleri

- [ ] Üç çağrı da 2 veriyor; tam yol, modül adı ve doğrudan işlev adı doğru kullanılmış.
- [ ] Her ara bileşen paket; son bileşen modül olabiliyor.
- [ ] `__init__`.py regular paket başlatma dosyası olarak tanımlanmış.
- [ ] from package import item ile import package.item arasındaki son öğe kuralları açıklanmış; namespace paket uygulaması istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
