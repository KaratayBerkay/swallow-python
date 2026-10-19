### 5.4.5. Module reprs

By default, all modules have a usable repr, however depending on the attributes set above, and in the module's spec, you can more explicitly control the repr of module objects.

If the module has a spec (`__spec__`), the import machinery will try to generate a repr from it. If that fails or there is no spec, the import system will craft a default repr using whatever information is available on the module. It will try to use the `module.__name__`, `module.__file__`, and `module.__loader__` as input into the repr, with defaults for whatever information is missing.

Here are the exact rules used:

- If the module has a `__spec__` attribute, the information in the spec is used to generate the repr. The "name", "loader", "origin", and "has_location" attributes are consulted.

- If the module has a `__file__` attribute, this is used as part of the module's repr.

- If the module has no `__file__` but does have a `__loader__` that is not `None`, then the loader's repr is used as part of the module's repr.

- Otherwise, just use the module's `__name__` in the repr.

Changed in version 3.12: Use of `module_repr()`, having been deprecated since Python 3.4, was removed in Python 3.12 and is no longer called during the resolution of a module's repr.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.4.5: Modül temsilinin yedek bilgi sırasını çıkar**

**Odak:** repr için spec, file, loader ve name önceliği.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.4](../5.4.4-path-attributes-on-modules/README.md).

##### Tek görev

1. Dört varsayımsal modül için repr bilgi kaynağını yaz: kullanılabilir spec var; spec yok ama `__file__` var; ikisi yok ama `__loader__` None değil; yalnız `__name__` var.

2. İlk durumdaki spec alanlarını kaynakta verilen adlarıyla işaretle.

3. Amaç tam repr metnini ezberlemek değil, hangi bilgiye başvurulduğunu göstermek.

##### Geçiş ölçütleri

- [ ] Öncelik spec, file, loader, name olarak doğru.
- [ ] Spec için name/loader/origin/has_location belirtilmiş.
- [ ] Eksik bilgi repr üretimini zorunlu olarak durdurmuyor.
- [ ] 3.12 ile kaldırılan module_repr çağrısı güncel akışa eklenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4.6-cached-bytecode-invalidation/README.md)
<!-- learning-task:end -->
