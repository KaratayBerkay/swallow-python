# Görev 4.9.1: Varsayılan değerin ömrünü düzelt

**Odak:** Zorunlu/isteğe bağlı argüman, tanım anında değerlendirme ve paylaşılan değiştirilebilir varsayılan.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../../4.8-defining-functions/README.md).
- Ön bilgi: [t:3.1.3](../../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

## Tek görev

1. README içindeki f(a, L=[]) örneğini 4 ve 9 ile art arda çağırıp liste paylaşımını göster.

2. Aynı işlevi varsayılan listesi çağrılar arasında paylaşılmayacak biçimde düzelt; ayrıca açıkça bir liste verilirse o listeye eklemeyi sürdürsün.

3. Ayrı bir örnekte seed = 4 iken def show(value=seed) tanımla, seed = 9 yapıp argümansız çağrının sonucunu açıkla. ask_ok örneğinde bir, iki ve üç argümanlı çağrıların hangi varsayılanları kullandığını not et.

## Geçiş ölçütleri

- [ ] İlk sürümün ikinci çağrısında [4, 9] oluşuyor.
- [ ] Düzeltilmiş sürümün argümansız liste kullanan çağrıları bağımsız; verilen liste ise aynı nesne olarak değişiyor.
- [ ] show varsayılanının 4 kalması tanım zamanı ile açıklanmış.
- [ ] ask_ok zorunlu prompt ve iki varsayılan bakımından doğru eşleştirilmiş; in üyelik denetimi olarak okunmuş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
