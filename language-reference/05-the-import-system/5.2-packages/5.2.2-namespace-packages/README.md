### 5.2.2. Namespace packages

A namespace package is a composite of various portions, where each portion contributes a subpackage to the parent package. Portions may reside in different locations on the file system. Portions may also be found in zip files, on the network, or anywhere else that Python searches during import. Namespace packages may or may not correspond directly to objects on the file system; they may be virtual modules that have no concrete representation.

Namespace packages do not use an ordinary list for their `__path__` attribute. They instead use a custom iterable type which will automatically perform a new search for package portions on the next import attempt within that package if the path of their parent package (or `sys.path` for a top level package) changes.

With namespace packages, there is no `parent/__init__.py` file. In fact, there may be multiple `parent` directories found during import search, where each one is provided by a different portion. Thus `parent/one` may not be physically located next to `parent/two`. In this case, Python will create a namespace package for the top-level `parent` package whenever it or one of its subpackages is imported.

Namespace packages may also be nested inside a regular package. When the import system searches a regular package's `__path__` and encounters a subdirectory that does not contain an `__init__.py` file, that subdirectory becomes a portion contributing to a namespace subpackage of the enclosing regular package.

See also [**PEP 420**](https://peps.python.org/pep-0420/) for the namespace package specification.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.2.2: Ayrı konumlardan tek namespace paketi kurulduğunu izle**

**Odak:** Namespace portion, `__init__` yokluğu, dinamik `__path__` ve iç içe paket.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.2.1](../5.2.1-regular-packages/README.md).

##### Tek görev

1. Yazılı bir import haritası çiz: /a/parent/one ve /b/parent/two var; parent dizinlerinde `__init__`.py yok, /a ve /b arama yolunda. parent ve iki alt öğenin nasıl aynı ad ağacında birleştiğini göster.

2. Sonra arama yoluna /c eklenip /c/parent/three bulunduğunda sonraki aramanın neyi yeniden değerlendireceğini açıkla.

3. Regular paket içindeki __init__siz alt klasör durumunu da çizime ekle.

##### Geçiş ölçütleri

- [ ] parent tek namespace paket, iki kök ayrı portion olarak gösterilmiş.
- [ ] parent için zorunlu tek bir fiziksel dizin veya `__init__` varsayılmamış.
- [ ] `__path__` düz sabit liste sanılmamış; ebeveyn yolu değişince yeni portion araması açıklanmış.
- [ ] Regular paket içinde namespace alt paket olasılığı doğru; yeni finder uygulamak gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
