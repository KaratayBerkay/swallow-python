### 16.1.2. Executable Python Scripts

On BSD'ish Unix systems, Python scripts can be made directly executable, like shell scripts, by putting the line

``` python
#!/usr/bin/env python3
```
> Code: [example_01.py](example_01.py)

(assuming that the interpreter is on the user's `PATH`) at the beginning of the script and giving the file an executable mode. The `#!` must be the first two characters of the file. On some platforms, this first line must end with a Unix-style line ending (`'\n'`), not a Windows (`'\r\n'`) line ending. Note that the hash, or pound, character, `'#'`, is used to start a comment in Python.

The script can be given an executable mode, or permission, using the **chmod** command.

``` console
$ chmod +x myscript.py
```

On Windows systems, there is no notion of an "executable mode". The Python installer automatically associates `.py` files with `python.exe` so that a double-click on a Python file will run it as a script. The extension can also be `.pyw`, in that case, the console window that normally appears is suppressed.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 16.1.2: Çalıştırılabilir betiğin başlığını doğrula**

**Odak:** Shebang konumu, PATH, yürütme izni ve Unix/Windows farkı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1.1](../16.1.1-error-handling/README.md).
- Ön bilgi: [t:2.2.1](../../../02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/2.2.1-source-code-encoding/README.md).

##### Tek görev

1. Kendi klasöründe print("ready") yazan betiğin başına bölümdeki shebang satırını koy.

2. Unix için chmod +x ve betik yolu üzerinden çalıştırma planını yaz; mümkünse yalnız bu dosyada dene.

3. Shebang önüne boş satır eklemenin, python3 komutunun PATH içinde olmamasının ve CRLF satır sonunun neden ayrı sorunlar olduğunu açıkla.

4. Windows .py/.pyw farkını kaynakla eşleştir.

##### Geçiş ölçütleri

- [ ] #! dosyanın ilk iki karakteri ve shebang ilk satır.
- [ ] Yürütme izniyle yorumlayıcı bulunması ayrı koşullar.
- [ ] Encoding bildirimi gerekirse ikinci satıra yerleştirilmiş.
- [ ] Windows ilişkilendirmesi Unix izniyle karıştırılmamış; .pyw konsol davranışı belirtilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../16.1.3-the-interactive-startup-file/README.md)
<!-- learning-task:end -->
