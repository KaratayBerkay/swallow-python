### 2.1.2. Interactive Mode

When commands are read from a tty, the interpreter is said to be in *interactive mode*. In this mode it prompts for the next command with the *primary prompt*, usually three greater-than signs (`>>>`); for continuation lines it prompts with the *secondary prompt*, by default three dots (`...`). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt:

``` console
$ python3.15
Python 3.15 (default, May 7 2025, 15:46:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Continuation lines are needed when entering a multi-line construct. As an example, take a look at this `if` statement:

``` python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```
> Code: [the_world_is_flat.py](the_world_is_flat.py)

For more on interactive mode, see Interactive Mode.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 2.1.2: Çok satırlı örneği REPL içinde tamamla**

**Odak:** Birincil ve devam istemleri, girinti, boş satırla bloğu tamamlama, girdi ve çıktı ayrımı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:2.1](../README.md).

##### Tek görev

1. README içindeki the_world_is_flat örneğini etkileşimli oturuma gir; yalnızca mesajı "Ground checked." yap.

2. Her satırdan önce gördüğün istemi ve çıktının hangi girişten sonra oluştuğunu not et. if yapısının iç işleyişini açıklaman gerekmiyor; burada verilen bloğu doğru girmek ölçülüyor.

##### Geçiş ölçütleri

- [ ] >>> ve ... karakterleri Python kodunun parçası olarak yazılmamış.
- [ ] Girintili satırdan sonra boş satır girilmiş ve mesaj bir kez basılmış.
- [ ] Karşılama metni, giriş satırları, devam istemi ve program çıktısı doğru ayrılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
