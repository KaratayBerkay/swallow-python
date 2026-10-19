# Görev 5.8.1: Çalıştırma biçimine göre ana specini belirle

**Odak:** `__main__.__spec__` dolu/None durumları ve import edilebilir modülden ayrı kimlik.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.8](../README.md).
- Ön bilgi: [r:5.4.3](../../5.4-loading/5.4.3-module-specs/README.md).

## Tek görev

1. Başlatma tablosu hazırla: python helper.py; python -m helper; -c; stdin; etkileşimli istem; dizin veya zip girişinden çalıştırma.

2. Her biri için ana `__name__` ve `__spec__` doluluk durumunu yaz. helper.py import edilebilir olmasına rağmen dosya yoluyla başlatılınca neden aynı metadata garantisinin oluşmadığını açıkla. -m ile çalışan ana nesne ile normal import helper nesnesini ayrı çiz.

## Geçiş ölçütleri

- [ ] Hepsinde ana ad `__main__`; spec -m/dizin/zip için dolu, dosya/-c/stdin/etkileşimli durumda None.
- [ ] Dosyanın import edilebilir olması doğrudan dosya çalıştırmasında spec oluşturma garantisi değil.
- [ ] -m ile ana modül ve normal import edilen modül ayrı modül nesneleri olarak modellenmiş.
- [ ] Main korumasının yalnız ana girişte çalışması kimlik/başlatma farkına bağlanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
