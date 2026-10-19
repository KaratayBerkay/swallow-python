### 16.1.1. Error Handling

When an error occurs, the interpreter prints an error message and a stack trace. In interactive mode, it then returns to the primary prompt; when input came from a file, it exits with a nonzero exit status after printing the stack trace. (Exceptions handled by an `except` clause in a `try` statement are not errors in this context.) Some errors are unconditionally fatal and cause an exit with a nonzero exit status; this applies to internal inconsistencies and some cases of running out of memory. All error messages are written to the standard error stream; normal output from executed commands is written to standard output.

Typing the interrupt character (usually Control-C or Delete) to the primary or secondary prompt cancels the input and returns to the primary prompt. (A problem with the GNU Readline package may prevent this.) Typing an interrupt while a command is executing raises the `KeyboardInterrupt` exception, which may be handled by a `try` statement.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 16.1.1: Aynı hatanın betikle oturumda farklı sonunu göster**

**Odak:** REPL geri dönüşü, betik çıkışı, stderr/stdout ve KeyboardInterrupt.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1](../README.md).
- Ön bilgi: [t:8.3](../../../08-errors-and-exceptions/8.3-handling-exceptions/README.md).

##### Tek görev

1. 1 / 0 ifadesini REPL içinde dene, ardından yeni bir ifade çalıştır.

2. Aynı hatadan sonra print("after") olan küçük betiği ayrı çalıştır; yürütmenin nereye kadar geldiğini karşılaştır.

3. Sonra betikte hatayı uygun except ile yakala ve after çıktısını kontrol et.

4. Ctrl+C ile giriş iptali ve çalışan komutu kesme durumlarını bölümden yazılı karşılaştır.

##### Geçiş ölçütleri

- [ ] REPL hata sonrası birincil isteme dönüp yeni komutu kabul ediyor.
- [ ] Yakalanmayan betik hatası after satırına ulaşmıyor; yakalanan sürüm ulaşıyor.
- [ ] Hata stderr, normal çıktı stdout olarak ayrılmış; yakalanmayan betiğin sıfır dışı çıkışı belirtilmiş.
- [ ] Komut girerken iptal ile yürütürken KeyboardInterrupt üretme ayrılmış; fatal sistem hatası yaratmak gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../16.1.2-executable-python-scripts/README.md)
<!-- learning-task:end -->
