### 5.8.1. \_\_main\_\_.\_\_spec\_\_

Depending on how `__main__` is initialized, `__main__.__spec__` gets set appropriately or to `None`.

When Python is started with the `-m` option, `__spec__` is set to the module spec of the corresponding module or package. `__spec__` is also populated when the `__main__` module is loaded as part of executing a directory, zipfile or other `sys.path` entry.

In the remaining cases `__main__.__spec__` is set to `None`, as the code used to populate the `__main__` does not correspond directly with an importable module:

- interactive prompt

- `-c` option

- running from stdin

- running directly from a source or bytecode file

Note that `__main__.__spec__` is always `None` in the last case, *even if* the file could technically be imported directly as a module instead. Use the `-m` switch if valid module metadata is desired in `__main__`.

Note also that even when `__main__` corresponds with an importable module and `__main__.__spec__` is set accordingly, they're still considered *distinct* modules. This is due to the fact that blocks guarded by `if __name__ == "__main__":` checks only execute when the module is used to populate the `__main__` namespace, and not during normal import.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.8.1: Çalıştırma biçimine göre ana specini belirle**

**Odak:** `__main__.__spec__` dolu/None durumları ve import edilebilir modülden ayrı kimlik.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.8](../README.md).
- Ön bilgi: [r:5.4.3](../../5.4-loading/5.4.3-module-specs/README.md).

##### Tek görev

1. Başlatma tablosu hazırla: python helper.py; python -m helper; -c; stdin; etkileşimli istem; dizin veya zip girişinden çalıştırma.

2. Her biri için ana `__name__` ve `__spec__` doluluk durumunu yaz. helper.py import edilebilir olmasına rağmen dosya yoluyla başlatılınca neden aynı metadata garantisinin oluşmadığını açıkla. -m ile çalışan ana nesne ile normal import helper nesnesini ayrı çiz.

##### Geçiş ölçütleri

- [ ] Hepsinde ana ad `__main__`; spec -m/dizin/zip için dolu, dosya/-c/stdin/etkileşimli durumda None.
- [ ] Dosyanın import edilebilir olması doğrudan dosya çalıştırmasında spec oluşturma garantisi değil.
- [ ] -m ile ana modül ve normal import edilen modül ayrı modül nesneleri olarak modellenmiş.
- [ ] Main korumasının yalnız ana girişte çalışması kimlik/başlatma farkına bağlanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
