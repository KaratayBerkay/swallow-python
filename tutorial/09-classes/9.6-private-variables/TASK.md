# Görev 9.6: Ad çakışmasını erişim yasağından ayır

**Odak:** _ geleneği, __ ad dönüştürme, alt sınıf çakışması ve mangled ada erişim.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.5.1](../9.5-inheritance/9.5.1-multiple-inheritance/README.md).

## Tek görev

1. README içindeki Mapping/MappingSubclass örneğini kopyala.

2. MappingSubclass içinde ayrıca __update adlı, farklı mesaj yazdıran bir metot ekle.

3. Alt nesneyi başlangıç verisiyle oluştur; üst `__init__` içindeki çağrının hangi update işlevine gittiğini çıkar. _Mapping__update ile _MappingSubclass__update adlarını karşılaştır ve _internal, __internal, `__internal__` adlarının bölümdeki kurala göre durumlarını yaz.

## Geçiş ölçütleri

- [ ] Üst `__init__` kendi sınıfının dönüştürülmüş adına bağlı; alt __update bunu ezmiyor.
- [ ] Mangling biçimleri iki farklı sınıf adına göre doğru.
- [ ] Tek _ erişimi engellemez; çift baş/çift son adlar aynı mangling grubunda sayılmamış.
- [ ] Dönüştürülmüş ada erişimin mümkün olduğu ve bunun güvenlik sınırı olmadığı açıklanmış.
- [ ] getattr/exec gibi dinamik metinlerin aynı otomatik dönüşümü uygulamadığı kaynak notuyla açıklanmış; bunların API kullanımını yazman gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
