# Görev 16.1.1: Aynı hatanın betikle oturumda farklı sonunu göster

**Odak:** REPL geri dönüşü, betik çıkışı, stderr/stdout ve KeyboardInterrupt.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1](../README.md).
- Ön bilgi: [t:8.3](../../../08-errors-and-exceptions/8.3-handling-exceptions/README.md).

## Tek görev

1. 1 / 0 ifadesini REPL içinde dene, ardından yeni bir ifade çalıştır.

2. Aynı hatadan sonra print("after") olan küçük betiği ayrı çalıştır; yürütmenin nereye kadar geldiğini karşılaştır.

3. Sonra betikte hatayı uygun except ile yakala ve after çıktısını kontrol et.

4. Ctrl+C ile giriş iptali ve çalışan komutu kesme durumlarını bölümden yazılı karşılaştır.

## Geçiş ölçütleri

- [ ] REPL hata sonrası birincil isteme dönüp yeni komutu kabul ediyor.
- [ ] Yakalanmayan betik hatası after satırına ulaşmıyor; yakalanan sürüm ulaşıyor.
- [ ] Hata stderr, normal çıktı stdout olarak ayrılmış; yakalanmayan betiğin sıfır dışı çıkışı belirtilmiş.
- [ ] Komut girerken iptal ile yürütürken KeyboardInterrupt üretme ayrılmış; fatal sistem hatası yaratmak gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
