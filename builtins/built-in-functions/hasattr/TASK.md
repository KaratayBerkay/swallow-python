# Görev b:3.31: hasattr davranışını ayırt et

## Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`class K: puan=4` ve `o=K()` için `hasattr(o,"puan")` ve `hasattr(o,"eksik")` sonuçlarını çalıştır. Ayrı bir hazır nesnenin nitelik okumasının AttributeError yerine ValueError yükselttiği verilmiş olsun; hasattr sonucunu yazılı çıkar. Bu nesnenin özel erişim mekanizmasını yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `ValueError`.
- [ ] Hasattr yalnız AttributeError durumunu False yapar; diğer hatayı yutmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
