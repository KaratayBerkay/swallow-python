## 4.10. Intermezzo: Coding Style

Now that you are about to write longer, more complex pieces of Python, it is a good time to talk about *coding style*. Most languages can be written (or more concisely, *formatted*) in different styles; some are more readable than others. Making it easy for others to read your code is always a good idea, and adopting a nice coding style helps tremendously for that.

For Python, [**PEP 8**](https://peps.python.org/pep-0008/) has emerged as the style guide that most projects adhere to; it promotes a very readable and eye-pleasing coding style. Every Python developer should read it at some point; here are the most important points extracted for you:

- Use 4-space indentation, and no tabs.

  4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.

- Wrap lines so that they don't exceed 79 characters.

  This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

- Use blank lines to separate functions and classes, and larger blocks of code inside functions.

- When possible, put comments on a line of their own.

- Use docstrings.

- Use spaces around operators and after commas, but not directly inside bracketing constructs: `a = f(1, 2) + g(3, 4)`.

- Name your classes and functions consistently; the convention is to use `UpperCamelCase` for classes and `lowercase_with_underscores` for functions and methods. Always use `self` as the name for the first method argument (see A First Look at Classes for more on classes and methods).

- Don't use fancy encodings if your code is meant to be used in international environments. Python's default, UTF-8, or even plain ASCII work best in any case.

- Likewise, don't use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.10: Aynı işlevi okunabilir biçimde yaz**

**Odak:** Dört boşluk, adlandırma, satır uzunluğu, boş satır, yorum, docstring ve UTF-8.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.8](../4.9-more-on-defining-functions/4.9.8-function-annotations/README.md).

#### Tek görev

1. Kendi yazdığın küçük bir fonksiyonu, örneğin combine fonksiyonunu, bölümdeki stil kurallarına göre düzenle.

2. Değişken ve fonksiyon adlarını ASCII ve lowercase_with_underscores biçiminde tut; docstring ve gerekli bir yorumu ekle.

3. Önceki ve sonraki sürümün aynı iki çağrıda aynı sonucu verdiğini kontrol et.

4. Sınıf adlandırma kuralını yalnız not et; yeni sınıf yazman gerekmiyor.

#### Geçiş ölçütleri

- [ ] Girintiler dört boşluk; sekme yok; satırlar 79 karakteri aşmıyor.
- [ ] Operatör çevresi ve virgül sonrası boşluklar, fonksiyonlar arası boş satırlar kurala uygun.
- [ ] Fonksiyon adı ve docstring kuralları uygulanmış; sınıflar için UpperCamelCase not edilmiş.
- [ ] Davranış aynı iki çağrıda korunmuş, dosya UTF-8 olarak kaydedilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
