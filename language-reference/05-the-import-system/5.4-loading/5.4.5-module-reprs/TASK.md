# Görev 5.4.5: Modül temsilinin yedek bilgi sırasını çıkar

**Odak:** repr için spec, file, loader ve name önceliği.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.4](../5.4.4-path-attributes-on-modules/README.md).

## Tek görev

1. Dört varsayımsal modül için repr bilgi kaynağını yaz: kullanılabilir spec var; spec yok ama `__file__` var; ikisi yok ama `__loader__` None değil; yalnız `__name__` var.

2. İlk durumdaki spec alanlarını kaynakta verilen adlarıyla işaretle.

3. Amaç tam repr metnini ezberlemek değil, hangi bilgiye başvurulduğunu göstermek.

## Geçiş ölçütleri

- [ ] Öncelik spec, file, loader, name olarak doğru.
- [ ] Spec için name/loader/origin/has_location belirtilmiş.
- [ ] Eksik bilgi repr üretimini zorunlu olarak durdurmuyor.
- [ ] 3.12 ile kaldırılan module_repr çağrısı güncel akışa eklenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
