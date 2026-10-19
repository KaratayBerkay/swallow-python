# Görev 5.7: Koşulun hangi kısmına gerçekten ulaşıldığını göster

**Odak:** Üyelik, kimlik/eşitlik, zincirli karşılaştırma, öncelik ve and/or kısa devresi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.6](../5.6-looping-techniques/README.md).
- Ön bilgi: [t:4.1](../../04-more-control-flow-tools/4.1-if-statements/README.md).

## Tek görev

1. a = [1], b = a, c = a[:] kur; == ile is sonuçlarını karşılaştır.

2. Sonra value = "" or "fallback" or "last" ifadesinin sonucunu; False and (1 / 0), True or (1 / 0) ifadelerinde hangi tarafın çalıştığını açıkla. x=3 ve x=7 için 0 < x < 5 dene.

3. A and not B or C ifadesini anlamı değişmeden parantezle; =, == ve bölümde adı geçen := rollerini sözle ayır.

## Geçiş ölçütleri

- [ ] a == c doğru, a is c yanlış, a is b doğru.
- [ ] or yalnız bool değil fallback metnini döndürüyor.
- [ ] Kısa devre nedeniyle iki bölme ifadesi de değerlendirilmemiş.
- [ ] Zincir koşulu 3 için doğru, 7 için yanlış; parantezler (A and (not B)) or C.
- [ ] in üyelik, is kimlik, == değer karşılaştırması; := ile yeni bir algoritma yazılması gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
