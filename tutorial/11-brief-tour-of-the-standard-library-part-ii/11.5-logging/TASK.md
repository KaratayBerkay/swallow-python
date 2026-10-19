# Görev 11.5: Görünmeyen kayıtla çalışmayan kodu karıştırma

**Odak:** Logging öncelikleri, varsayılan eşik, stderr ve mesaj yerleştirme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.4](../11.4-multi-threading/README.md).
- Ön bilgi: [t:10.4](../../10-brief-tour-of-the-standard-library/10.4-error-output-redirection-and-program-termination/README.md).

## Tek görev

1. Yeni bir betikte debug, info, warning, error ve critical seviyelerinde kendine ait beş mesaj üret. warning mesajına bölümdeki %s yöntemiyle "lesson.conf" değerini geçir.

2. Varsayılan yapılandırmada hangi mesajların çıktığını önce yaz, sonra çalıştır.

3. Bastırılan mesajların kodunun çalışmadığı sonucunun neden çıkarılamayacağını açıkla.

## Geçiş ölçütleri

- [ ] WARNING, ERROR, CRITICAL mesajları var; DEBUG ve INFO görünmüyor.
- [ ] Yerleştirilen dosya adı lesson.conf; log mesajı ile seviye ayrı.
- [ ] Varsayılan hedef stderr; ayrı yapılandırılmış oturum davranışı bu deneyle karıştırılmamış.
- [ ] Öncelik filtresi ile program yürütme koşulu ayrılmış; henüz gösterilmeyen handler yapılandırması istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
