### 5.4.2. Submodules

When a submodule is loaded using any mechanism (e.g. `importlib` APIs, the `import` or `import-from` statements, or built-in `__import__()`) a binding is placed in the parent module's namespace to the submodule object. For example, if package `spam` has a submodule `foo`, after importing `spam.foo`, `spam` will have an attribute `foo` which is bound to the submodule. Let's say you have the following directory structure:

``` python
spam/
    __init__.py
    foo.py
```

and `spam/__init__.py` has the following line in it:

``` python
from .foo import Foo
```
> Code: [spam/__init__.py](spam/__init__.py)

then executing the following puts name bindings for `foo` and `Foo` in the `spam` module:

``` python
>>> import spam
>>> spam.foo
<module 'spam.foo' from '/tmp/imports/spam/foo.py'>
>>> spam.Foo
<class 'spam.foo.Foo'>
```
> Code: [spam.py](spam.py)

Given Python's familiar name binding rules this might seem surprising, but it's actually a fundamental feature of the import system. The invariant holding is that if you have `sys.modules['spam']` and `sys.modules['spam.foo']` (as you would after the above import), the latter must appear as the `foo` attribute of the former.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.4.2: Alt modülün iki erişim yolunun aynı nesneye çıktığını göster**

**Odak:** Alt modül yüklenmesinin ebeveyn namespace üzerinde oluşturduğu bağ.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.1](../5.4.1-loaders/README.md).

##### Tek görev

1. Bölümdeki spam örneğini kendi çalışma kopyanda kullan. import spam sonrasında spam.foo ve spam.Foo adlarını incele. sys.modules["spam.foo"] is spam.foo ve sys.modules["spam"] is spam ilişkilerini karşılaştır.

2. Bir sınıfın dışarı aktarılmasıyla alt modül bağının neden aynı olay olmadığını açıkla.

##### Geçiş ölçütleri

- [ ] spam.foo modül, spam.Foo sınıf nesnesi.
- [ ] İki kimlik kontrolü de doğru.
- [ ] `__init__` yalnız Foo adını açıkça alsa bile alt modül ebeveynde foo niteliği olarak bağlı.
- [ ] Yerel kullanıcı adı ile ebeveyn modül niteliği ayrılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4.3-module-specs/README.md)
<!-- learning-task:end -->
