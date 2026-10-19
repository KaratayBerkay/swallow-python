## 10.3. Command-line arguments

Common utility scripts often need to process command-line arguments. These arguments are stored in the `sys` module's *argv* attribute as a list. For instance, let's take the following `demo.py` file:

``` python
# File demo.py
import sys
print(sys.argv)
```
> Code: [demo.py](demo.py)

Here is the output from running `python demo.py one two three` at the command line:

``` python
['demo.py', 'one', 'two', 'three']
```
> Code: [example_01.py](example_01.py)

The `argparse` module provides a more sophisticated mechanism to process command-line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed:

``` python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
> Code: [parser.py](parser.py)

When run at the command line with `python top.py --lines=5 alpha.txt beta.txt`, the script sets `args.lines` to `5` and `args.filenames` to `['alpha.txt', 'beta.txt']`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.3: Komut satırının sözleşmesini sınırda kontrol et**

**Odak:** argparse konumsal çoklu değer, int dönüşümü, seçenek adı ve varsayılan.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.2](../10.2-file-wildcards/README.md).
- Ön bilgi: [t:2.1.1](../../02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.1-argument-passing/README.md).

#### Tek görev

1. Bölümdeki parser iskeletini kopyala: filenames nargs="+", -l/--lines type=int ve default=10 kalsın.

2. Dosya okumadan yalnız ayrıştırılan değerleri göster.

3. İki dosya adı; --lines=3 ile iki dosya; -l 0 ile bir dosya; hiç dosya vermeme; --lines=bad ile bir dosya senaryolarını ayrı çalıştır.

4. Aynı girdinin sys.argv içinde neye benzediğini karşılaştır.

#### Geçiş ölçütleri

- [ ] Seçenek yokken lines 10; diğer geçerli değerler 3 ve 0, türleri int.
- [ ] filenames sıra korunmuş metin listesi.
- [ ] Eksik zorunlu konumsal ve geçersiz int girdileri parser tarafından reddediliyor.
- [ ] sys.argv ham metinler ile argparse sonucu aynı yapı sanılmamış; dosya açma bu göreve eklenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.4-error-output-redirection-and-program-termination/README.md)
<!-- learning-task:end -->
