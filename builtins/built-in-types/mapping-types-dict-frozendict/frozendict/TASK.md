# Görev b:2.12.1: Değişmez eşlemenin sınırını göster

## Önce

[b:2.12](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

`f=frozendict(a=[1]); once=f` ile başla. `f["a"].append(2)`, f içine yeni anahtar atama, `hash(f)` ve `f |= {"b":3}` işlemlerini ayrı ayrı incele. Sonuncudan önceki ve sonraki kimlikleri karşılaştır. Ayrıca hashable değerli bir frozendict ile hash dene.

## Geçiş ölçütleri

- [ ] İç liste değişebilir; shallow değişmezlik derin dondurma değildir.
- [ ] Anahtar atama TypeError, hash(f) TypeError; hashable anahtar ve değerler hash için gerekir.
- [ ] |= yeni frozendict üretir; once eski eşlemeyi tutar; frozendict dict alt sınıfı değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
