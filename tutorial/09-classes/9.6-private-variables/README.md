## 9.6. Private Variables

"Private" instance variables that cannot be accessed except from inside an object don't exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. `_spam`) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called *name mangling*. Any identifier of the form `__spam` (at least two leading underscores, at most one trailing underscore) is textually replaced with `_classname__spam`, where `classname` is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

> **See also**
>
> The private name mangling specifications for details and special cases.

Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

``` python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
> Code: [init.py](init.py)

The above example would work even if `MappingSubclass` were to introduce a `__update` identifier since it is replaced with `_Mapping__update` in the `Mapping` class and `_MappingSubclass__update` in the `MappingSubclass` class respectively.

Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

Notice that code passed to `exec()` or `eval()` does not consider the classname of the invoking class to be the current class; this is similar to the effect of the `global` statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to `getattr()`, `setattr()` and `delattr()`, as well as when referencing `__dict__` directly.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.6: Ad çakışmasını erişim yasağından ayır**

**Odak:** _ geleneği, __ ad dönüştürme, alt sınıf çakışması ve mangled ada erişim.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.5.1](../9.5-inheritance/9.5.1-multiple-inheritance/README.md).

#### Tek görev

1. README içindeki Mapping/MappingSubclass örneğini kopyala.

2. MappingSubclass içinde ayrıca __update adlı, farklı mesaj yazdıran bir metot ekle.

3. Alt nesneyi başlangıç verisiyle oluştur; üst `__init__` içindeki çağrının hangi update işlevine gittiğini çıkar. _Mapping__update ile _MappingSubclass__update adlarını karşılaştır ve _internal, __internal, `__internal__` adlarının bölümdeki kurala göre durumlarını yaz.

#### Geçiş ölçütleri

- [ ] Üst `__init__` kendi sınıfının dönüştürülmüş adına bağlı; alt __update bunu ezmiyor.
- [ ] Mangling biçimleri iki farklı sınıf adına göre doğru.
- [ ] Tek _ erişimi engellemez; çift baş/çift son adlar aynı mangling grubunda sayılmamış.
- [ ] Dönüştürülmüş ada erişimin mümkün olduğu ve bunun güvenlik sınırı olmadığı açıklanmış.
- [ ] getattr/exec gibi dinamik metinlerin aynı otomatik dönüşümü uygulamadığı kaynak notuyla açıklanmış; bunların API kullanımını yazman gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.7-odds-and-ends/README.md)
<!-- learning-task:end -->
