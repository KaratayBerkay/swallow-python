# Görev 8.9: Toplu hatadan yalnız seçilen türleri işle

**Odak:** ExceptionGroup, iç içe gruplar, except* ve işlenmeyen alt hataların yayılması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.8](../8.8-predefined-clean-up-actions/README.md).

## Tek görev

1. Bir grupta ValueError("a"), TypeError("b") ve içinde ValueError("c") ile OSError("d") bulunan alt grup oluştur.

2. İlk çalıştırmada except* ValueError, ikinci çalıştırmada ayrıca except* TypeError kullan.

3. Hangi hata yapraklarının işlendiğini ve hangilerinin kalan traceback içinde yer aldığını önceden çıkar.

4. Ayrı bir denemede except Exception ile grubun tamamını yakalamayı karşılaştır.

## Geçiş ölçütleri

- [ ] İlk denemede a ve c işleniyor; b ve d yayılıyor.
- [ ] İkinci denemede b de işleniyor; d kalıyor.
- [ ] İç içe grup ilişkileri düz ve ilişkisiz hata listesi sanılmamış.
- [ ] except Exception tek grup nesnesini yakalıyor; except* alt türleri seçiyor.
- [ ] Grupta sınıflar yerine hata örnekleri bulunuyor; eşzamanlı yürütme altyapısı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
