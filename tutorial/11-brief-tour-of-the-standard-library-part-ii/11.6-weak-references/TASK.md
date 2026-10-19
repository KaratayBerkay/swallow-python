# Görev 11.6: İzleyen tablonun nesneyi yaşatıp yaşatmadığını göster

**Odak:** Güçlü/zayıf referans, WeakValueDictionary ve son güçlü bağın silinmesi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.5](../11.5-logging/README.md).
- Ön bilgi: [t:9.1](../../09-classes/9.1-a-word-about-names-and-objects/README.md).

## Tek görev

1. Bölümdeki A sınıfıyla bir nesne oluştur; onu weakref.WeakValueDictionary içinde tut.

2. Ayrıca keeper adını aynı nesneye bağla.

3. İlk adı silip gc.collect sonrası weak tabloyu kontrol et; sonra keeper adını da sil, gc.collect yapıp tekrar bak.

4. Deneyi REPL içindeki son sonuç referansından etkilenmemesi için ayrı bir betikte yap.

## Geçiş ölçütleri

- [ ] keeper varken weak tablodan erişim mümkün.
- [ ] Son güçlü bağ silinince anahtara erişim KeyError.
- [ ] weak tabloya koymanın nesneyi tek başına yaşatmadığı açıklanmış.
- [ ] gc.collect dönüşündeki belirli sayı beklenmemiş; yanlışlıkla saklanan nesne referansı sonucu bozmuyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
