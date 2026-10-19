## 12.2. Creating Virtual Environments

The module used to create and manage virtual environments is called `venv`. `venv` will install the Python version from which the command was run (as reported by the `--version` option). For instance, executing the command with `python3.12` will install version 3.12.

To create a virtual environment, decide upon a directory where you want to place it, and run the `venv` module as a script with the directory path:

``` bash
python -m venv tutorial-env
```
> Command: [example_01.sh](example_01.sh)

This will create the `tutorial-env` directory if it doesn't exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

A common directory location for a virtual environment is `.venv`. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with `.env` environment variable definition files that some tooling supports.

Once you've created a virtual environment, you may activate it.

On Windows, run:

``` console
tutorial-env\Scripts\activate
```
> Command: [example_02.sh](example_02.sh)

On Unix or MacOS, run:

``` bash
source tutorial-env/bin/activate
```
> Command: [example_03.sh](example_03.sh)

(This script is written for the bash shell. If you use the **csh** or **fish** shells, there are alternate `activate.csh` and `activate.fish` scripts you should use instead.)

Activating the virtual environment will change your shell's prompt to show what virtual environment you're using, and modify the environment so that running `python` will get you that particular version and installation of Python. For example:

``` console
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

Note that the activated virtual environment does not alter the `PYTHONPATH` variable in any way. This may lead to unexpected results if the path includes references to code which is incompatible with the Python version the virtual environment is using. The best practice is to `unset PYTHONPATH` in bash or the equivalent for the shell you are using.

To deactivate a virtual environment, type:

``` bash
deactivate
```
> Command: [example_04.sh](example_04.sh)

into the terminal.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 12.2: Oluşturma ile etkinleştirmeyi ayır**

**Odak:** venv yorumlayıcı seçimi, activate/deactivate, sys.path ve PYTHONPATH sınırı.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:12.1](../12.1-introduction/README.md).
- Ön bilgi: [t:6.2](../../06-modules/6.2-standard-modules/README.md).

#### Tek görev

1. Yeni bir terminal oturumunda mevcut python --version sonucunu ve REPL içinde import sys sonrası sys.path listesini kaydet; quit() ile REPLden çık.

2. Kendi çalışma klasöründe henüz bulunmayan lesson-env dizinini python -m venv lesson-env ile oluştur. Bölümde işletim sistemin ve shellin için verilen activate yolunu kullan. Etkin ortamda python --version ve REPL içindeki sys.path gözlemini tekrarla; ortamın site-packages yolunu işaretle.

3. REPLden çıkıp deactivate çalıştır. Aynı gözlemi tekrar alarak terminalin önceki yorumlayıcı seçimine döndüğünü doğrula. Sürüm numarasının aynı kalmasının, ortamın değişmediği anlamına neden gelmediğini açıkla.

4. Python 3.12 yerine 3.11 ile ortam oluşturmanın sonucu, .venv/.env ayrımı ve PYTHONPATH sınırını not et. Paket indirme, global ayar değiştirme veya yeni yorumlayıcı kurma yok.

Kurulu yorumlayıcı venv oluşturmayı engelliyorsa gerçek hata kaydını sun; sistem kurulumu çözmek bu görevin kapsamı değildir. Uygulama kanıtı sağlanana kadar karar Kanıt bekleniyor olur; komut taslağı tek başına uygulama kanıtı sayılmaz.

#### Geçiş ölçütleri

- [ ] venv kendisini çağıran Python sürümüyle oluşuyor; istenen başka sürümü kendiliğinden indirmiyor.
- [ ] Yerel lesson-env gerçekten oluşturulmuş; oluşturma ile shell içinde etkinleştirme ayrı olaylar olarak gösterilmiş.
- [ ] Önce/etkin/sonra gözlemleri var; etkin ortamın site-packages yolu sys.path içinde gösterilmiş. Yalnız istemdeki etikete veya sürüm numarasına bakılmamış.
- [ ] deactivate sonrasında önceki terminal seçimine dönüldüğü gerçek gözlemle doğrulanmış.
- [ ] Aktivasyon PYTHONPATH içeriğini temizleme garantisi vermiyor.
- [ ] Windows ve Unix yolları karıştırılmamış; .env değişken dosyası ile .venv dizini ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../12.3-managing-packages-with-pip/README.md)
<!-- learning-task:end -->
