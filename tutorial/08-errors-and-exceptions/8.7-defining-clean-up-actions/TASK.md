# Görev 8.7: Temizliği bütün çıkış yollarında izle

**Odak:** finally ile normal/hatalı çıkış, return ve hata bastırma riski.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.5](../8.5-exception-chaining/README.md).

## Tek görev

1. README içindeki divide örneğinin kopyasında her bölüme farklı kısa bir işaret koy. (6, 2), (6, 0) ve ("6", "2") için try/except/else/finally sırasını önce çıkar, sonra çalıştır.

2. Ayrı bir fonksiyonda try içinden 1 döndür; finally yalnız mesaj bassın.

3. Sonra finally içine return 2 ekle ve dönen değer ile bir hata durumuna etkisini karşılaştır.

## Geçiş ölçütleri

- [ ] Normal yol else ve finally; sıfır yolunda except ve finally; tip hatasında finally sonrası yayılma.
- [ ] finally temizliği hatayı kendiliğinden çözmüyor.
- [ ] Yalnız mesajlı finally dönüş 1 değerini koruyor; return 2 eklenince sonuç 2.
- [ ] finally içindeki return hatayı da bastırabilir; bu yüzden temizliğe kontrol akışı ekleme riski açıklanmış.
- [ ] 3.14+ SyntaxWarning farkı bölümdeki sürüm notuyla ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
