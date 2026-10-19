## 14.2. Alternatives to the Interactive Interpreter

This facility is an enormous step forward compared to earlier versions of the interpreter; however, some wishes are left: It would be nice if the proper indentation were suggested on continuation lines (the parser knows if an `INDENT` token is required next). The completion mechanism might use the interpreter's symbol table. A command to check (or even suggest) matching parentheses, quotes, etc., would also be useful.

One alternative enhanced interactive interpreter that has been around for quite some time is [IPython](https://ipython.org/), which features tab completion, object exploration and advanced history management. It can also be thoroughly customized and embedded into other applications. Another similar enhanced interactive environment is [bpython](https://bpython-interpreter.org/).

<!-- learning-task:start -->
### Bölüm görevi

**Görev 14.2: Alternatif arayüzü ihtiyaca göre seç**

**Odak:** IPython/bpython yeteneklerini temel yorumlayıcı arayüzünden ayırma.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:14.1](../14.1-tab-completion-and-history-editing/README.md).

#### Tek görev

1. Kullanıcının nesne keşfi, gelişmiş geçmiş ve özelleştirme istediği bir durum için bölümde tanıtılan alternatifleri değerlendiren kısa seçim notu yaz.

2. Python dilini değiştirme ihtiyacıyla arayüz iyileştirme ihtiyacını ayır.

3. Notunda yalnız bu bölümün verdiği özellikleri kullan; herhangi bir paket kurman gerekmiyor.

#### Geçiş ölçütleri

- [ ] IPython özellikleri kaynakta verilenlerle gerekçelendirilmiş; bpython benzer alternatif olarak tanımlanmış.
- [ ] Arayüz seçimi kodun dil anlamını değiştiren işlem sayılmamış.
- [ ] Kaynakta öğretilmeyen magic komutlar, eklentiler veya kurulum gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
