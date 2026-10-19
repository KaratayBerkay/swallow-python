# 5. The import system

Python code in one module gains access to the code in another module by the process of importing it. The `import` statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as `importlib.import_module()` and built-in `__import__()` can also be used to invoke the import machinery.

The `import` statement combines two operations; it searches for the named module, then it binds the results of that search to a name in the local scope. The search operation of the `import` statement is defined as a call to the `__import__()` function, with the appropriate arguments. The return value of `__import__()` is used to perform the name binding operation of the `import` statement. See the `import` statement for the exact details of that name binding operation.

A direct call to `__import__()` performs only the module search and, if found, the module creation operation. While certain side-effects may occur, such as the importing of parent packages, and the updating of various caches (including `sys.modules`), only the `import` statement performs a name binding operation.

When an `import` statement is executed, the standard builtin `__import__()` function is called. Other mechanisms for invoking the import system (such as `importlib.import_module()`) may choose to bypass `__import__()` and use their own solutions to implement import semantics.

When a module is first imported, Python searches for the module and if found, it creates a module object (See `types.ModuleType`.), initializing it. If the named module cannot be found, a `ModuleNotFoundError` is raised. Python implements various strategies to search for the named module when the import machinery is invoked. These strategies can be modified and extended by using various hooks described in the sections below.

Changed in version 3.3: The import system has been updated to fully implement the second phase of [**PEP 302**](https://peps.python.org/pep-0302/). There is no longer any implicit import machinery - the full import system is exposed through `sys.meta_path`. In addition, native namespace package support has been implemented (see [**PEP 420**](https://peps.python.org/pep-0420/)).


<!-- learning-task:start -->
## Bölüm görevi

**Görev 5: Modülü bulmayla ad bağlamayı ayır**

**Odak:** import arama/oluşturma ve yerel ad bağlama, doğrudan `__import__` çağrısının farkı.

### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.4.2](../../tutorial/06-modules/6.4-packages/6.4.2-intra-package-references/README.md).

### Tek görev

1. Ayrı yeni oturumlarda üç ifade için olay tablosu yaz: import math; `__import__`("math"); m = `__import__`("math").

2. Her satırda modülün bulunması/oluşması ve yerel kapsamda math veya m adının bağlanması olaylarını ayır. dir() ile bağlanan adları kontrol et.

3. Var olmayan benzersiz bir modül adı için hata türünü de belirt.

### Geçiş ölçütleri

- [ ] import math yerel math adını bağlıyor.
- [ ] Doğrudan `__import__` modülü döndürüyor, yerel math adı oluşturması beklenmiyor.
- [ ] Atama üçüncü durumda m adını bağlıyor.
- [ ] Bulunamayan modül ModuleNotFoundError; arama yan etkileri ile yerel ad bağlama ayrılmış.
- [ ] importlib gibi başka giriş yollarının `__import__` mekanizmasını atlayabileceği kaynak sınırlarıyla açıklanmış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.1-importlib/README.md)
<!-- learning-task:end -->
## Sections

- [5.1. `importlib`](5.1-importlib/README.md)
- [5.2. Packages](5.2-packages/README.md)
- [5.3. Searching](5.3-searching/README.md)
- [5.4. Loading](5.4-loading/README.md)
- [5.5. The Path Based Finder](5.5-the-path-based-finder/README.md)
- [5.6. Replacing the standard import system](5.6-replacing-the-standard-import-system/README.md)
- [5.7. Package Relative Imports](5.7-package-relative-imports/README.md)
- [5.8. Special considerations for \_\_main\_\_](5.8-special-considerations-for-main/README.md)
- [5.9. References](5.9-references/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Import sorununu doğru katmanda teşhis et**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Import sisteminin bütün işlenmiş katmanlarını tek inceleme ağacında kullanma.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. Bir geliştirici "aynı modülü değiştirip tekrar import ettim ama eski değeri gördüm; -m ile dosyadan çalıştırma da farklı" diyor.

2. Teşhis kaydında yerel ad bağlama, sys.modules, reload, meta path/path cache, bytecode geçerliliği, parent alt modül bağı, göreli import bağlamı ve `__main__.__spec__` katmanlarını ayır.

3. Üç kontrollü varyant için beklenen iz yaz: aynı oturumda tekrar import; yeni süreçte kaynak değişimi; -m ile ana giriş.

4. Hookları değiştirerek çözmek yerine eldeki bulgudan hangi katmanın sorumlu olduğunu gerekçelendir.

### Geçiş ölçütleri

- [ ] Aynı oturumun eski değerini önce modül cacheiyle açıklıyor; .pyc otomatik suçlanmıyor.
- [ ] Yeni süreçte kaynak/bytecode geçerliliği ayrı; finder cache modül nesnesi tutuyor sanılmamış.
- [ ] Reload kimliği, namespace/parent bağı ve göreli import tabanı tutarlı.
- [ ] -m ile dosya yolunun ana spec farkı doğru; import edilebilir nesneyle ana nesne ayrılmış.
- [ ] Güncel exec_module ile tarihsel load_module karıştırılmamış; bilgi eksikliği boş referans bölümlerinden tamamlanmış sayılmamış.
- [ ] Her öneri ilgili gözlemle destekli; gerçek import hook veya sistem ayarı değiştirilmemiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../../builtins/built-in-constants/README.md)
<!-- learning-milestone:end -->
