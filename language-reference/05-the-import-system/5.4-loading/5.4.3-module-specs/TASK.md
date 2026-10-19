# Görev 5.4.3: Specin hangi sınırdan bilgi taşıdığını açıkla

**Odak:** Per-module import metadata, finder/loader arası taşıma ve `__spec__`.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.2](../5.4.2-submodules/README.md).

## Tek görev

1. math ve kendi küçük modülünü import edip `__spec__` değerlerini yalnız gözlemle.

2. Bir çizimde specin finder tarafından üretildiği yeri, import machinery ve loader tarafından kullanılma amacını göster.

3. Aynı isimli modülün verisini taşıyan `__dict__` ile import bilgisini taşıyan `__spec__` rollerini ayır; `__main__` için her zaman dolu olduğunu varsayma.

## Geçiş ölçütleri

- [ ] Spec modülün import bilgisi; kullanıcı iş verisi yerine konmamış.
- [ ] Finder -> spec -> machinery/loader ilişkisi doğru.
- [ ] `__spec__` modülden gözlemlenmiş; gösterimdeki adres veya her alanın aynı olması beklenmemiş.
- [ ] `__main__` istisnası belirtilmiş; ileride açıklanacak bütün başlatma türleri ezberden istenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
