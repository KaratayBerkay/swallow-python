# Görev 6.1.2: Yanlış modülün neden seçildiğini bul

**Odak:** sys.path kaynakları, arama önceliği, built-in ayrımı ve dosya adı çakışması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1.1](../6.1.1-executing-modules-as-scripts/README.md).

## Tek görev

1. Bir arama izi yaz: betik /work/app/run.py, PYTHONPATH içindeki yol /work/shared, varsayılan kitaplık yolu /python/lib olsun.

2. Hem /work/app/random.py hem kitaplığın random modülü var; /work/shared/helper.py de var. random ve helper için hangi kaynağın seçileceğini açıkla.

3. Sonra sys built-in olduğunda aynı klasörde sys.py bulunmasını ayrı değerlendir. run.py bir sembolik bağ üzerinden çağrılsaydı hangi dizinin ekleneceğini anlat.

4. Gerçek ortam değişkeni veya sistem dosyası değiştirmen gerekmiyor.

## Geçiş ölçütleri

- [ ] random için betik dizinindeki dosya, helper için shared yolu seçilmiş.
- [ ] sys built-in aramasının yol aramasından önce olduğu ayrılmış.
- [ ] sys.path için betik dizini, PYTHONPATH ve varsayılan kurulum kaynakları belirtilmiş.
- [ ] Sembolik bağın bulunduğu yer yerine çözümlenmiş betik dizini kullanılıyor; dosya adının kitaplığı gölgelemesi açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
