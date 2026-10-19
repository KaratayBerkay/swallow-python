### 5.4.6. Cached bytecode invalidation

Before Python loads cached bytecode from a `.pyc` file, it checks whether the cache is up-to-date with the source `.py` file. By default, Python does this by storing the source's last-modified timestamp and size in the cache file when writing it. At runtime, the import system then validates the cache file by checking the stored metadata in the cache file against the source's metadata.

Python also supports "hash-based" cache files, which store a hash of the source file's contents rather than its metadata. There are two variants of hash-based `.pyc` files: checked and unchecked. For checked hash-based `.pyc` files, Python validates the cache file by hashing the source file and comparing the resulting hash with the hash in the cache file. If a checked hash-based cache file is found to be invalid, Python regenerates it and writes a new checked hash-based cache file. For unchecked hash-based `.pyc` files, Python simply assumes the cache file is valid if it exists. Hash-based `.pyc` files validation behavior may be overridden with the `--check-hash-based-pycs` flag.

Changed in version 3.7: Added hash-based `.pyc` files. Previously, Python only supported timestamp-based invalidation of bytecode caches.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.4.6: Bytecode geçerliliğini politika bazında ayır**

**Odak:** Timestamp/size kontrolü ve checked/unchecked hash cache ayrımı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.5](../5.4.5-module-reprs/README.md).
- Ön bilgi: [t:6.1.3](../../../../tutorial/06-modules/6.1-more-on-modules/6.1.3-compiled-python-files/README.md).

##### Tek görev

1. Üç sütunlu cache karar tablosu hazırla: timestamp+size, checked hash, unchecked hash.

2. Kaynağın zamanı/boyutu aynı kalırken içeriği değişmiş olsun; her politikada hangi verinin kontrol edildiğini, farkın fark edilip edilmeyebileceğini ve geçersiz checked hash durumunda ne olacağını yaz. --check-hash-based-pycs seçeneğinin hangi kararı etkileyebildiğini sözle belirt.

##### Geçiş ölçütleri

- [ ] Metadata politikası yalnız zaman/boyut bilgisiyle karar veriyor; aynı metadata içerik değişimini kaçırabilir.
- [ ] Checked hash kaynak içeriğini hashleyip karşılaştırıyor ve geçersizse yeni checked cache üretiyor.
- [ ] Unchecked var olan cachei normalde geçerli kabul ediyor; bu davranış seçeneğe bağlı değişebilir.
- [ ] Cache politikası program sonucunun doğruluğuyla, .pyc yükleme hızıyla karıştırılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
