# 3. An Informal Introduction to Python

In the following examples, input and output are distinguished by the presence or absence of prompts (\>\>\> and ...): to repeat the example, you must type everything after the prompt, when the prompt appears; lines that do not begin with a prompt are output from the interpreter. Note that a secondary prompt on a line by itself in an example means you must type a blank line; this is used to end a multi-line command.

You can use the "Copy" button (it appears in the upper-right corner when hovering over or tapping a code example), which strips prompts and omits output, to copy and paste the input lines into your interpreter.

Many of the examples in this manual, even those entered at the interactive prompt, include comments. Comments in Python start with the hash character, `#`, and extend to the end of the physical line. A comment may appear at the start of a line or following whitespace or code, but not within a string literal. A hash character within a string literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.

Some examples:

``` python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```
> Code: [spam.py](spam.py)


<!-- learning-task:start -->
## Bölüm görevi

**Görev 3: Örnekten yalnızca Python girdisini ayır**

**Odak:** İstem, çıktı ve yorum ayrımı; tırnak içindeki # karakteri.

### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:2.1.2](../02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.2-interactive-mode/README.md).

### Tek görev

1. README içindeki spam örneğini kendi dosyana aktar.

2. Değişken adlarını koruyup sayıyı 2, metni "# lesson note" yap.

3. Ardından notunda bir REPL örneğini dosyaya geçirirken >>>, ..., sonuç satırları ve tek başına devam isteminin nasıl ele alınacağını açıkla.

### Geçiş ölçütleri

- [ ] Dosyada istem veya örnek çıktı satırı yok.
- [ ] Satır başındaki ve kod sonundaki yorumlar yorum olarak; metindeki # ise veri olarak tanımlanmış.
- [ ] Boş devam satırının REPL içinde bloğu bitirdiği açıklanmış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](3.1-using-python-as-a-calculator/3.1.1-numbers/README.md)
<!-- learning-task:end -->
## Sections

- [3.1. Using Python as a Calculator](3.1-using-python-as-a-calculator/README.md)
- [3.2. First Steps Towards Programming](3.2-first-steps-towards-programming/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Bir sonraki değeri eski durumdan üret**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Sayı, metin, liste, while ve eşzamanlı atamayı bir araya getirme.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. a=1, b=2 ile başlayıp a < 15 oldukça a değerini bir sonuç listesine ekleyen while programı yaz; her turda a, b = b, a+b kullan.

2. Sonuç listesinin ilk/son öğesini ve uzunluğunu göster; bir dilim kopyası üzerinden ilk değeri değiştirip kaynağın korunduğunu doğrula.

3. Sayıları print end ile aynı satıra yaz.

4. İlk üç turu elle izleyip eşzamanlı atama yerine iki sıradan atamanın farkını açıkla.

### Geçiş ölçütleri

- [ ] Liste [1, 2, 3, 5, 8, 13], uzunluk 6.
- [ ] 15 sınırı ve döngü sonu doğru; sonsuz döngü yok.
- [ ] Kopyada değişiklik kaynak listeyi etkilemiyor.
- [ ] Durum geçişi eski iki değere dayanıyor; açıklama yalnız çıktının tekrarından oluşmuyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../04-more-control-flow-tools/4.1-if-statements/README.md)
<!-- learning-milestone:end -->
