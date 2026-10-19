## 5.2. Packages

Python has only one type of module object, and all modules are of this type, regardless of whether the module is implemented in Python, C, or something else. To help organize modules and provide a naming hierarchy, Python has a concept of packages.

You can think of packages as the directories on a file system and modules as files within directories, but don't take this analogy too literally since packages and modules need not originate from the file system. For the purposes of this documentation, we'll use this convenient analogy of directories and files. Like file system directories, packages are organized hierarchically, and packages may themselves contain subpackages, as well as regular modules.

It's important to keep in mind that all packages are modules, but not all modules are packages. Or put another way, packages are just a special kind of module. Specifically, any module that contains a `__path__` attribute is considered a package.

All modules have a name. Subpackage names are separated from their parent package name by a dot, akin to Python's standard attribute access syntax. Thus you might have a package called `email`, which in turn has a subpackage called `email.mime` and a module within that subpackage called `email.mime.text`.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.2: Paket hiyerarşisini nesne modeliyle eşleştir**

**Odak:** Her paketin modül olması, `__path__` ayırıcı niteliği ve dosya sistemi analojisinin sınırı.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.1](../5.1-importlib/README.md).
- Ön bilgi: [t:6.4](../../../tutorial/06-modules/6.4-packages/README.md).

#### Tek görev

1. email, email.mime ve email.mime.text adlarının ilişkisini çiz.

2. Kod yazmadan her düzeydeki ebeveyn/çocuk ilişkisini ve hangilerinin paket olduğunu kaynak örneğine göre belirt. "Bir modülün `__path__` niteliği var" ve "bir kaynağın disk üzerinde dizini yok" gözlemlerinden paket olup olmadığına dair ne çıkarılabileceğini açıkla.

#### Geçiş ölçütleri

- [ ] email ve email.mime paket, email.mime.text modül olarak gösterilmiş.
- [ ] Paket modül ailesinin özel durumu; her modül paket sayılmamış.
- [ ] `__path__` paket ölçütü, disk dizini yalnız benzetme olarak ayrılmış.
- [ ] Kaynakların zip veya sanal yerlerden gelebileceği düşünülmüş; bu kaynakları açan yeni API gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.2.1-regular-packages/README.md)
<!-- learning-task:end -->
### Sections

- [5.2.1. Regular packages](5.2.1-regular-packages/README.md)
- [5.2.2. Namespace packages](5.2.2-namespace-packages/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: İki paket türünü aynı ağaçta çöz**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Regular başlangıç kodu ile namespace portion birleşiminin ayrımı.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Bir kökte `__init__` içeren app paketi, app altında `__init__` içermeyen plugins dizini; iki ayrı arama kökünde __init__siz extras paketinin farklı alt modülleri olsun.

2. Her import için paket türünü, çalışacak başlangıç dosyalarını ve kaynakların neden tek fiziksel kök zorunluluğu taşımadığını çiz.

3. Çizime yeni bir portion eklendiğinde arama yolunun hangi olayda güncelleneceğini ekle.

#### Geçiş ölçütleri

- [ ] app regular; app.plugins namespace alt paket olarak doğru.
- [ ] extras portionları tek namespace altında birleşiyor.
- [ ] Namespace için sahte `__init__` yürütmesi varsayılmamış.
- [ ] Yol değişimini yeniden arama ilişkisiyle açıklayabiliyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.3-searching/README.md)
<!-- learning-milestone:end -->
