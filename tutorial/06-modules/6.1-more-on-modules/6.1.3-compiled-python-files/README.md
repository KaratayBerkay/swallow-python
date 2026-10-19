### 6.1.3. "Compiled" Python files

To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name `module.`*`version`*`.pyc`, where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.3 the compiled version of spam.py would be cached as `__pycache__/spam.cpython-33.pyc`. This naming convention allows compiled modules from different releases and different versions of Python to coexist.

Python checks the modification date of the source against the compiled version to see if it's out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that's loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

Some tips for experts:

- You can use the `-O` or `-OO` switches on the Python command to reduce the size of a compiled module. The `-O` switch removes assert statements, the `-OO` switch removes both assert statements and \_\_doc\_\_ strings. Since some programs may rely on having these available, you should only use this option if you know what you're doing. "Optimized" modules have an `opt-` tag and are usually smaller. Future releases may change the effects of optimization.

- A program doesn't run any faster when it is read from a `.pyc` file than when it is read from a `.py` file; the only thing that's faster about `.pyc` files is the speed with which they are loaded.

- The module `compileall` can create .pyc files for all modules in a directory.

- There is more detail on this process, including a flow chart of the decisions, in [**PEP 3147**](https://peps.python.org/pep-3147/).

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 6.1.3: Önbelleğin neyi hızlandırdığını ayır**

**Odak:** .pyc, sürüm etiketi, kaynak değişimi, doğrudan betik, -O/-OO ve derleme/yürütme ayrımı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1.2](../6.1.2-the-module-search-path/README.md).

##### Tek görev

1. counts.py için dört durumlu karar tablosu hazırla: önbellek yokken ilk import; aynı kaynak ve geçerli önbellekle yeni yorumlayıcıda import; kaynağın değişiklik tarihi değişip önbellek eski kaldığında yeni yorumlayıcıda import; dosyayı doğrudan betik olarak çalıştırma. Normal, önbellek yazılabilen bir çalışma klasörü varsay.

2. Her satırda kaynak derlenir mi, `__pycache__` kullanılabilir mi ve işlevin çalışma hızı hakkında ne söylenebilir yaz.

3. Kaynaksız dağıtımın özel yerleşimini, sürüm etiketini ve -O/-OO farkını ayrıca açıklayıp compileall aracının amacını belirt.

4. Kurulu dosyalarda önbellek silmen gerekmiyor.

##### Geçiş ölçütleri

- [ ] Verilen eski önbellek durumunda kaynak yeniden derleniyor; geçerli önbellek durumunda derlenmiş sürüm kullanılabiliyor. Karar, anlatımdaki değişiklik tarihi denetimine dayandırılmış.
- [ ] Aynı oturumdaki import cache ile disk bytecode cache ayrılmış.
- [ ] Doğrudan çalıştırılan ana betik için normal modül cache davranışı varsayılmamış.
- [ ] .pyc yüklemeyi hızlandırır; aynı kodun yürütmesini kendiliğinden hızlandırmaz.
- [ ] Sürüm etiketleri, kaynak olmadan .pyc yerleşimi ve platform bağımsızlığı doğru.
- [ ] -O assert, -OO ayrıca docstring kaldırma; compileall toplu derleme olarak açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
