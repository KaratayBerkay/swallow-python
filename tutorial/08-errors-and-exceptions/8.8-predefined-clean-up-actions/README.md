## 8.8. Predefined Clean-up Actions

Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. Look at the following example, which tries to open a file and print its contents to the screen.

``` python
for line in open("myfile.txt"):
    print(line, end="")
```
> Code: [example_01.py](example_01.py)

The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications. The `with` statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

``` python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
> Code: [example_02.py](example_02.py)

After the statement is executed, the file *f* is always closed, even if a problem was encountered while processing the lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.8: Blok hatayla bitse de dosyayı kapat**

**Odak:** with ile önceden tanımlı temizlik ve hata sonrası kaynak durumu.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.7](../8.7-defining-clean-up-actions/README.md).
- Ön bilgi: [t:7.2](../../07-input-and-output/7.2-reading-and-writing-files/README.md).

#### Tek görev

1. Kendi çalışma dosyanı with open(..., encoding="utf-8") as f ile aç; ilk satırdan sonra bilerek ValueError yükselt.

2. Dıştaki try/except içinde hatayı yakaladıktan sonra f.closed kontrol et.

3. Aynı akışın with kullanmadan yazılan taslağında close satırına neden ulaşılamayacağını göster.

#### Geçiş ölçütleri

- [ ] Hata yakalandıktan sonra f.closed True.
- [ ] Hata with bloğu içinde oluşmuş; temizlik yalnız başarı yolunda sınanmamış.
- [ ] with kaynağın temizliğini, except hataya verilen tepkiyi yönetiyor.
- [ ] Kendi context manager sınıfını yazmak veya özel metot API bilgisi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.9-raising-and-handling-multiple-unrelated-exceptions/README.md)
<!-- learning-task:end -->
