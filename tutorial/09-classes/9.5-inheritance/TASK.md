# Görev 9.5: Üst metodun çağırdığı alt davranışı izle

**Odak:** Kalıtım, nitelik arama, override, taban metodu açık çağırma, isinstance/issubclass.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.4](../9.4-random-remarks/README.md).

## Tek görev

1. BaseCounter içinde kind niteliği, describe(self) içinde self.label() çağrısı, label(self) içinde "base" dönüşü olsun.

2. NamedCounter(BaseCounter) yalnız label metodunu "named" döndürecek biçimde değiştirsin.

3. Alt örnekte describe, kind, isinstance ve issubclass sonuçlarını göster.

4. Sonra alt label içinde BaseCounter.label(self) sonucuna ek metin ekleyerek genişlet.

## Geçiş ölçütleri

- [ ] Alt örnekte describe named döndürüyor; üst gövdedeki self.label alt override buluyor.
- [ ] kind üst sınıftan bulunuyor.
- [ ] Örnek/taban isinstance ve sınıf/taban issubclass doğru; ilgisiz tür karşılaştırması yanlış.
- [ ] Üst metodun açık çağrısında self verilmiş; henüz yalnız adı geçmiş super altyapısı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
