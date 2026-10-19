## 2.1. Invoking the Interpreter

The Python interpreter is usually installed as `/usr/local/bin/python3.15` on those machines where it is available; putting `/usr/local/bin` in your Unix shell's search path makes it possible to start it by typing the command:

``` text
python3.15
```

to the shell. (On Unix, the Python 3.x interpreter is by default not installed with the executable named `python`, so that it does not conflict with a simultaneously installed Python 2.x executable.) Since the choice of the directory where the interpreter lives is an installation option, other places are possible; check with your local Python guru or system administrator. (E.g., `/usr/local/python` is a popular alternative location.)

On Windows machines where you have installed Python from the Microsoft Store, the `python3.15` command will be available. If you have the py.exe launcher installed, you can use the `py` command. See Python install manager for other ways to launch Python.

Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn't work, you can exit the interpreter by typing the following command: `quit()`.

The interpreter's line-editing features include interactive editing, history substitution and code completion on most systems. Perhaps the quickest check to see whether command line editing is supported is typing a word in on the Python prompt, then pressing Left arrow (or Control-b). If the cursor moves, you have command line editing; see Appendix Interactive Input Editing and History Substitution for an introduction to the keys. If nothing appears to happen, or if a sequence like `^[[D` or `^B` appears, command line editing isn't available; you'll only be able to use backspace to remove characters from the current line.

The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a *script* from that file.

A second way of starting the interpreter is `python -c command [arg] ...`, which executes the statement(s) in *command*, analogous to the shell's `-c` option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote *command* in its entirety.

Some Python modules are also useful as scripts. These can be invoked using `python -m module [arg] ...`, which executes the source file for *module* as if you had spelled out its full name on the command line.

When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing `-i` before the script.

All command line options are described in Command line and environment.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 2.1: Python oturumunu doğru başlat**

**Odak:** Etkileşimli oturum, dosyadan çalıştırma, -c, -m, -i ve oturumdan çıkış.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.

#### Tek görev

1. Bir çalışma notunda şu beş ihtiyaca uygun başlatma biçimini yaz: komutları tek tek denemek; hazır demo.py dosyasını çalıştırmak; tek bir hazır Python komutunu çalıştırmak; adı verilen bir modülü program gibi çalıştırmak; demo.py bittikten sonra değişkenlerini oturumda incelemek.

2. Sonra bilgisayarındaki Python komutuyla etkileşimli oturumu aç, sol okla satır düzenlemeyi kontrol et ve bölümdeki çıkış yöntemlerinden biriyle kapat.

3. Python kodu üretmen gerekmiyor.

#### Geçiş ölçütleri

- [ ] Beş ihtiyaç sırasıyla etkileşimli başlangıç, dosya adı, -c, -m ve -i ile eşleştirilmiş.
- [ ] Python komutu ile >>> istemi birbirinden ayrılmış; komutun sistemindeki adı kaydedilmiş.
- [ ] EOF ile quit() yöntemlerinin amacı ve sol ok denemesinin sonucu açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](2.1.1-argument-passing/README.md)
<!-- learning-task:end -->
### Sections

- [2.1.1. Argument Passing](2.1.1-argument-passing/README.md)
- [2.1.2. Interactive Mode](2.1.2-interactive-mode/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Bir çalıştırma kaydını yeniden kur**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Başlatma biçimini, programa kalan argümanları ve REPL istemlerini birlikte yorumlama.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. demo.py için şu isteğe bir çalıştırma taslağı hazırla: red ve 7 programa verilsin, betik bitince oturumda kalınsın.

2. Komutu, sys.argv içeriğini ve betik sonrası birincil/devam istemlerinin görevini yaz.

3. Aynı betiği etkileşimli kalmadan çalıştıracak tek değişikliği göster.

#### Geçiş ölçütleri

- [ ] -i doğru yerde ve dosya adı/iki argüman korunmuş.
- [ ] Argümanlar metin, yorumlayıcı seçeneği argv içine katılmamış.
- [ ] Betik yürütmesiyle sonraki REPL evresi ayrılmış.
- [ ] İstemler kodun veya program çıktısının parçası yapılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../2.2-the-interpreter-and-its-environment/2.2.1-source-code-encoding/README.md)
<!-- learning-milestone:end -->
