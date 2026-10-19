### 6.1.2. The Module Search Path

When a module named `spam` is imported, the interpreter first searches for a built-in module with that name. These module names are listed in `sys.builtin_module_names`. If not found, it then searches for a file named `spam.py` in a list of directories given by the variable `sys.path`. `sys.path` is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).

- `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`).

- The installation-dependent default (by convention including a `site-packages` directory, handled by the `site` module).

More details are at The initialization of the sys.path module search path.

> **Note**
>
> On file systems which support symlinks, the directory containing the input script is calculated after the symlink is followed. In other words the directory containing the symlink is **not** added to the module search path.

After initialization, Python programs can modify `sys.path`. The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended. See section Standard Modules for more information.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 6.1.2: Yanlış modülün neden seçildiğini bul**

**Odak:** sys.path kaynakları, arama önceliği, built-in ayrımı ve dosya adı çakışması.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1.1](../6.1.1-executing-modules-as-scripts/README.md).

##### Tek görev

1. Bir arama izi yaz: betik /work/app/run.py, PYTHONPATH içindeki yol /work/shared, varsayılan kitaplık yolu /python/lib olsun.

2. Hem /work/app/random.py hem kitaplığın random modülü var; /work/shared/helper.py de var. random ve helper için hangi kaynağın seçileceğini açıkla.

3. Sonra sys built-in olduğunda aynı klasörde sys.py bulunmasını ayrı değerlendir. run.py bir sembolik bağ üzerinden çağrılsaydı hangi dizinin ekleneceğini anlat.

4. Gerçek ortam değişkeni veya sistem dosyası değiştirmen gerekmiyor.

##### Geçiş ölçütleri

- [ ] random için betik dizinindeki dosya, helper için shared yolu seçilmiş.
- [ ] sys built-in aramasının yol aramasından önce olduğu ayrılmış.
- [ ] sys.path için betik dizini, PYTHONPATH ve varsayılan kurulum kaynakları belirtilmiş.
- [ ] Sembolik bağın bulunduğu yer yerine çözümlenmiş betik dizini kullanılıyor; dosya adının kitaplığı gölgelemesi açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../6.1.3-compiled-python-files/README.md)
<!-- learning-task:end -->
