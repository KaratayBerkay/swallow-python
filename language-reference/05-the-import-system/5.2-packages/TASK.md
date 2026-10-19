# Görev 5.2: Paket hiyerarşisini nesne modeliyle eşleştir

**Odak:** Her paketin modül olması, `__path__` ayırıcı niteliği ve dosya sistemi analojisinin sınırı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.1](../5.1-importlib/README.md).
- Ön bilgi: [t:6.4](../../../tutorial/06-modules/6.4-packages/README.md).

## Tek görev

1. email, email.mime ve email.mime.text adlarının ilişkisini çiz.

2. Kod yazmadan her düzeydeki ebeveyn/çocuk ilişkisini ve hangilerinin paket olduğunu kaynak örneğine göre belirt. "Bir modülün `__path__` niteliği var" ve "bir kaynağın disk üzerinde dizini yok" gözlemlerinden paket olup olmadığına dair ne çıkarılabileceğini açıkla.

## Geçiş ölçütleri

- [ ] email ve email.mime paket, email.mime.text modül olarak gösterilmiş.
- [ ] Paket modül ailesinin özel durumu; her modül paket sayılmamış.
- [ ] `__path__` paket ölçütü, disk dizini yalnız benzetme olarak ayrılmış.
- [ ] Kaynakların zip veya sanal yerlerden gelebileceği düşünülmüş; bu kaynakları açan yeni API gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
